from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Nikola Kuzmanovic"
PAGE_ICON = ":wave:"
NAME = "Nikola Kuzmanovic"
DESCRIPTION = """
Senior Reservoir Engineer / Data Science
"""
EMAIL = "nikola.kuzmanovic@rgf.rs"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/nikola-kuzmanovic-4089b0236/",
}

PHONE= "+381644042145"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫 Email:", EMAIL)
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write("Social media: "f"[{platform}]({link})")
    st.write("📞 Phone:", PHONE)        



# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("---")
st.write(
    """
- ✔️ Highly analytical and results-driven Reservoir Engineer with 6 years of experience in conventional and unconventional asset development across the Balkan, Africa and Russia regions
- ✔️ Proven expertise in reservoir simulation, production forecasting, reserves estimation, and optimizing field performance
- ✔️ Adept at leveraging advanced analytical tools (Eclipse, Petrel RE, Python) to solve complex subsurface challenges and support strategic decision-making
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Streamlit, Tkinter), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
- 💻 Other : Schlumberger Petrel, Eclipse 100, 300 , Tnavigator (Model designer, Geology designer, Simulation),MBAL, PETEX, PVTSim Nova OFM, NGT
"""
)




# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Reservoir Engineer | NIS a.d Novi Sad, Republic of Serbia**")
st.write("04/2023 - Present")
st.write(
    """
- ► Responsible for big field numerical simulation of low permeability (<5 mD) reservoir in Western Siberia.
- ► Managed a field containing over 2,000 wells with hydraulic fracturing, water injection support, and a history period over 20 years, including sector modeling, upscaling, fracture modeling, and AHM
- ► Led and participated in integrated reservoir multidisciplinary studies in Serbia throughout all milestones of data analysis, model construction, history matching, calibration, and prediction
- ► Developed and implemented new software using Python for efficient Schedule creation, DCA, WOR analysis, and Chan Plots
- ► Mentored entry-level engineers, providing career guidance and technical support.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Reservoir Engineer | NIS a.d Novi Sad, Republic of Serbia**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Calculated reserves and recovery, generated production forecasts, and created/optimized field development plans using material balance and decline applications
- ► Computed OOIP or OGIP for oil and gas reservoirs using IPM (MBAL) software.
- ► Responsible for creating OFM databases for oil & gas fields.Built OFM projects (plots, DCA, reports), managed well completions and well logs, and constructed different maps to aid in field analysis 
- ► Performed fluid & PVT analysis, including extensive fluid characterization using EOS, PVT packages, and PVT properties calculation based on laboratory tests or correlations.
- ► Designed, QC'd, and analyzed reservoir studies, e.g., RCA, SCA

"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write(
    """
- 🎓 Master of Science | "Gubkin" Russian State University of Oil and Gas | Russian Federation, 2020
- 🎓 Bachelor of Science | Faculty of Mining and Geology, Belgrade University | Republic of Serbia,  2017
- 🎓 Database course (SQL, PlSQL) | FTN Informatika | Republic of Serbia,  2022
- 🎓 Java Web Development course | FTN Informatika | Republic of Serbia,  2023
"""
)

# --- COURSES ---
st.write('\n')
st.subheader("Certifications/Courses")
st.write("---")
st.write(
    """
- 💡 Underground CO2 storage - HOT engineering (2024)
- 💡 Special core analysis - HOT engineering (2024)
- 💡 Reservoir simulation in Tnavigator (Advanced level) - tips and tricks (2022) 
- 💡 Petroleum Engineering Certification (PEC) - Ministry of Mining and Energy of Serbia (2023) 
- 💡 Chemical Methods for Enhanced Oil Recovery with Eclipse (2021)
"""
)
# --- AWARDS ---
st.write('\n')
st.subheader("Awards")
st.write("---")
st.write(
    """
- ⭐ Serbian State Scholarships (2015, 2016, and 2017) 
- ⭐ Russian Government Scholarship (2017)
- ⭐ Scholarship from company NIS Gazprom Neft, program Energy of knowledge (2018-2020) 

"""
)
