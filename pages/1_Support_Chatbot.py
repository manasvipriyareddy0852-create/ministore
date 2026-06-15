import streamlit as st

st.title("💬 MiniStore Support")

if "messages" not in st.session_state:
    st.session_state.messages = []

products = [
    "Wireless Headphones",
    "Smart Watch",
    "Laptop Backpack",
    "Gaming Mouse",
    "Coffee Mug",
    "Desk Lamp"
]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask your question")

if user_input:

    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    text = user_input.lower()

    if "product" in text:
        reply = f"We currently offer: {', '.join(products)}."

    elif "delivery" in text:
        reply = "Delivery takes 3-7 business days."

    elif "refund" in text:
        reply = "Refunds are processed within 5 business days."

    elif "return" in text:
        reply = "Returns are accepted within 30 days."

    elif "payment" in text:
        reply = "We accept UPI, Credit Cards and Net Banking."

    elif "order" in text:
        reply = "Please provide your order ID."

    else:
        reply = "I can help with products, delivery, refunds, returns, payments, and orders."

    st.session_state.messages.append(
        {"role":"assistant","content":reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)