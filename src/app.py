import streamlit as st
from utils import Response,load_img
# from PIL import Image

# Initialize the chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def main():
    # load the image so i can use in later
    logo_img=load_img("images/logo/chet.jpeg")
    # Set the main container for chat input
    with st.container():
        with st.container():
            st.image(logo_img, caption="ChatGPT Clone", use_column_width=False)
            st.title("Chat Gpt Clone")

    # make a empty chat list that can store the chat 
    user_input=st.chat_input("Enter your text: ")

    if(user_input):
        st.write(user_input) 
        
        with st.spinner("waiting for chatgpt response...."):
            try:
                response=Response(f"find best result of this input: {user_input}")
            except Exception as e:
                response=e

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
        st.title("User History")
        try:
            for entry in st.session_state.chat_history:
                st.write(f"{entry['user']}")
        except Exception as e:
            st.write(e)
        
if __name__=="__main__":
    main()