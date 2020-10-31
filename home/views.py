from django.shortcuts import render, redirect
from home.forms import RegisterForm
from django.contrib import messages
from home.backEnd import FaceRecognition
from home.models import UserProfile
from django.shortcuts import HttpResponse

facerecognition = FaceRecognition()

def home(request):
    return render(request, 'home/home.html')

def register(request):

    if request.POST:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully Registerd!')
            addFace(request.POST['face_id'])
            return redirect('/')
        else:
            messages.error(request, "Account Register Failed!")

    form = RegisterForm()
    context = {
        'title' : 'Register Form',
        'form' : form
    }
    return render(request, 'home/register.html', context)

def addFace(face_id):
    face_id = face_id
    facerecognition.faceDetect(face_id)
    facerecognition.trainFace()
    return redirect('/')

def logine(request):
    return render(request, 'home/password.html')


def login(request):
    face_id = facerecognition.recognizeFace()
    return redirect('/home/welcome/'+ str(face_id))

def welcome(request, face_id):
    face_id = int(face_id)
    print(face_id)
    # data = {
    #     'user': UserProfile.objects.get(face_id= face_id)
    # }

    return render(request, 'home/sevagen.html')