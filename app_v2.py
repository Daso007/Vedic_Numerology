import streamlit as st
import google.generativeai as genai
import re

# Import all the corrected V2.2 calculator functions
from numerology_calculator_v2 import (
    calculate_psychic_number,
    calculate_destiny_number,
    calculate_kua_number,
    generate_complete_lo_shu_grid,
    get_birth_chart_digits
)

# --- CONFIGURATION & API KEY ---
# --- IMPORTANT: PASTE YOUR GOOGLE AI API KEY HERE ---
GOOGLE_API_KEY = "AIzaSyDEhhTw5iPc6RmiDji5aHvCzfe3P4saSBg"

# --- WEB APP INTERFACE ---
st.set_page_config(layout="wide", page_title="AI Numerology Platform")
st.title("AI-Powered Numerology & Career Guidance Platform")
st.write("Discover your inner self through a fusion of Vedic and Chinese numerology systems.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Personal Details")
    birth_date_input = st.text_input("Enter Date of Birth (DD/MM/YYYY)", "14/08/1996")
    # GENDER INPUT IS BACK and is required for the corrected Kua calculation
    gender_input = st.radio(
        "Select Your Gender:",
        ('Male', 'Female'),
        key="gender",
        horizontal=True
    )

with col2:
    st.subheader("Your Life Path & Aspirations")
    user_type = st.radio(
        "Select your current status:",
        ('Professional (Seeking Alignment)', 'Student (Exploring Options)'),
        key="user_type",
        horizontal=True
    )
    career_info_input = st.text_area(
        "Briefly describe your career/study information:",
        height=125,
        placeholder="e.g., 'Worked in marketing...' or 'I love science...'"
    )


# --- CORE LOGIC (Using st.cache_data for speed) ---
@st.cache_data
def generate_full_report(birth_date_str, gender, user_type, career_info):
    
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception:
        st.error("Error connecting to Google AI. Please check your API key in the `app_v2.py` file.")
        return None, None

    # Calculate ALL numerology data using the CORRECTED functions
    psychic_num = calculate_psychic_number(birth_date_str)
    destiny_num = calculate_destiny_number(birth_date_str)
    # The Kua number now correctly uses gender
    kua_num = calculate_kua_number(birth_date_str, gender)
    lo_shu_grid_text, all_digits = generate_complete_lo_shu_grid(birth_date_str, psychic_num, destiny_num, kua_num)
    
    missing_numbers = sorted(list(set(range(1, 10)) - set(all_digits)))
    
    try:
        with open("Cleaned-Knowledge-V2.txt", "r", encoding="utf-8") as f:
            full_knowledge_text = f.read()
    except FileNotFoundError:
        st.error("Knowledge base file 'Cleaned-Knowledge-V2.txt' not found.")
        return None, None
        
    # --- The Final V2 Master Prompt ---
    prompt = f"""
    You are an expert numerologist, skilled in Vedic and Chinese systems. Base your analysis ONLY on the context provided.
    
    **CLIENT'S DATA:**
    - Birth Date: {birth_date_str}
    - Gender: {gender}
    - Mulyank (Psychic Number): {psychic_num}
    - Bhagyank (Destiny Number): {destiny_num}
    - Kua Number: {kua_num}
    - Missing Numbers from Grid: {missing_numbers}
    - User Info: {user_type} - "{career_info}"

    **YOUR KNOWLEDGE BASE:**
    {full_knowledge_text}
    
    **REPORT STRUCTURE:**
    Generate a detailed, personalized report with these exact bolded headings:
    1. **Your Core Numerological Blueprint:** Briefly introduce their three core numbers (Mulyank, Bhagyank, Kua).
    2. **Your Psychic Number ({psychic_num}):** Analyze their personality and talents.
    3. **Your Destiny Number ({destiny_num}):** Explain their life's purpose.
    4. **Unlocking Luck with Your Kua Number ({kua_num}):** Explain their Kua meaning and give their favorable directions.
    5. **The Story of Your Lo Shu Grid:** Analyze the grid as a whole, focusing on populated Planes and missing numbers as lessons.
    6. **Career & Path Alignment:** Provide career/study advice based on ALL their numbers and user info.
    7. **Summary & Recommendations:** Conclude with 2-3 actionable tips.
    """
    
    response = model.generate_content(prompt)
    return lo_shu_grid_text, response.text

# --- Button to run the App ---
if st.button("✨ Generate My Complete Numerology Report ✨"):
    if re.match(r"^\d{2}/\d{2}/\d{4}$", birth_date_input):
        with st.spinner("Analyzing your complete numerological profile... This will just take a moment."):
            grid_display, report_text = generate_full_report(birth_date_input, gender_input, user_type, career_info_input)
        if grid_display and report_text:
            st.subheader("Your Complete Lo Shu Grid")
            st.text(grid_display)
            st.subheader("Your Personalized Analysis")
            st.markdown(report_text)
            st.success("Report Generated!")
    else:
        st.error("Invalid Date Format. Please use DD/MM/YYYY.")