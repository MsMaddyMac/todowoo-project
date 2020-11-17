from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.
def registeruser(request):
  if request.method == 'GET':
    # to use Django generated form, create import first
    # render form in registeruser.html
    return render(request, 'todo/registeruser.html', {'form':UserCreationForm()})
  else:
    # import User model which is autogenerated with Django magic
    # invoke the User() with built in methods and pass in the request info from the form by referencing the keys of each input to be used.
    # If password1 is equal to password2 create new user
    if request.POST['password1'] == request.POST['password2']:
      try:
          # Create a new user
        user = User.objects.create_user(request.POST['username'], request.POST['password1'])
          #  Save new user in database
        user.save()
      except IntegrityError:
        return render(request, 'todo/registeruser.html', {'form':UserCreationForm(), 'error':'Username is already taken. Please choose a new one!'})
    else:
      return render(request, 'todo/registeruser.html', {'form':UserCreationForm(), 'error':'Passwords did not match!'})
