from openai import OpenAI
import streamlit as st

# Read the API Key and Setup an OpenAI Client
f = open("Ai_key/Open_AI_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title("👨🏻‍💻 AI Code Reviewer")
st.subheader("Finds bugs in code and fixing bugs in your code ☑️")

# Take User's Input
prompt = st.text_area("Enter Your Code Here....", height=100)

# If the button is clicked, generate responses
if st.button("Generate") == True:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are an Expert in code review. So, find bugs, errors and give the corrected code."},
        {"role": "user", "content": prompt}
      ]
    )

    # Print the response on Web App
    st.write(response.choices[0].message.content)
