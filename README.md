# 📄 AI Resume Analyzer

An AI-powered resume analysis web application built using Python and Streamlit. The application allows users to upload PDF or DOCX resumes and automatically extract, clean, and analyze their content.

It identifies important resume sections, detects technical skills, calculates a resume score, and provides recommendations to help improve the resume.

## 🚀 Live Demo

👉 **[Open AI Resume Analyzer](https://ai-resume-analyzer-kjums7n379vunqk.streamlit.app/)**

## 📌 Project Overview

Finding important information in a resume manually can be time-consuming. This project provides an interactive solution that analyzes resumes automatically.

Users can upload their resume in **PDF or DOCX format**, and the application processes the document to identify skills, sections, and areas that can be improved.

## ✨ Features

- 📄 Upload PDF and DOCX resumes
- 📝 Extract text from uploaded resumes
- 🧹 Clean and preprocess extracted text
- 🛠️ Identify technical skills
- 📑 Detect important resume sections
- 📊 Calculate an overall resume score
- 💡 Generate personalized resume recommendations
- 🔄 Support analysis of different resumes
- 🖥️ Interactive Streamlit interface
- 📥 Download processed resume information

## 🔍 Resume Analysis

The application analyzes the following sections:

- Professional Summary
- Education
- Experience
- Internships
- Projects
- Technical Skills
- Certifications
- Languages

### 🛠️ Skills Detection

Skills are categorized into areas such as:

**Programming**
- Python
- C

**AI & Machine Learning**
- Artificial Intelligence
- Machine Learning
- Machine Learning Algorithms
- Generative AI
- Scikit-learn

**Data & Analytics**
- Data Analysis
- Data Analytics
- Exploratory Data Analysis
- Pandas
- Matplotlib
- Power BI
- SQL

**Tools & Deployment**
- Git
- GitHub

The skill detection system can be extended by adding additional skills and categories.

## 📊 Resume Scoring

The application calculates a resume score based on factors such as:

- Important resume sections
- Technical skills
- Overall resume content

The score helps users understand the completeness of their resume and identify areas for improvement.

## 💡 Recommendations

Based on the analysis, the application can provide suggestions such as:

- Add a professional summary
- Add more relevant technical skills
- Include project details
- Add GitHub or portfolio links
- Improve missing resume sections

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **pdfplumber**
- **python-docx**
- **Regular Expressions (Regex)**

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
├── test_pdf.py
├── requirements.txt
├── README.md
└── .gitignore
