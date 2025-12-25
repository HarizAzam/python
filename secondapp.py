import streamlit as st
#page setup
st.set_page_config(page_title="My Streamlit App - Hariz",layout="wide")

st.title("Layout and Sidebar")
col1 , col2 = st.columns(2)

with col1:
    st.header("Left Side")
    name = st.text_input('Enter Your Name ?')
    if name:
        st.success(f'Welcome User {name} !')

with col2:
    st.header("Odd Even Checker")
    num = st.slider("Select A Number",1,100,3)
    if num%2==0:
        st.write("Even Number")
    else:
        st.write("Odd Number")


with st.sidebar:
    st.header("Control Panel")
    user_color = st.color_picker("Pick Your Favourite Color","#000000")
    st.write("You have Selected : ",user_color)
