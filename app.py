import streamlit as st
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os

# Load environment variables (useful for local dev, not required on Streamlit Cloud)
load_dotenv()

# 🔑 Initialize OpenAI client with key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit page config
st.set_page_config(
    page_title="AI Career & Skills Advisor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Career & Skills Advisor")
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
        with st.spinner("AI is preparing your personalized career roadmap..."):
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
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500
                )

                st.subheader("📌 Personalized Career Guidance")
                st.write(response.choices[0].message.content)

            except RateLimitError:
                st.error("⚠️ The AI service is busy or you’ve hit the usage limit. Showing a sample roadmap instead.")

                # --- Fallback Demo Response ---
                st.subheader("📌 Sample Career Guidance (Demo)")
                st.write(f"""
                Hi {name if name else "Student"}! Based on your interests in **{interests}** 
                and goal to become a **{goals}**, here’s a quick roadmap:

                1. **Suitable Career Paths**  
                   - Junior {goals}  
                   - Freelance projects in {interests}  
                   - Entry-level internships  

                2. **Top 3 Skills to Learn Next**  
                   - Advanced {interests} skills  
                   - Communication & teamwork  
                   - Problem-solving with real projects  

                3. **Best Resources**  
                   - [freeCodeCamp](https://www.freecodecamp.org/)  
                   - [Coursera](https://www.coursera.org/)  
                   - [YouTube tutorials](https://www.youtube.com)  

                4. **3-Step Actionable Roadmap**  
                   - Step 1: Pick a small project related to your interest  
                   - Step 2: Learn one new skill daily for 30 days  
                   - Step 3: Apply for internships or freelance gigs  
                """)

            except Exception as e:
                st.error(f"⚠️ Something went wrong: {e}")
