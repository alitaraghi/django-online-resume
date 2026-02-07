from django.shortcuts import render
from datetime import datetime
from .models import Skill, Project


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()

    # دسته‌بندی اسکیل‌ها برای نمایش
    skills_by_category = {
        "Programming": skills.filter(category="programming"),
        "Web": skills.filter(category="web"),
        "Frameworks & Tools": skills.filter(category="frameworks_tools"),
        "Other": skills.filter(category="other"),
    }

    context = {
        "name": "Ali Taraghikon",
        "title": "Python Developer | Interested in Web Development and AI",
        "current_year": datetime.now().year,
        "skills_by_category": skills_by_category,
        "projects": projects,
    }
    return render(request, "portfolio/home.html", context)
