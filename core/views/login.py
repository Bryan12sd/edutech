from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response

def login_view(request):
    return render(request, 'login.html')


@api_view(['POST'])
def login_api(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(username=username, password=password)

    if user:
        return Response({
            "message": "Login exitoso",
            "user_id": user.id,
            "username": user.username
        })

    return Response({"error": "Credenciales incorrectas"})
