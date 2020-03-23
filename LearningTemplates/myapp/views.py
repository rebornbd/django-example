from django.shortcuts import render

# Create your views here.

def home(request):
    my_dict = {'main_text': 'I love my country.'}
    return render(request, 'myapp/home.html', my_dict)

