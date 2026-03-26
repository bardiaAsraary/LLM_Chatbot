# LLM_Chatbot
A fast, free CLI chatbot powered by Groq (Llama 3.3 70B) with persistent conversation memory. Fully containerized with Docker for easy setup and deployment.

# Groq Chatbot Setup Script
# This script clones the repo, sets up environment variables, and runs the chatbot with Docker

# --- 1. Clone the repository ---
echo "Cloning the repository..."
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name || { echo "Failed to enter repo directory"; exit 1; }

# --- 2. Set up Groq API Key ---
echo "Creating .env file..."
read -p "Enter your Groq API Key: " GROQ_KEY
cat <<EOL > .env
GROQ_API_KEY=$GROQ_KEY
MODEL=llama-3.3-70b-versatile
EOL
echo ".env file created."

echo "You can get a free API key from: https://console.groq.com/keys"

# --- 3. Build and run chatbot ---
echo "Starting chatbot using Docker Compose..."
docker-compose up --build -d

echo "Chatbot is running!"
echo "To chat interactively, use: docker-compose run --rm chatbot"
echo "Type 'exit', 'quit', or 'bye' to stop."
echo "Your conversation history is saved in app/data/conversations.json."
