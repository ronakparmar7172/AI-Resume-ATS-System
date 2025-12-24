AI Resume ATS Analyzer

I built this project to understand how resume screening systems (ATS) work and to help job seekers see why their resume gets shortlisted or rejected.
The system compares a resume with a job description, calculates an ATS score, shows missing skills, and gives clear suggestions on how the resume can be improved.

What this project actually does :
Takes one or more resumes as input
Takes a job description from the user
Checks how closely the resume matches the job
Calculates an ATS score
Shows which skills match and which are missing
Suggests how the resume can be improved
Displays everything in a clean dashboard
This is similar to how real companies filter resumes before a human sees them.

Why I created this :
Many candidates apply for jobs but never hear back, even with good resumes.
One major reason is ATS filtering.

I created this project to:
Learn real ATS logic
Practice AI and NLP concepts
Help users improve their resumes
build a practical, real-world project using Django and BERT

Key features :
Resume upload (PDF, DOCX, TXT)
Job description input
Meaning-based comparison using BERT
Skill matching and skill gap detection
ATS score calculation
Resume ranking
Resume improvement suggestions
Full-screen and user-friendly UI
How the ATS score works (simple explanation) 


The ATS score is based on two things:

Meaning match (70%)
Checks how similar the resume content is to the job description using AI.
Skill match (30%)
Checks how many required job skills appear in the resume.
Both are combined to give a final score.


Technologies used :

Python
Django
Natural Language Processing (NLP)
BERT (Sentence Transformers)
Scikit-learn
NLTK
HTML and CSS
SQLite
Git and GitHub

Project structure :

resume_ats/
├── manage.py
├── requirements.txt
├── resume_ats/
├── ats_app/
│   └── utils/
├── templates/
└── static/

How to run this project :

Clone the repository
git clone https://github.com/ronakparmar7172/AI-Resume-ATS-System.git
Go to the project folder
cd AI-Resume-ATS-System
Install required packages
pip install -r requirements.txt
Start the server
python manage.py runserver
Open the browser and go to
http://127.0.0.1:8000/


How to use it :

Upload resume files
Paste the job description
Click on Analyze Resume
View ATS score, missing skills, and suggestions


It is built for learning, practice, and improvement.

If you find it useful, feel free to star the repository ⭐
