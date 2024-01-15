import streamlit as st

def main():
    st.set_page_config(page_title='Ask your CSV')
    st.header('Ask your CSV')

    user_csv = st.file_uploader('Upload your csv file', type='csv')

    if user_csv is not None:
        user_question = st.text_input('Ask a question about your CSV')
    


if __name__ == '__main__':
    main()
