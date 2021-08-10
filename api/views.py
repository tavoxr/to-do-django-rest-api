from api.models import Task
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, TaskCreateSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls ={
        'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
    }    

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
def taskDetail(request, id):

    
    try:
        task = Task.objects.get(id = id)
        print('task', task)
        serializer = TaskSerializer(task)

        return Response(serializer.data, status = status.HTTP_200_OK)
    except :
        return Response('Task doesn\'t exist')

@api_view(['POST'])
def taskCreate(request):

    name = request.data['name']
    print('request.data', name )
    try:
        serializer = TaskCreateSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()    
        
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    except:
            
        
        return Response('Data not vald')

@api_view(['PUT'])
def taskUpdate(request, id):

    try:
        task = Task.objects.get(id = id)
        serializer = TaskCreateSerializer(data = request.data, instance = task )

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status = status.HTTP_200_OK)
        
    except:
        return Response('Data not valid')



@api_view(['DELETE'])
def taskDelete(request, id):

    try:
        task = Task.objects.get(id = id)
        task.delete()
    
        return Response('Task Deleted')
    
    except:
        return Response('Error, task coudn\'t be deleted')





