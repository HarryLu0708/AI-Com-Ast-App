from langchain.chat_models import ChatOpenAI
# from langchain.schema import HumanMessage
from langchain.chains import LLMChain
import streamlit as st
from langchain.prompts import PromptTemplate

key = st.sidebar.text_input('OpenAI API Key')

def home():
    st.title("AI-powered Human Communication Assistant")
    st.write("Created by Harry Lu")
    st.markdown(
        """
        ## The Goal of This Project
        The purpose of this streamlit application is to using the power of AI to help human better communicate with each other. 
        ## Tech-Stack
        Technologies: Python, LangChain, Streamlit
        ## User Guide
        This app provides three AI assistants to help you complete different tasks:
        - Message Assistant: helps users to write better messages.
        - E-Mail Assistant: helps users to write better email.
        - Social Media Post Assistant: helps users to create better social media posts. 
        """
    )

def generate_message(target,event,tone,style,t):
    llm = ChatOpenAI(temperature=t, openai_api_key=key)
    template = """
    generate a message telling {target} {event} using {tone} tone and {style} style
    """
    prompt = PromptTemplate(template=template, input_variables=["target","event","tone","style"])
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain({'target':target,'event':event,'tone':tone,'style':style})
    st.code(response['text'],language="text")

def msg_ast():
    st.title('Messaging Assistant App')
    st.markdown(
        """
        ### User Guide
        - **Target**: The target to which this message was sent.
        - **Event**: The content or theme of this message. 
        - **Tone**: The tone of this message.
        - **Style**: The style of this message.
        - **Temparature**: The randomness of this message(0-lowest, 1-highest). 
        """
    )
    with st.form("message form"):
        target = st.text_input('Target','friend')
        event = st.text_input('Event:','go to eat breakfast')
        tone = st.text_input('Tone','friendly')
        style = st.text_input('Style','concise')
        temp = st.number_input("Temparature")
        submitted = st.form_submit_button('Submit')
        if not key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key to continue!')
        if submitted and key.startswith('sk-'):
            generate_message(target,event,tone,style,temp)

def generate_email(target,event,tone,style,t,your_name):
    llm = ChatOpenAI(temperature=t, openai_api_key=key)
    template = """
    generate a email telling {target} {event} using {tone} tone and {style} style, and my name is{your_name}
    """
    prompt = PromptTemplate(template=template, input_variables=["target","event","tone","style","your_name"])
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain({'target':target,'event':event,'tone':tone,'style':style,'your_name':your_name})
    st.code(response['text'],language="text")

def email_ast():
    st.title('E-Mail Assistant App')
    st.markdown(
        """
        ### User Guide
        - **Target**: The target to which this message was sent.
        - **Your Name**: User's name. 
        - **Event**: The content or theme of this message. 
        - **Tone**: The tone of this message.
        - **Style**: The style of this message.
        - **Temparature**: The randomness of this message(0-lowest, 1-highest). 
        """
    )
    with st.form("email form"):
        target = st.text_input('Target','friend')
        your_name = st.text_input('Your Name','Harry')
        event = st.text_input('Event:','go to eat breakfast')
        tone = st.text_input('Tone','friendly')
        style = st.text_input('Style','concise')
        temp = st.number_input("Temparature")
        submitted = st.form_submit_button('Submit')
        if not key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key to continue!')
        if submitted and key.startswith('sk-'):
            generate_email(target,event,tone,style,temp,your_name)

def generate_post(target,event,tone,style,t,platform,theme):
    llm = ChatOpenAI(temperature=t, openai_api_key=key)
    template = """
    generate a post for {platform} for {event} about {theme} using {tone} tone and {style} style, the audiences for this post are {target}
    """
    prompt = PromptTemplate(template=template, input_variables=["target","event","tone","style","platform"])
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain({'target':target,'event':event,'tone':tone,'style':style,'platform':platform,'theme':theme})
    st.code(response['text'],language="text")

def post_ast():
    st.title('Social Media Post Assistant App')
    st.markdown(
        """
        ### User Guide
        - **Target**: The target to which this message was sent.
        - **Platform**: The platform that you want to post on. 
        - **Event**: The content or theme of this message. 
        - **Theme**: The theme of this social media post. 
        - **Tone**: The tone of this message.
        - **Style**: The style of this message.
        - **Temparature**: The randomness of this message(0-lowest, 1-highest). 
        """
    )
    with st.form("post form"):
        target = st.text_input('Audience','gamer')
        platform = st.text_input('Platform','twitter')
        event = st.text_input('Event','gaming')
        theme = st.text_input('Theme','Hearthstone')
        tone = st.text_input('Tone','funny')
        style = st.text_input('Style','concise')
        temp = st.number_input("Temparature")
        submitted = st.form_submit_button('Submit')
        if not key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key to continue!')
        if submitted and key.startswith('sk-'):
            generate_post(target,event,tone,style,temp,platform,theme)

pages = {
    "Home":home,
    "Message Assistant": msg_ast,
    "Email Assistant": email_ast,
    "Social Media Post Assistant": post_ast
}


app = st.sidebar.selectbox("Choose a mode",pages.keys())
pages[app]()
