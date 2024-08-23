from django.shortcuts import render,redirect
from django.views import View
from .models import SigninModel,Course,StudentLogin
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
class IndexView(View):
    def get(self,r):
        return render(r,template_name='home/index.html')
class SigninView(View):
    def get(self,r):
        return render(r,template_name='home/signin.html')
class Signin(View):
    def post(self,r):
        email=r.POST.get('email')
        username=r.POST.get('username')
        pas=r.POST.get('password')
        cpas=r.POST.get('cpassword')
        s1=SigninModel.objects.filter(email=email)
        if s1.exists():
            return render(r,'home/login.html',{'s1':s1})
        else:
            SigninModel.objects.create(email=email,username=username,pas=pas,cpas=cpas)
            return render(r,template_name='home/signin.html')
class LoginView(View):
    def get(self,r):
        return render(r,template_name='home/login.html')
class Login(View):
    def post(self, r):
        user = r.POST.get('username')
        password = r.POST.get('password')  
        try:
            user = SigninModel.objects.get(username=user, pas=password)
            return redirect('home')
        except SigninModel.DoesNotExist:
            return render(r, 'home/login.html', {'error': "Invalid email or password"})

class ForgetView(View):
    def get(self,r):
        return render(r,template_name='home/forget.html')
class Forget(View):
    def post(self,r):
        email=r.POST.get('email')
        try:
            s2=SigninModel.objects.get(email=email)
            subject='WELCOME TO OUPG COLLEGE'
            msg=str(s2.pas)
            email_from=settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]
            send_mail(subject, msg, email_from, recipient_list)
            return render(r, 'home/login.html', {'success': "Password has been sent to your email."})
        except SigninModel.DoesNotExist:
            return render(r,'home/forget.html',{'fail': "Enter valid Email"})
class Home(View):
    def get(self,r):
        return render(r,template_name='main/home.html')
    
class CourseView(View):
    def get(self,r):
        c1=Course.objects.all()
        return render(r,'main/course.html',{'c1':c1})

class Faculty(View):
    def get(self,r):
        return render(r,template_name='main/faculty.html')
class About(View):
    def get(self,r):
        return render(r,template_name='main/about.html')
#student App
class StudentLoginView(View):
    def get(self,r):
        return render(r,template_name='student/login.html')
class StudentLoginV2(View):
    def post(self,r):
        roll=r.POST.get("roll_number")
        dob=r.POST.get("dob")
        s4=StudentLogin(s_roll=roll,s_dob=dob)
        if s4:
            return render(r,template_name='student/shome.html')
        else:
            return HttpResponse("Please Enter Valid Detials")
class Shome(View):
    def get(self,r):
        return render(r,template_name='student/shome.html')
class Timetable(View):
    def get(self,r):
        return render(r,template_name='student/timetable.html')
class Library(View):
    def get(self,r):
        return render(r,template_name='student/library.html')
class ExamResult(View):
    def get(self,r):
        return render(r,template_name='student/examresult.html')