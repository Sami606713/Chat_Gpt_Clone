import streamlit as st
from utils import Response,load_img,process_file
# from PIL import Image

# Initialize the chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Set the page layout and title
st.set_page_config(
    page_title="Chat-Gpt Clone",  # Set the page title
    page_icon=":chart_with_upwards_trend:",  # Set a favicon for the page (optional)
    layout="wide",  # Set the layout ("wide" or "centered")
    initial_sidebar_state="auto"  # Set the initial sidebar state ("auto", "expanded", "collapsed")
)
def main():
    # load the image so i can use in later
    # logo_img=load_img("images/logo/chet.jpeg")
    # Set the main container for chat input
    with st.container():
        with st.container():
            # st.image(logo_img, caption="ChatGPT Clone", use_column_width=False)
            st.markdown(f"<h1 style='text-align: center;'>Gpt-Clone</h1>", unsafe_allow_html=True)

    # make a empty chat list that can store the chat
    col1, col2 = st.columns(2)

    file = st.file_uploader("", type=["csv"])
    user_input = st.chat_input("Enter your text: ")
    with st.container():
        transform_file=process_file(file)
        if(transform_file is not None):
            transform_file=transform_file    
        else:
            transform_file=""
        # print(transform_file)
        if(user_input and transform_file is not None):
            st.write(user_input) 
            
            with st.spinner("waiting for chatgpt response...."):
                try:
                    response=Response(f"{transform_file} {user_input}")
                    st.write(response)
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
            
if __name__=="__main__":
    main()