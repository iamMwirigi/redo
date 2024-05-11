from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    return render(request, 'base/room.html')

def server(request):
    return render(request, 'base/server.html') 