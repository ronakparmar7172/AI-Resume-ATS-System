def final_score(semantic, skill_ratio):
    return round((semantic * 0.7 + skill_ratio * 0.3) * 100, 2)

def improvement_tips(missing_skills):
    tips = []
    for s in missing_skills:
        tips.append(f"Add experience or projects related to '{s}'")
    return tips
