from django.shortcuts import render
from .utils.text import extract_text, clean_text
from .utils.embeddings import semantic_similarity
from .utils.skills import skill_analysis
from .utils.scoring import final_score, improvement_tips

def index(request):
    results = []

    if request.method == "POST":
        jd = clean_text(request.POST['job_description'])

        for r in request.FILES.getlist('resumes'):
            resume = clean_text(extract_text(r))

            semantic = semantic_similarity(resume, jd)
            ratio, matched, missing = skill_analysis(resume, jd)
            score = final_score(semantic, ratio)

            results.append({
                "name": r.name,
                "score": score,
                "semantic": round(semantic*100, 2),
                "skills": round(ratio*100, 2),
                "matched": matched,
                "missing": missing,
                "tips": improvement_tips(missing)
            })

        results.sort(key=lambda x: x['score'], reverse=True)

    return render(request, 'index.html', {'results': results})
