import streamlit as st
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re


st.set_page_config(
     page_title="Jeopardy Study Helper",
     page_icon="💰",
     layout="wide",
     initial_sidebar_state="expanded")

@st.cache
def load_data():
    df = pd.read_pickle("df.pkl")
    return df

df = load_data()

######################### INITIALIZATION ##########################
def load_page():
    #show question
    st.title('Jeopardy Study Helper')
    st.write(f'Question from category {st.session_state.text} for ${st.session_state.value}:')
    st.write(st.session_state.question['question'].to_list()[0] + '.')
    
# Add select box, slider to the sidebar:
st.sidebar.write('Select a category:')
category = st.sidebar.radio('',sorted(df.Category.unique()), key='category', on_change=load_page)
def set_amount(value):
    amount = st.sidebar.slider('Amount', min_value=200, max_value=1800, value=value, step=200, key='amount', on_change=load_page)
    return amount
amount = set_amount(200)

    
def generate_question(df=df, category=category, amount=amount):
    
    st.session_state.question = df[(df.Category == category) & (df.value == amount)].sample(n=1)
    st.session_state.text = st.session_state.question['category'].to_list()[0]
    st.session_state.value = st.session_state.question['value'].to_list()[0]
    st.session_state.answer = st.session_state.question['answer'].to_list()[0]
    
    load_page()
    #clear space for user input
    st.text_input("What is: ", '', key='user_input')
    
    return st.session_state.question, st.session_state.text, st.session_state.value, st.session_state.answer

# Initialization
if 'total' not in st.session_state:
    st.session_state['total'] = 0
if 'num_correct' not in st.session_state:
    st.session_state['num_correct'] = 0
if 'winnings' not in st.session_state:
    st.session_state['winnings'] = 0
if 'question' not in st.session_state:
    st.session_state['question'] = generate_question()[0]
if 'text' not in st.session_state:
    st.session_state['text'] = generate_question()[1]
if 'value' not in st.session_state:
    st.session_state['value'] = generate_question()[2]
if 'answer' not in st.session_state:
    st.session_state['answer'] = generate_question()[3]

    
######################### QUESTION SELECTION ##########################

def check_answer(answer=st.session_state.answer, user_input=st.session_state.user_input):
    if user_input == '':
        pass
    else:
        user_input = user_input.lower()
        user_input = re.sub(r'[^\w\s]','',user_input)
        answer = answer.lower()
        answer = answer.replace('/', ' ')
        answer = re.sub(r'[^\w\s]','',answer)
        similarity_score = fuzz.token_sort_ratio(user_input, answer)
        if (similarity_score > 95) or (user_input in answer):
            load_page()
            st.session_state.winnings +=  st.session_state.value
            st.session_state.num_correct +=1
            st.session_state.total += 1
            st.text_input("What is: ", user_input)
            st.write(f'Correct! The correct answer is {answer.title()}.')
            st.write(f'Your score is {st.session_state.num_correct}/{st.session_state.total} and winnings are ${st.session_state.winnings}')
        else:
            load_page()
            st.session_state.winnings -=  st.session_state.value
            st.session_state.total += 1
            st.text_input("What is: ", user_input)
            st.write(f'Incorrect. The correct answer is {answer.title()}.')
            st.write(f'Your score is {st.session_state.num_correct}/{st.session_state.total} and winnings are ${st.session_state.winnings}')
        
    if st.session_state.total >= 3:
        if (st.session_state.num_correct/float(st.session_state.total)) >= 0.75:
            st.success('You\'re on a roll! Consider moving up to the next $$ amount with the slider on the left.')
       
check_answer()


######################### BUTTONS ##########################

# two buttons: next question, reset score
next_button = st.button('Next Question', on_click=generate_question)

reset = st.button('Reset Score', on_click=generate_question)
if reset:
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]




