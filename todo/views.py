from django.shortcuts import render

# Create your views here.
def registeruser(request):
  return render(request, 'todo/registeruser.html')
