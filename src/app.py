import streamlit as st
from utils import Response
from PIL import Image

# Initialize the chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def main():
    # Set the main container for chat input
    with st.container():
        st.title("Chat Gpt Clone")

    # make a empty chat list that can store the chat 
    user_input=st.chat_input("Enter your text: ")
    # uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

    if(user_input):
        st.write(user_input) 
        
        with st.spinner("bot responding...."):
            response=Response(user_input)

        # Store the user input and resposne in sessin state
        st.session_state.chat_history.append(
            {
                "user":user_input,
                "bot":response
            }   
        )
        
        # Fetch result in session state and display the result
        for entry in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(f"{entry['user']}")
            
            with st.chat_message("assistant"):
                st.write(f"{entry['bot']}")
            st.empty()
    
    # Set the container for history
    with st.sidebar.container():
        st.title("history")
if __name__=="__main__":
    main()