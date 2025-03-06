import streamlit as st
import pandas as pd
from io import BytesIO
import random
from fpdf import FPDF

st.title("🌱 Growth Mindset App")

st.write("Welcome to the Growth Mindset App! A place where dreams grow, resilience thrives, and you become unstoppable! 🚀")

# Goal Setting
st.subheader("🎯 Set Your Goal")
goal = st.text_input("What’s your biggest dream right now?")
if st.button("Lock It In! 🔥"):
    st.success(f"Boom! Your goal is set: {goal} 💪")

# Progress Tracker
st.subheader("📊 Track Your Progress")
progress = st.slider("How far have you come?", 0, 100, 0)
st.progress(progress / 100)
st.write(f"You're {progress}% closer to greatness! Keep pushing! 🚀")

# Habit Tracker
st.subheader("🔄 Build Winning Habits")
habit = st.text_input("What's the power habit you're building?")
habit_days = st.number_input("For how many days?", min_value=1, max_value=365, value=30)
if st.button("Commit! 💥"):
    st.success(f"Yes! '{habit}' is your new superpower for {habit_days} days! 🏆")

# Daily Journaling
st.subheader("📖 Write Your Growth Story")
journal_entry = st.text_area("Pour your heart out. What went great today? What’s the next step?")
if st.button("Save My Thoughts ✍️"):
    st.success("Your words are magic! Saved and stored. ✨")

# Daily Affirmation
affirmations = [
    "I am unstoppable and full of potential! 💥",
    "Every challenge makes me stronger! 💪",
    "I am becoming the best version of myself! 🌟",
    "I embrace growth and learning every day! 📚",
    "Success is my destiny! 🚀",
]
st.subheader("💡 Today's Power Affirmation")
st.write(random.choice(affirmations))


# Generate and Download Progress Report in PDF
def generate_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, "Your Growth Mindset Report", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Goal: {goal}\n\n")
    pdf.multi_cell(0, 10, f"Progress: {progress}%\n\n")
    pdf.multi_cell(0, 10, f"Habit: {habit} ({habit_days} days)\n\n")
    pdf.multi_cell(0, 10, f"Journal Entry:\n{journal_entry}\n\n")
    
    pdf_output = BytesIO()
    pdf_bytes = pdf.output(dest='S').encode('latin1')  # Generate PDF as a string and encode
    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)
    return pdf_output

st.subheader("📜 Download Your Growth Report")
if st.button("Get My Progress Report 📄"):
    pdf_file = generate_pdf()
    st.download_button(
        label="Download as PDF",
        data=pdf_file,
        file_name="growth_mindset_report.pdf",
        mime="application/pdf"
    )

st.write("Stay focused, stay unstoppable! 🚀")
