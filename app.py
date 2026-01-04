import streamlit as st

st.title("WriteWise Lite ✍️")
st.write("AI helper for beginner content writers")

name = st.text_input("Your Name")
level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
topic = st.text_input("Enter a topic you want to write about")

if st.button("Generate Ideas"):
    if topic:
        st.subheader("Content Ideas")
        st.write(f"• Introduction to {topic}")
        st.write(f"• Common mistakes in {topic}")
        st.write(f"• How beginners can start with {topic}")

        st.subheader("Suggested Pricing")
        if level == "Beginner":
            st.write("₹0.5 – ₹1 per word")
        elif level == "Intermediate":
            st.write("₹2 – ₹3 per word")
        else:
            st.write("₹4 – ₹6 per word")
    else:
        st.warning("Please enter a topic")
