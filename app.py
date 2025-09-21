import streamlit as st
import openai

# 🔑 Add your OpenAI API Key here
openai.api_key = st.secrets["OPENAI_API_KEY"]
st.set_page_config(page_title="AI Career & Skills Advisor", page_icon="🎓", layout="centered")

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

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )

            st.subheader("📌 Personalized Career Guidance")
            st.write(response["choices"][0]["message"]["content"])
