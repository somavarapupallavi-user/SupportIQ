🧠 SupportIQ

AI Customer Support with Persistent Memory

SupportIQ is an AI-powered customer support assistant that remembers important information from previous customer conversations and uses that context to provide more personalized support.

Unlike a stateless chatbot, SupportIQ uses Hindsight as a persistent memory layer so the assistant can recall relevant customer information across conversations.

🎯 Problem

Traditional AI support assistants often treat every conversation as a new conversation.

This can lead to:

- Repeated questions
- Loss of customer context
- Generic responses
- Poor continuity between support interactions

💡 Solution

SupportIQ gives the AI assistant persistent customer memory.

For each customer, SupportIQ can remember relevant information such as:

- Previous support issues
- Customer preferences
- Company or product context
- Earlier conversation details

When the customer returns, SupportIQ recalls relevant memories and uses them to generate a more contextual response.

🧠 How Hindsight Is Used

SupportIQ uses Hindsight as the memory layer.

The workflow is:

Customer
   ↓
SupportIQ Web Interface
   ↓
Customer-specific Hindsight Memory
   ↓
Relevant Memories
   ↓
LLM
   ↓
Personalized Support Response

Each customer is assigned a separate Hindsight memory bank. This keeps customer memories isolated from one another.

Example

First conversation:

«Hi, our reports are taking too long to generate.»

SupportIQ stores the relevant conversation as memory.

Later conversation:

«Hi, I'm Rahul again. We're still having the reporting problem. What should I do next?»

SupportIQ recalls the previous reporting issue and uses that context when generating the response.

This demonstrates how persistent memory improves continuity between support interactions.

✨ Key Features

- 🧠 Persistent customer memory using Hindsight
- 👤 Customer-specific memory isolation
- 💬 Context-aware support responses
- 🔄 Memory recall across conversations
- 🤖 LLM-powered responses using Groq
- 🌐 Simple Streamlit web interface

🛠️ Technology Stack

- Python
- Streamlit
- Hindsight
- Groq
- "openai/gpt-oss-120b"
- Git & GitHub

🚀 Running Locally

1. Clone the repository

git clone https://github.com/somavarapallavi-user/SupportIQ.git
cd SupportIQ

2. Create a virtual environment

python -m venv .venv

3. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

4. Install dependencies

pip install streamlit hindsight-client groq

5. Configure environment variables

Set the required Hindsight and Groq environment variables using your own API keys.

Do not commit API keys or other secrets to GitHub.

6. Start Hindsight

Run the Hindsight API locally on port "8888".

7. Start SupportIQ

streamlit run app.py

The Streamlit application will normally open at:

http://localhost:8501

🔐 Privacy and Isolation

SupportIQ uses a separate Hindsight memory bank for each customer ID.

For example:

CUST-001 → supportiq_cust_001
CUST-002 → supportiq_cust_002

This prevents memories from different customer IDs from being intentionally stored in the same memory bank.

📌 Project Scope

SupportIQ focuses on one clear workflow:

AI-powered customer support with persistent customer memory.

The goal is to demonstrate how memory can make support conversations more contextual and continuous over time.

👩‍💻 Project

SupportIQ

Built by Pallavi Somavarapu