from django.shortcuts import render, redirect
from django.contrib import messages
from add_project.models import Project
from add_project.utils import check_password

def register_project(request):
    if request.method == "POST":
        password = request.POST['password']
        if not password:
            messages.error(request, 'Escribe la contraseña')
            return redirect('register')
    
        if check_password(password):
            try:
                new_project = Project.objects.create(
                    name=request.POST['name'],
                    image=request.FILES.get('image'),
                    github=request.POST['github'],
                    deploy=request.POST['deploy'],
                    devchallenges=request.POST['devchallenges']
                )
                new_project.save()
                return redirect('gallery')
            except:
                messages.error(request, 'No se pudo registrar')
                return redirect('register')
            
        messages.error(request, 'Contraseña incorrecta')    
        return redirect('register')
    
    return render(request, 'register-form.html')