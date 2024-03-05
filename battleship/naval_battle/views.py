from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from naval_battle.serializer import UserRegistrationSerializer
from django.contrib.auth.models import User

# Create your views here.
@api_view(['POST'])
def user_create(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
