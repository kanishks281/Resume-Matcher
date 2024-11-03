# Resume Matcher

A web application built with Python, Flask, and Scikit-learn that matches job descriptions with resumes using Word2Vec embeddings. This system provides an efficient and user-friendly interface for recruiters to upload job descriptions and resumes, processing them to identify the top candidates based on semantic similarity.

## Features

- **Automated Text Extraction**: Supports text extraction from PDF, DOCX, and TXT resume formats.
- **Word2Vec-based Matching**: Utilizes pre-trained Word2Vec embeddings to perform semantic matching between job descriptions and resumes.
- **Real-time Similarity Scoring**: Displays similarity scores for top-matching candidates in real-time.
- **Responsive UI**: User-friendly and responsive interface designed with Bootstrap for seamless recruiter interactions.

## Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Word2Vec (from Gensim library)
- **Frontend**: HTML, CSS, Bootstrap
- **Text Extraction**: docx2txt, PyPDF2

## Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kanishks281/Resume-Matcher.git
   cd job-resume-matching-system
   ```

2. **Install dependencies**:
   Install the necessary Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Example `requirements.txt` file:
   ```
   Flask
   gensim
   scikit-learn
   docx2txt
   PyPDF2
   numpy
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

1. **Home Page**: Start by navigating to the home page where you can enter a job description and upload resumes.

2. **Job Description and Resumes Upload**:
   - Input the job description in the provided text box.
   - Upload multiple resumes in PDF, DOCX, or TXT formats (up to 50 resumes per session).

3. **Get Top Matching Resumes**:
   - The system will compute the similarity scores for the uploaded resumes and display the top-matching candidates based on semantic similarity.

## Project Structure

```
job-resume-matching-system/
│
├── app.py                    # Main application file
├── templates/
│   └── matchresume.html      # HTML template for the UI
├── uploads/                  # Directory for uploaded resumes
└── requirements.txt          # Python dependencies
```



