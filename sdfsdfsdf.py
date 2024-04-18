import streamlit as st
import openai



def askGpt(prompt):
    messages_prompt = [{"role":"system","content":prompt}]
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages_prompt)
    gptResponse = response["choices"][0]["message"]["content"]
    return gptResponse


st.set_page_config(page_title="요약프로그램")

def main():
    with st.sidebar:
        open_apikey = st.text_input(label='OPENAI API 키', placeholder = 'Enter Your API Key', type = 'password')
        if open_apikey:
            openai.api_key = open_apikey
    st.markdown('---')

st.header("요약프로그램")
st.markdown('---')
text = st.text_area(label = "야호")

if st.button("요약"):
    prompt = f''' You translte the "text" in english
    -text : {text}'''


    st.info(askGpt(prompt))

if __name__ == "__main__":
    main()



