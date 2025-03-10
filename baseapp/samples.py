# from django.shortcuts import render

# Create your views here.
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# load_dotenv()


# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Create the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-2.0-flash",
#   generation_config=generation_config,
#   system_instruction="Accept text prompts from users.\nProvide accurate Web3 and Solana-related responses using AI models trained on blockchain topics.\nFetch real-time data from the Solana blockchain, including:\nWallet balances\nRecent transactions\nSmart contract details\nStaking information\nNFT metadata (via Metaplex)\nIntegrate Solana’s RPC API for blockchain interactions.\nUse Web3 authentication (e.g., Phantom Wallet) for personalized responses.",
# )

# history = []

# print("Bot: Hello, how can i help you today?")

# while True:

#   user_input = input("You: ")

#   chat_session = model.start_chat(
#     history=history
#   )

#   response = chat_session.send_message(user_input)

#   model_response = response.text
#   print(f'Bot: {model_response}')

#   history.append({"role": "user", "parts": [user_input]})
#   history.append({"role": "user", "parts": [model_response]})


# Run the chat


# import os
# import google.generativeai as genai
# from django.views import View
# from django.http import JsonResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# Configure GenAI once when the server starts
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#     model_name="gemini-2.0-flash",
#     generation_config=generation_config,
#     system_instruction="""Accept text prompts from users.
#     Provide accurate Web3 and Solana-related responses using AI models trained on blockchain topics.
#     Fetch real-time data from the Solana blockchain, including:
#     Wallet balances
#     Recent transactions
#     Smart contract details
#     Staking information
#     NFT metadata (via Metaplex)
#     Integrate Solana’s RPC API for blockchain interactions.
#     Use Web3 authentication (e.g., Phantom Wallet) for personalized responses."""
# )



# @method_decorator(csrf_exempt, name='dispatch')
# class GeminiChatView(View):
#     def get(self, request):
#         """Handle initial GET request with greeting"""
#         request.session['chat_history'] = []  # Initialize fresh session
#         return JsonResponse({"response": "Hello, how can I help you today?"})

#     def post(self, request):
#         """Handle POST requests with user input"""
#         user_input = request.POST.get('user_input', '')
#         chat_history = request.session.get('chat_history', [])
        
#         try:
#             # Start chat with current history
#             chat_session = model.start_chat(history=chat_history)
#             response = chat_session.send_message(user_input)
#             model_response = response.text

#             # Update chat history (note: you might want to fix the role for bot responses)
#             chat_history.append({"role": "user", "parts": [user_input]})
#             chat_history.append({"role": "user", "parts": [model_response]})
            
#             # Save updated history to session
#             request.session['chat_history'] = chat_history
#             request.session.modified = True

#             return JsonResponse({"response": model_response})
        
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)