import re

from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
from django.template import loader
from rest_framework.decorators import api_view

from .models import Users, Students


def signup_page(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())


def signin_page(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())


@api_view(['POST'])
def create_user(request):
    user_name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']

    if not re.match(r"(^([^\s@]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,})$)", email):
        return HttpResponse("<h2>Please Enter Valid Email</h2>")
    if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return HttpResponse(
            "<h2>Password should be minimum 8 character</h2>")
    if Users.objects.values("id").filter(email=email):
        return HttpResponse("<h2>User already exists. Please sign in with your credentials</h2>")

    instance = Users.objects.create(name=user_name, email=email, password=password)
    template = loader.get_template('signin.html')

    return HttpResponse(template.render())


@api_view(["POST"])
def signin_user(request):
    email = request.data["email"]
    password = request.data['password']
    if not re.match(r"(^([^\s@]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,})$)", email):
        return HttpResponse("<h2>Please Enter valid Email</h2>")
    if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        return HttpResponse("<h2>Password should be minimum 8 character</h2>")
    data = Users.objects.filter(Q(email=email) & Q(password=password))
    if not data:
        return HttpResponse("<h2>Invalid credential</h2>")
    template = loader.get_template('studentform.html')

    return HttpResponse(template.render())


@api_view(["POST"])
def student_form(request):
    name = request.data["name"]
    enroll = request.data['enroll']
    if isinstance(enroll, str):
        return HttpResponse("<h2>Please Enter the Numeric value in Enrollment number</h2>")
    gender = request.data['gender']
    hobbies = request.data['hobbies']
    city = request.data['city']
    state = request.data['state']
    country = request.data['country']
    instance = Students.objects.create(name=name, Enrollment_number=enroll, gender=gender, hobbies=hobbies, city=city,
                                       state=state, country=country)
    template = loader.get_template('display.html')
    data = Students.objects.all()
    response = {
        "data": list(data)
    }
    return HttpResponse(template.render(response))
