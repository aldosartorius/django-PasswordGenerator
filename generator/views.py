from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = " "     #Variable for store de password

    characters = list('abcdefghijklmnopkrstuvwxyz') #list of all lowercase letters


    #If uppercase is selected all uppercase letteres are added to characters
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    #If special characters is selected all special characters are added to characters
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+'))

    #If number is selected all numbers are added to characters
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length')) #Get from form the length of the password and typecast to int

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
