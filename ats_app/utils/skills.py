# ats_app/utils/skills.py

# ==============================
# MASTER TECHNOLOGY SKILLS LIST
# ==============================

SKILLS = [

    # Programming Languages
    "python", "java", "c++", "c#", "javascript", "typescript",
    "go", "kotlin", "swift", "ruby", "php",

    # Java Technologies
    "core java", "advanced java", "jdbc", "servlet", "jsp",
    "spring", "spring boot", "spring mvc", "hibernate", "jpa",
    "maven", "gradle",

    # .NET Technologies
    ".net", ".net core", ".net framework", "asp.net", "asp.net mvc",
    "asp.net core", "web api", "ado.net", "entity framework",
    "linq", "wpf", "winforms", "blazor",

    # Python Frameworks
    "django", "flask", "fastapi",

    # Web Technologies
    "html", "html5", "css", "css3", "bootstrap", "tailwind",
    "javascript dom", "ajax", "json",

    # Frontend Frameworks
    "react", "react js", "angular", "vue js", "next js",

    # Backend / APIs
    "node.js", "express.js", "rest api", "graphql", "microservices",

    # Databases
    "mysql", "postgresql", "sqlite", "oracle", "sql server",
    "mongodb", "redis", "firebase", "sql",

    # AI / ML
    "artificial intelligence", "machine learning", "deep learning",
    "nlp", "natural language processing", "computer vision",
    "data science",

    # ML / AI Libraries
    "scikit-learn", "tensorflow", "keras", "pytorch",
    "nltk", "spacy", "huggingface", "bert", "sentence transformers",

    # Data Analysis
    "pandas", "numpy", "matplotlib", "seaborn",

    # Cloud & DevOps
    "aws", "azure", "google cloud", "docker", "kubernetes",
    "linux", "git", "github",

    # Software Engineering
    "oops", "data structures", "algorithms",
    "design patterns", "mvc", "mvvm", "agile"
]

# ==============================
# SKILL EXTRACTION LOGIC
# ==============================

def extract_skills(text: str):
    """
    Extract skills found in given text
    """
    text = text.lower()
    found = set()

    for skill in SKILLS:
        if skill in text:
            found.add(skill)

    return found


def skill_analysis(resume_text: str, jd_text: str):
    """
    Compare resume skills with JD skills
    """
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills

    ratio = len(matched) / len(jd_skills) if jd_skills else 0

    return ratio, list(matched), list(missing)
