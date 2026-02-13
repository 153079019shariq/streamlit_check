import streamlit as st

st.title("Welcome to streamlit")

if st.checkbox("Display_widget"):
  # display the text if the checkbox returns True value
  st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")

if(st.button("Click me")):
   st.text("button_click")

def square(num):
   return num*num

num = st.number_input("Enter a number")
if(st.button("Calculate_square")):
   result = square(num)
   st.text(result)