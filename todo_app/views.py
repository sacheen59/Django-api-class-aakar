from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import Todo
from .serializers import TodoSerializer

# Create your views here.

# json => javascript object notation
@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return Response({'message':"hello we are learning django rest framework"})
    elif request.method == 'POST':
        pass

# class based views 
class IndexView(APIView):
    def get(self,request):
        # This function returns a response with a message saying "hello we are learning django rest framework"
        return Response({'message':"hello we are learning django rest framework"})
    
    def post(self,request):
        pass

class TodoView(APIView):
    def get(self,request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo,many=True)
        return Response(data=serializer.data)