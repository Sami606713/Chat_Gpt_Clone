import streamlit as st
from utils import Response
def main():
    with st.sidebar.container():
        st.title("history")

    with st.container():
        st.title("Chat Gpt Clone")

    # make a empty chat list that can store the chat 
    chat_history=[]
    user_input=st.chat_input("Enter your text: ")
    if (user_input):
        st.write(user_input)
        chat_history.append(user_input)
        with st.status("bot responding...."):
            response=Response(user_input)
        chat_history.append(response)
        st.write(response)
        
        st.empty()
        for message in chat_history:
            st.write(message)
        

    def Chat_Histort():
        pass
if __name__=="__main__":
    main()