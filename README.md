# 📄 AI Resume Analyzer

An AI-powered resume analysis web application built with **Python and Streamlit**.

The application allows users to upload **PDF or DOCX resumes** and automatically extracts, cleans, and analyzes their content to identify skills, resume sections, and areas for improvement.

## 🚀 Features

- 📤 Upload PDF and DOCX resumes
- 📄 Extract resume text automatically
- 🧹 Clean and preprocess resume content
- 🛠️ Detect technical skills
- 📑 Detect important resume sections
- 📊 Calculate a resume score
- 💡 Generate personalized resume recommendations
- 🔄 Supports different resume formats and resumes
- 🖥️ Interactive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- pdfplumber
- python-docx
- Regular Expressions (Regex)

## 📊 Resume Analysis

The application analyzes:

### 📑 Resume Sections
- Professional Summary
- Education
- Experience
- Internships
- Projects
- Technical Skills
- Certifications
- Languages

### 🛠️ Skills
- Programming
- Artificial Intelligence
- Machine Learning
- Generative AI
- Data Analysis
- Exploratory Data Analysis (EDA)
- Development & Cloud Tools

## 📈 Resume Scoring

The application evaluates the uploaded resume based on:

- Number of relevant skills
- Important resume sections
- Technical skill coverage
- Overall resume completeness

It then provides a **resume score out of 100** along with recommendations for improvement.

## 💡 Recommendations

The application can provide suggestions such as:

- Add more relevant technical skills
- Add a GitHub profile
- Add relevant project repositories
- Improve the professional summary
- Add missing resume sections

## 🚀 Live Demo

👉 **[Open AI Resume Analyzer]**[YOUR_STREAMLIT_APP_URL](/(https://ai-resume-analyzer-kjums7n379vunqk.streamlit.app/)/)

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_pdf.py
