from django.shortcuts import render
from .models import feedbackData,courseData

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def feedback(request):
    if request.method=='GET':
        return render(request, 'feedback.html')
    else:
            feedbackData(name=request.POST.get('name'),
                        rating=request.POST.get('rating'),
                        feedback=request.POST.get('feedback')).save()
            form=feedbackData.objects.all()
            return render(request, 'feedback.html',{'form':form})

def services(request):
    cd=courseData.objects.all()
    return render(request,'services.html',{'cd':cd})
    
def galary(request):
    return render(request, 'galary.html')

