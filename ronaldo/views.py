from django.shortcuts import render, redirect
from .models import About_1, Education_1, Experience_1, Skill_1, Awards_1, Project_1, Counter_1
from .forms import ContactForm


def index(request):
        objects = About_1.objects.all()
        education_1 = Education_1.objects.all()
        experience_1 = Experience_1.objects.all()
        skill_1 = Skill_1.objects.all()
        awards_1 = Awards_1.objects.all()
        project_1 = Project_1.objects.all()
        counter_1 = Counter_1.objects.all()
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('.')

        context = {
        'objects': objects,
        'education_1': education_1,
        'experience_1': experience_1,
        'skill_1': skill_1,
        'awards_1': awards_1,
        'project_1': project_1,
        'counter_1': counter_1,
        'form': form
        }        
        return render (request, 'index.html', context)









