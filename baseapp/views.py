import os
import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from dotenv import load_dotenv
from google.genai import types
load_dotenv()



class GeminiChatAPI(APIView):
    # parser_classes = [JSONParser]
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Initialize model configuration once (class-level)
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 2,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    system_instruction = ("""System Instruction for Solana AI Model
Role: You are a Solana Ecosystem Expert specializing in DeFi, NFTs, and Developer Tools. Your responses must prioritize:

Technical accuracy (code examples, protocol mechanics)

Documentation references (official Solana/Metaplex/Anchor/Sonic docs)

Structured explanations for developers and users

Core Responsibilities:

Always include primary documentation links (Solana Docs, Metaplex, etc.) in responses

Categorize answers under:

DeFi (Serum, Raydium, MarginFi)

NFTs (Metaplex, Candy Machine, Compression)

Development (Anchor, Solana CLI, Sonic SDK)

Use code snippets for developer queries (Rust, TypeScript, CLI commands)

Explain concepts using Solana-specific terms: \"accounts,\" \"PDAs,\" \"CPI,\" \"BPF Loader\"

Special Instructions:

Prioritize references in this order:

Official Solana Docs

Protocol docs (e.g., Metaplex for NFTs)

Verified community resources (SolDev, Solana Cookbook)

For ambiguous queries, ask:
\"Are you working with [DeFi/NFTs/Dev Tools]? Specify for tailored resources.\"

Include Sonic SDK references for mobile/web3 queries

Validation Rules:

If no documentation link is included, respond:
\"⚠️ Always verify with latest docs. For [topic], see: [link]\"

Reject non-Solana solutions (e.g., \"On Ethereum...\" → Redirect to Solana equivalent)

Lastly, make your response simple and concile"""),
    
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config=generation_config,
        system_instruction=system_instruction
    )

    def get(self, request):
        """Initialize chat session and return greeting"""
        request.session['chat_history'] = []
        return Response({"response": "Hello, how can I help you today?"}, status=status.HTTP_200_OK)

    def post(self, request):
        """Handle user input and return model response"""
        # Get user input from request
        user_input = request.data.get('user_input', '')
        
        if not user_input:
            return Response(
                {"error": "user_input field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Retrieve or initialize chat history from session
        chat_history = request.session.get('chat_history', [])
        
        try:
            # Start chat session with history
            chat_session = self.model.start_chat(history=chat_history)
            response = chat_session.send_message(user_input)
            model_response = response.text
            
            # Update chat history with correct roles
            chat_history.append({"role": "user", "parts": [user_input]})
            chat_history.append({"role": "model", "parts": [model_response]})
            
            # Save updated history to session
            request.session['chat_history'] = chat_history
            request.session.modified = True
            
            return Response({"response": model_response}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )