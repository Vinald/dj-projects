from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello/helloworld.html', {'title': 'Hello World'})


def greet(request, name: str):
    return render(request, 'hello/greet.html', {'name': name, 'title': 'Greet'})
