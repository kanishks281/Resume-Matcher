from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import gensim.downloader as api  # Gensim for pre-trained word embedding model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load pre-trained Word2Vec model (Google News)
word2vec_model = api.load('word2vec-google-news-300')

# Extract text from different file formats
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

# Function to get the average word embedding for a text document
def get_average_word_embedding(text, model):
    words = text.split()  # Simple tokenization, could be improved
    word_vectors = [model[word] for word in words if word in model]
    if word_vectors:
        return np.mean(word_vectors, axis=0)  # Average of word vectors
    else:
        return np.zeros(300)  # Return a zero vector if no words are found

@app.route("/")
def matchresume():
    return render_template('matchresume.html')

@app.route('/matcher', methods=['POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_files = request.files.getlist('resumes')

        resumes = []
        resume_texts = []
        for resume_file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            resume_text = extract_text(filename)
            resumes.append(resume_text)
            resume_texts.append(resume_text)

        if not resumes or not job_description:
            return render_template('matchresume.html', message="Please upload resumes and enter a job description.")

        # Compute embeddings for job description and resumes
        job_desc_embedding = get_average_word_embedding(job_description, word2vec_model)
        resume_embeddings = [get_average_word_embedding(resume_text, word2vec_model) for resume_text in resumes]

        # Calculate cosine similarities between job description and resumes
        similarities = [cosine_similarity([job_desc_embedding], [resume_embedding])[0][0] for resume_embedding in resume_embeddings]

        # Get top 5 resumes and their similarity scores
        top_indices = np.argsort(similarities)[-5:][::-1]
        top_resumes = [resume_files[i].filename for i in top_indices]
        similarity_scores = [round(similarities[i], 2) for i in top_indices]

        return render_template('matchresume.html', message="Top matching resumes:", top_resumes=top_resumes, similarity_scores=similarity_scores)

    return render_template('matchresume.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
