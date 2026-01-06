"""
Simple Chatbot with Memory using Groq API
Model: Llama 3.1 8B Instant
Author: Ganesh Vempati
Date: January 6, 2026
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Store conversation history
conversation_history = []

def chat(user_message):
    """
    Send message to Groq API and get response
    
    Args:
        user_message (str): User's input message
    
    Returns:
        str: Assistant's response
    """
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    try:
        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fast, efficient model
            messages=conversation_history,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            stream=False
        )
        
        # Get assistant's reply
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Main chatbot loop"""
    print("=" * 60)
    print("🤖 Simple Chatbot with Groq (Llama 3.1 8B Instant)")
    print("=" * 60)
    print("\nCommands:")
    print("  - Type your message to chat")
    print("  - Type 'quit', 'exit', or 'bye' to exit")
    print("  - Type 'clear' to clear conversation history")
    print("=" * 60)
    
    while True:
        # Get user input
        user_input = input("\n😊 You: ").strip()
        
        # Exit condition
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Goodbye! Thanks for chatting!")
            break
        
        # Clear history
        if user_input.lower() == 'clear':
            conversation_history.clear()
            print("\n🗑️  Conversation history cleared!")
            continue
        
        # Skip empty input
        if not user_input:
            print("⚠️  Please enter a message.")
            continue
        
        # Get response
        print("\n🤖 Bot: ", end="", flush=True)
        response = chat(user_input)
        print(response)

if __name__ == "__main__":
    # Check if API key exists
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY not found in .env file")
        print("Please create a .env file with your Groq API key")
        print("Example: GROQ_API_KEY=your-key-here")
    else:
        main()
