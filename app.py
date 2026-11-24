
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="EduScore - Score Prediction",
    page_icon="🎓",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent

# LOAD MODEL
@st.cache_resource
def load_model():
    return joblib.load(BASE_DIR / "student_model.pkl")

model = load_model()

# CUSTOM CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef0ff, #f8f7ff);
    color: #202447;
}

.block-container {
    max-width: 850px;
    padding-top: 0.7rem;
    padding-bottom: 0.5rem;
}

header, footer {
    visibility: hidden;
}

h1, h2, h3 {
    color: #292653;
}

div[data-testid="stForm"] {
    background: white;
    border: 1px solid #e6e1fa;
    border-radius: 18px;
    padding: 15px 20px 12px 20px;
    box-shadow: 0 6px 22px rgba(56, 44, 120, 0.07);
}

div[data-testid="stNumberInput"] input {
    background: #f7f6ff;
    border-radius: 9px;
}

div[data-testid="stNumberInput"] label {
    color: #39345f;
    font-weight: 600;
    font-size: 13px;
}

div.stFormSubmitButton > button {
    background: linear-gradient(90deg, #6046c7, #9870e8);
    color: white;
    border: none;
    border-radius: 10px;
    height: 43px;
    font-size: 15px;
    font-weight: 700;
}

div.stFormSubmitButton > button:hover {
    color: white;
    border: none;
    background: #5036ad;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e5defa;
    border-radius: 13px;
    padding: 12px 16px;
}

div[data-testid="stMetricValue"] {
    color: #553bb1;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# HEADER - st.html RENDERS HTML DIRECTLY
st.html("""
<div style="
    background:linear-gradient(110deg,#282454,#5945B5,#9670E6);
    border-radius:18px;
    padding:19px 24px;
    margin-bottom:13px;
    color:white;
    text-align:center;
">
    <div style="font-size:29px;font-weight:800;">
        🎓 EduScore
    </div>
    <div style="font-size:19px;font-weight:600;margin-top:3px;">
        Student Score Prediction
    </div>
    <div style="font-size:12px;color:#E8E1FF;margin-top:5px;">
        Predict academic performance using Machine Learning
    </div>
</div>
""")

# INPUT FORM
with st.form("student_form"):

    st.markdown("### 📝 Enter Student Details")

    col1, col2 = st.columns(2, gap="medium")

    with col1:

        study = st.number_input(
            "📚 Study Hours Per Day",
            min_value=0.0,
            max_value=12.0,
            value=4.0,
            step=0.5
        )

        previous = st.number_input(
            "📊 Previous Exam Score",
            min_value=0.0,
            max_value=100.0,
            value=70.0
        )

        assignment = st.number_input(
            "📝 Assignment Average (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0
        )

    with col2:

        attendance = st.number_input(
            "📅 Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=85.0
        )

        sleep = st.number_input(
            "😴 Sleep Hours Per Day",
            min_value=0.0,
            max_value=12.0,
            value=7.0,
            step=0.5
        )

        practice = st.number_input(
            "🎯 Practice Tests Per Month",
            min_value=0,
            max_value=20,
            value=4
        )

    submitted = st.form_submit_button(
        "✨  PREDICT STUDENT SCORE",
        use_container_width=True
    )

# PREDICTION
if submitted:

    student = pd.DataFrame(
        [[
            study,
            attendance,
            previous,
            sleep,
            assignment,
            practice
        ]],
        columns=[
            "Study_Hours",
            "Attendance",
            "Previous_Score",
            "Sleep_Hours",
            "Assignment_Average",
            "Practice_Tests"
        ]
    )

    score = float(model.predict(student)[0])
    score = max(0, min(100, score))

    st.html(f"""
    <div style="
        background:linear-gradient(120deg,#e9e5ff,#f5efff);
        border:1px solid #d9cef9;
        border-radius:15px;
        padding:13px 18px;
        margin-top:12px;
        text-align:center;
    ">
        <div style="
            color:#67569c;
            font-size:12px;
            font-weight:700;
            letter-spacing:1px;
        ">
            YOUR PREDICTED FINAL SCORE
        </div>
        <div style="
            color:#4933a1;
            font-size:37px;
            font-weight:800;
            margin-top:2px;
        ">
            {score:.2f}
            <span style="font-size:17px;">/ 100</span>
        </div>
    </div>
    """)

    if score >= 75:
        st.success("Excellent! Strong estimated academic performance.")
    elif score >= 50:
        st.info("Good effort! There is scope for improvement.")
    else:
        st.warning("Additional academic support may be helpful.")

# FOOTER
st.html("""
<div style="
    text-align:center;
    color:#85809f;
    font-size:11px;
    padding:9px 0 0 0;
">
    EduScore | Python | Pandas | Machine Learning | Streamlit
</div>
""")
