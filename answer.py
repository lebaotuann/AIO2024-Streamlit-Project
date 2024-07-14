import streamlit as st

from constants import DATA_DIRECTORY_PATH

st.title("Question 1: st.text(...) => A")
st.text("Answer: A")

st.title("Question 2: C")
options = st.multiselect(
    "Your favorite colors:", ["Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"]
)
st.write("You selected:", options)

st.title("Question 3: st.text_input(...) => D")
your_name = st.text_input("Enter your name:")
if your_name:
    st.write(f"Hello, {your_name}!")

st.title("Question 4: C")
image_path = DATA_DIRECTORY_PATH + "/data/cat.jpg"
# Specify color channels (options: 'RGB', 'BGR', 'GRAY')
st.image(image_path, caption="A cat", width=100, channels="RGB")
st.image(image_path, caption="A cat", width=None, channels="BGR")
st.image(image_path, caption="A cat", width=None, channels="RGB")

st.title("Question 5: A")

st.title("Question 6: D")

st.title("Question 7: D")
with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, " - Last Name:", l_name)

st.title("Question 8: A")
uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)

st.title("Question 9: D")

st.title("Question 10: B")
