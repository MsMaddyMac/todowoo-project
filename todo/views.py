from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def registeruser(request):
  # to use Django generated form, create import first
  # render form in registeruser.html
  return render(request, 'todo/registeruser.html', {'form':UserCreationForm()})
