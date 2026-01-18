docker install

python -m venv .venv

source .venv/bin/activate

curl -fsSL https://ollama.com/install.sh | sh

ollama serve

ollama pull llama3.2:3b

ollama run llama3.2:3b "explain dockerfile best practices"

cd docker-agent

pip install -r requirements.txt

python3 -m agent.main

