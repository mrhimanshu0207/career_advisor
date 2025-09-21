import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables (local dev)
load_dotenv()

# 🔑 Configure Gemini with API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(
    page_title="AI Career & Skills Advisor (Gemini)",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Career & Skills Advisor (Gemini)")
st.markdown("Your personalized AI buddy for career paths and skill growth 🚀")

# --- Input fields ---
name = st.text_input("👤 Your Name")
interests = st.text_area("✨ What are your interests? (e.g., coding, design, business)")
goals = st.text_area("🎯 Your Career Goals (e.g., software engineer, data scientist)")
skills = st.text_area("🛠️ Skills you already have")

# --- Generate Advice ---
if st.button("Get My Career Advice"):
    if not interests or not goals:
        st.warning("Please fill in your interests and career goals to continue.")
    else:
        with st.spinner("Gemini AI is preparing your personalized career roadmap..."):
            prompt = f"""
            A student named {name} has interests in {interests} and career goals as {goals}.
            Current skills: {skills}.
            
            Please suggest in a simple, student-friendly way:
            1. Suitable career paths
            2. Top 3 skills to learn next
            3. Best resources (free or popular platforms)
            4. A 3-step actionable roadmap to start today
            """

            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)

                st.subheader("📌 Personalized Career Guidance")
                st.write(response.text)

            except Exception as e:
                st.error(f"⚠️ Something went wrong: {e}")
