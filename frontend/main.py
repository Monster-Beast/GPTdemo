import streamlit as st
import requests

st.set_page_config(page_title="ChatGPT Clone", layout="wide")
# 自定义CSS样式
st.markdown("""
<style>
.chat-container {
    max-width: 800px;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)
# 增加消息气泡CSS样式
st.markdown("""
<style>
.user-message {
    background-color: #dcf8c6;
    padding: 10px;
    border-radius: 10px;
    max-width: 70%;
    margin: 5px 0;
}
.bot-message {
    background-color: #f1f0f0;
    padding: 10px;
    border-radius: 10px;
    max-width: 70%;
    margin: 5px 0;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("会话历史")
if 'history' not in st.session_state:
    st.session_state.history = []
st.session_state.history.append({"user": "你好！"})
st.session_state.history.append({"bot": "你好！有什么我可以帮您的吗？"})
st.session_state.history.append({"user": "你好！"})
st.session_state.history.append({"bot": "你好！有什么我可以帮您的吗？"})


user_input = st.text_input("你:", key="input")
if st.button("发送"):
    if user_input:
        st.session_state.history.append({"user": user_input})
        response = requests.post("http://localhost:8000/chat/", json={"user_message": user_input})
        if response.status_code == 200:
            bot_response = response.json().get("response")
            st.session_state.history.append({"bot": bot_response})
        else:
            st.session_state.history.append({"bot": "Error: " + response.text})

for chat in st.session_state.history:
    if "user" in chat:
        st.markdown(f"""
        <div class="user-message">
            <strong>你:</strong> {chat['user']}
        </div>
        """, unsafe_allow_html=True)
    elif "bot" in chat:
        st.markdown(f"""
        <div class="bot-message">
            <strong>机器人:</strong> {chat['bot']}
        </div>
        """, unsafe_allow_html=True)