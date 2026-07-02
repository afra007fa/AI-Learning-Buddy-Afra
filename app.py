import streamlit as st
from google import genai
import os

# Configure Gemini API
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="AI Learning Buddy Afra",
    page_icon="🎓"
)

# Title
st.title("🎓 AI Learning Buddy Afra")

# User input
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# Generate button
if st.button("Generate"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        else:
            prompt = topic

        try:
            with st.spinner("Generating response..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
