from django.shortcuts import render
from .functions import create_user, create_password


def layout(request):
    return render(request,'layout.html')

def user(request):
    return render(request,'user.html')

def password(request):
    return render(request,'password.html')

def information(request):
    return render(request,'information.html')

def result(request):
    craft = None
    title = ''
    
    if request.method == 'POST':
        source_view = request.POST.get('source_view')
        
        if source_view == 'uss':
            name = request.POST.get('name')
            hobby = request.POST.get('hobby')
            birthdate = request.POST.get('fecha')

            craft = create_user(name, birthdate, hobby)
            title = 'USER CREATED'
        else:
            length = int(request.POST.get('length'))  
            capitalLetters = 'capitalLetters' in request.POST
            specialCharacters = 'specialCharacters' in request.POST
            numbers = 'numbers' in request.POST
            
            craft = create_password(length, capitalLetters=capitalLetters, specialCharacters=specialCharacters, numbers=numbers)
            title = 'PASSWORD CREATED'

    return render(request, 'result.html', {
        'title': title,
        'craft': craft
    })
