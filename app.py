import streamlit as st
from hindsight_client import Hindsight
from groq import Groq

st.set_page_config(
    page_title="SupportIQ",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 SupportIQ")
st.markdown(
    "### AI Customer Support with Persistent Memory"
)
st.caption(
    "Remember every customer interaction. Respond with context. "
    "Improve support over time."
)


st.write(
    "SupportIQ remembers important customer information and "
    "uses previous conversations to provide personalized support."
)

BANK_ID = "supportiq_demo"
def get_customer_bank_id(customer_id):
    return f"supportiq_{customer_id.strip().lower().replace('-', '_')}"
def ensure_customer_bank(customer_id):
    bank_id = get_customer_bank_id(customer_id)

    with Hindsight(base_url="http://localhost:8888") as client:
        try:
            client.create_bank(
                bank_id=bank_id,
                name=f"SupportIQ {customer_id}"
            )
        except Exception:
            pass

    return bank_id
def recall_memories(customer_id, customer_message):
    with Hindsight(base_url="http://localhost:8888") as client:
        memories = client.recall(
            bank_id=get_customer_bank_id(customer_id),
            query=customer_message
        )
    return memories.results


def generate_response(customer_name, customer_message, memories):
    memory_text = "\n".join(
        f"- {memory.text}"
        for memory in memories
    )

    system_prompt = f"""
You are SupportIQ, an intelligent customer-support assistant.
Customer name:
{customer_name}
Your job is to help customers using relevant information from
their previous interactions.

IMPORTANT RULES:
- Use remembered information when it is relevant.
- Do not invent customer information.
- Do not invent email addresses, phone numbers, company names,
  ticket numbers, or policies.
- Do not claim that you can arrange calls, send emails, create tickets,
  contact staff, or perform actions that are not actually available.
- Do not promise that SupportIQ will run diagnostics, investigate issues,
  contact the customer later, or provide a future update unless the user
  has explicitly provided a real system capability that allows it.
- Treat remembered conversations only as customer context. Never treat remembered promises, suggested actions, or past assistant statements as proof that SupportIQ can perform those actions.
- Only describe actions that SupportIQ can perform in this application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
- Do not add signatures or fake contact details.
- Keep the response concise and practical.
- Give clear next steps.
- If important information is missing, ask the customer for it.
- Never say that you will run diagnostics, investigate the issue, contact the customer later, or send/get back to the customer by email.
- You must never promise any future action or follow-up. Do not say "I will investigate", "I will get back to you", "I will send an email", "we will contact you", or similar.
- Your response must only describe what the customer can do right now in this chat.
- If the customer prefers email, acknowledge that preference but do not claim that SupportIQ can send email.
Remembered customer information:
{memory_text}

Respond naturally as a professional customer-support agent.
"""

    groq_client = Groq()

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": customer_message
            }
        ]
    )

    return response.choices[0].message.content


def store_memory(customer_id, customer_name, customer_message, assistant_response):
    with Hindsight(base_url="http://localhost:8888") as client:
        client.retain(
            bank_id=get_customer_bank_id(customer_id),
            content=f"""
Customer ID:
{customer_id}

Customer name:
{customer_name}

Customer message:
{customer_message}

SupportIQ response:
{assistant_response}
"""
        )


st.divider()
customer_id = st.text_input(
    "🆔 Customer ID",
    placeholder="Example: CUST-001",
    help="Use a unique customer ID so SupportIQ keeps different customers' memories separate."
)
customer_name = st.text_input(
    "👤 Customer Name",
    placeholder="Example: Rahul",
    help="Enter the customer's name so SupportIQ can connect the conversation with their remembered context."
)
    
    

customer_message = st.text_area(
    "💬 Customer Message",
    placeholder="Example: Hi, I'm Rahul again. We're still having the reporting problem.",
    height=140,
    help="Enter the customer's current support request. SupportIQ will recall relevant previous interactions."
)
    
    
    


if st.button("🚀 Send to SupportIQ", type="primary"):

    if customer_id.strip() and customer_message.strip():

     ensure_customer_bank(customer_id)

    with st.spinner("Recalling customer memory..."):
        memories = recall_memories(customer_id, customer_message)

        with st.spinner("Generating personalized response..."):
            response = generate_response(
                customer_name,
                customer_message,
                memories
            )

        store_memory(
            customer_id,
            customer_name,
            customer_message,
            response
        )

        st.divider()

        st.subheader("🤖 SupportIQ Response")
        st.success(response)

        st.subheader("🧠 Hindsight Memory Used")
        st.caption(
            "Relevant information recalled from previous customer interactions."
        )

        if memories:
            for memory in memories:
                st.info(memory.text)
        else:
            st.write("No previous relevant memories found.")

else:
        st.warning("Please enter both a Customer ID and a customer message.")