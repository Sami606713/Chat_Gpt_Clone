import google.generativeai as genai
from PIL import Image
import pandas as pd
import streamlit as st
api_key="AIzaSyCXEwoavVZD14DNMOf-_I6Wtm3QFvFiu34"
genai.configure(api_key=api_key)

# Set up the model
def Response(text):
    model=genai.GenerativeModel('gemini-pro')
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
    ]

    model = genai.GenerativeModel(model_name="gemini-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    chat = model.start_chat(history=[])

    chat.send_message(text)
    return chat.last.text

# load image
def load_img(file_path):
    try:
        img=Image.open(file_path)
        return img
    except FileNotFoundError:
        return f"file not found {file_path}"


def file_csv(file):
    try:
        df=pd.read_csv(file)

        st.dataframe(df)

        return df
    except pd.errors.EmptyDataError:
        st.warning("The CSV file is empty.")
        return None
    except Exception as e:
        return e

def process_file(file):
    with st.spinner("Processing file...."):
        if file is None:
            st.warning("Please upload a file.")
            return

        if file.type=="text/csv":
            return file_csv(file)
        elif file.type=="image/jpeg":
            return st.image(load_img(file))
        elif file.type=="text/txt":
            content=file.read().decode("utf-8")
            st.code(content,language="plaintext")

            return content
        



# if __name__=="__main__":
#     print(Response("who are you"))