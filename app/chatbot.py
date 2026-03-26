from openai import OpenAI
from memory import load_memory, save_memory   # Changed import
from config import GROQ_API_KEY, MODEL

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def chat():
    print("🤖 Groq Chatbot is ready! (Type 'exit', 'quit', or 'bye' to stop)\n")
    
    messages = load_memory()
    
    if not messages or messages[0]["role"] != "system":
        messages.insert(0, {
            "role": "system",
            "content": "You are a helpful, friendly, and concise assistant."
        })
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("👋 Goodbye! Conversation saved.")
                break
                
            if not user_input:
                continue
            
            messages.append({"role": "user", "content": user_input})
            
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )
            
            assistant_reply = response.choices[0].message.content
            
            messages.append({"role": "assistant", "content": assistant_reply})
            save_memory(messages)
            
            print(f"Groq: {assistant_reply}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            if "429" in str(e) or "rate limit" in str(e).lower():
                print("→ Rate limit reached. Please wait a few seconds and try again.\n")

if __name__ == "__main__":
    chat()