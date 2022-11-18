from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupview(request):
    if request.method == 'POST':
        username_data = request.POST.get('username_data')
        password_data = request.POST.get('password_data')
    
        try:
            User.objects.create_user(username_data , '' , password_data)
        except IntegrityError :
            return render(request, 'signup.html', {'error':'このユーザはすでに登録されています。'})

    else:
        print(User.objects.all())
    return render(request, 'signup.html', {})
