from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'content/index.html')

def projects(request):
    return render(request, 'content/projects.html')

def references(request):
    return render(request, 'content/references.html')