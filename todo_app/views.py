from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from . models import Todo
from .serializers import TodoSerializer
from rest_framework import status

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
    
    def post(self,request,format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self,request,todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
            serializer = TodoSerializer(todo)
            return Response(data=serializer.data)
        except:
            return Response({'message':"Todo with given id doesnot exists"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        serializer = TodoSerializer(todo,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        serializer = TodoSerializer(todo,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,todo_id):
        todo = Todo.objects.get(id = todo_id)
        todo.delete()
        return Response({'message':"Todo deleted successfully"},status=status.HTTP_200_OK)