import streamlit as st
from utils import Response,load_img,process_file
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
            st.markdown(f"<h1 style='text-align: center;'>Gpt-Clone</h1>", unsafe_allow_html=True)

    # make a empty chat list that can store the chat
    col1, col2 = st.columns(2)

    # Input field
    # with col1:
        # user_input = st.chat_input("Enter your text: ")

    # File uploader
    # with col2:
    file = st.file_uploader("", type=["csv","jpg","txt","py","js"])
    user_input = st.chat_input("Enter your text: ")
    with st.container(): 
        transform_file=process_file(file)
        if process_file(file)==None:
            transform_file=""
        else:
            transform_file=process_file(file)
        print(transform_file)
        if(user_input and transform_file is not None):
            st.write(user_input) 
            
            with st.spinner("waiting for chatgpt response...."):
                try:
                    response=Response(f"{transform_file} {user_input}")
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