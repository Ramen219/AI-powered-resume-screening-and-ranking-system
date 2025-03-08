# AI-Powered Resume Screening & Ranking System

## Introduction
The **AI-Powered Resume Screening & Ranking System** is a web-based application that automates the process of screening and ranking resumes based on relevance to a specified job role. 
This system leverages **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques to extract key details from resumes and rank candidates efficiently. 
It aims to reduce the manual workload of recruiters and ensure a fair and unbiased selection process.

## Features
- **Automated Resume Parsing**: Extracts candidate details such as name, email, phone number, skills, and experience.
- **AI-Based Resume Ranking**: Uses NLP to evaluate and rank resumes based on job relevance.
- **Batch Resume Upload**: Supports multiple file uploads for processing multiple resumes at once.
- **User-Friendly Interface**: Built with React.js for a smooth and interactive experience.
- **Fast & Scalable**: The Flask-based backend ensures quick processing and seamless scalability.
- **Custom Job Role Input**: Allows users to specify job roles for ranking resumes accordingly.
- **Dark Theme UI**: Aesthetic design for better user experience.

## How It Works
1. **Upload Resumes**: Users upload resumes in **PDF format**.
2. **Enter Job Role**: Specify the desired job role for ranking.
3. **Resume Processing**: The system extracts information from resumes using **NLP-based text parsing**.
4. **Relevance Scoring**: Each resume is analyzed and assigned a **score** based on its relevance to the job role.
5. **Display Ranked Resumes**: The ranked list is displayed in a table, showing details such as file name, email, phone number, and ranking score.

## Tech Stack & Tools Used
- **Frontend**: React.js, HTML, CSS, Tailwind CSS
- **Backend**: Flask (Python)
- **AI & NLP**: sklearn, TfidfVectorizer, TF-IDF (Term Frequency - Inverse Document Frequency)
- **PDF(file) Processing**: PyMuPDF (fitz), PyPDF, docx2txt
- **Data Handling**: Pandas, NumPy
- **Deployment**: Flask for backend, React for frontend, Docker (optional)

## Installation & Running the Project
### Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.8)
- Node.js & npm
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/ai-resume-screening.git
cd ai-resume-screening
```

### Step 2: Backend Setup (Flask API)
```bash
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate virtual environment (For Windows: venv\Scripts\activate)
pip install -r requirements.txt  # Install dependencies
python app.py  # Run Flask server
```
The backend will start running at `http://127.0.0.1:5000/`

### Step 3: Frontend Setup (React)
```bash
cd frontend
npm install  # Install dependencies
npm start  # Run frontend
```
The frontend will start at `http://localhost:3000/`

## Future Enhancements
- Improve ranking accuracy using **Deep Learning models**.
- Add **support for multiple job roles** at once.
- Integrate with **HR management systems**.
- Enable **email notifications for shortlisted candidates**.
- Deploy the system using **Docker & Cloud Services**.

## Conclusion
This project demonstrates the power of **AI in recruitment**, providing a scalable, fast, and objective method for screening and ranking resumes. 
By automating the process, it reduces recruiter workload and ensures a **fair hiring process**.

## License
This project is open-source
