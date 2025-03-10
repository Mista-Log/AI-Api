import os
import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from dotenv import load_dotenv
load_dotenv()



class GeminiChatAPI(APIView):
    # parser_classes = [JSONParser]
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Initialize model configuration once (class-level)
    genai.configure(api_key=api_key)
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    
    system_instruction = (
        "Accept text prompts from users.\n"
        "Provide accurate Web3 and Solana-related responses using AI models trained on blockchain topics.\n"
        "Fetch real-time data from the Solana blockchain, including:\n"
        "Wallet balances\nRecent transactions\nSmart contract details\n"
        "Staking information\nNFT metadata (via Metaplex)\n"
        "Integrate Solana’s RPC API for blockchain interactions.\n"
        "Use Web3 authentication (e.g., Phantom Wallet) for personalized responses."
    )
    
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