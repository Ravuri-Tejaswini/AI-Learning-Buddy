
import streamlit as st
import google.generativeai as genai

# -------------------------------
# Configure Gemini API
# -------------------------------
genai.configure(api_key="YOUR_GOOGLE_API")
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.markdown("### Learn any topic with your friendly AI tutor **Binary Buddy** 🤖")

st.info(
    "👋 Welcome! Enter any topic, choose an activity, and let Binary Buddy help you learn step by step."
)

# -------------------------------
# User Input
# -------------------------------

topic = st.text_input("📚 Enter a Topic")

option = st.selectbox(
    "🎯 Choose Activity",
    (
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Evaluate My Answer",
        "Ask Anything"
    )
)

learner_answer = ""

if option == "Evaluate My Answer":
    learner_answer = st.text_area(
        "✍ Enter your answer"
    )

# -------------------------------
# Generate Button
# -------------------------------

if st.button("🚀 Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    persona = """
You are Binary Buddy.

You are a friendly, patient and encouraging AI tutor.

Rules:
- Explain concepts in beginner-friendly language.
- Break difficult ideas into simple steps.
- Encourage learners.
- Give accurate information.
- If you are unsure, say you are unsure instead of guessing.
- End with one motivational sentence.
"""

    if option == "Explain Concept":

        prompt = persona + f"""

Teach the topic: {topic}

Explain in simple language.

Explain step by step.

Use bullet points wherever helpful.

End with a short summary.
"""

    elif option == "Real-Life Example":

        prompt = persona + f"""

Topic: {topic}

Give one simple real-life example.

Explain why the example matches the topic.

Keep it beginner friendly.
"""

    elif option == "Generate Quiz":

        prompt = persona + f"""

Topic: {topic}

Generate 5 multiple-choice questions.

Requirements:

- Four options

- Mention correct answer

- Easy to moderate level
"""

    elif option == "Evaluate My Answer":

        if learner_answer.strip() == "":
            st.warning("Please enter your answer.")
            st.stop()

        prompt = persona + f"""

Topic:
{topic}

Student Answer:
{learner_answer}

Evaluate the answer.

Provide:

1. Correct points

2. Mistakes

3. Suggestions

4. Score out of 10

5. One encouraging sentence.
"""

    else:

        prompt = persona + f"""

Student Question:

{topic}

Answer clearly in simple language.
"""

    with st.spinner("Binary Buddy is thinking... 🤖"):
        response = model.generate_content(prompt)

    st.success("Response Generated Successfully!")

    st.markdown("## 📖 AI Response")

    st.write(response.text)

# -------------------------------
# Footer
# -------------------------------

st.markdown("---")

st.caption(
    "⚠ Responsible AI Notice: AI-generated responses may occasionally contain mistakes. Always verify important information using trusted learning resources."
)

st.caption("Developed using Streamlit + Google Gemini")
