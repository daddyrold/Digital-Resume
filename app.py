from pathlib import Path

import streamlit as st
from PIL import Image

# ---PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"




# ---GENERAL SETTINGS ---
PAGE_TITLE = "DIGITAL CV | HAROLD TANQUIZON"
PAGE_ICON = ":wave:"
NAME = "HAROLD TANQUIZON"
DESCRIPTION = """
Data Analysist, assisting enterprises by supporting data-driven decision-amking.
"""
EMAIL ="haroldtanquizonofficial@gmail.com"
SOCIAL_MEDIA = {
    "Youtube": "https://www.youtube.com",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
}
PROJECTS  = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://www.youtube.com",
    "🏆 Income and Expenses Tracker - Web app with NoSQL database": "https://www.youtube.com",
}



st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

# ---LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#-- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
    
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📬", EMAIL)


# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 7 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sencse of initiative on tasks
    """
)


# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- Prograaming: Python and C#
- Data Visualization: MS Excel and Plotly
- Modeling: Logistic Regression, Linear Regression, Decition Trees
    """
)




# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

#---JOB 1 ---
st.write("📊", "**Data Analyst | ActiveSystems Software Inc.**")
st.write("2028/2029 - Present")
st.write(
    """
- Organizing the system in company.
    """
)

#---JOB 2 ---
st.write("#")
st.write("🌐", "**Web Developer | Mugna  Tech**")
st.write("2029/2030 - Present")
st.write(
    """
- Develop new website in the company that is more organize. 
    """
)

# -- Job 3 ---
st.write("#")
st.write("🛠️", "**Debugger | Fligno Software Philippines**")
st.write("2030/2035 - Present")
st.write(
    """
- Solving the error in websites and datasystems. 
    """
)











# --- PROJECTS AND ACCOMPLISHMENTS ---
st.write("#")
st.subheader("Projects and Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

























