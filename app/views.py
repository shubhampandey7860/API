from django.shortcuts import render
from app.serializers import *
from django.http import JsonResponse
from django.http import *


from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/course-list/',
        'Detail View':'course-detail/<str:pk>',
        'Create':'/course-create/',
        'Update':'course-update/<str:pk>',
        'Delete':'/course-delete/<str:pk>'
    } 
    return Response(api_urls)

@api_view(['GET'])   
def CourseList(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course,many=True)
    return Response(serializer.data) 
 
@api_view(['GET'])   
def CourseDetail(request,pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(course,many=False)
    return Response(serializer.data) 


@api_view(['POST'])
def CourseCreate(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    
      

@api_view(['POST'])
def CourseUpdate(request,pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(instance=course,data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)    

@api_view(['Delete'])
def CourseDelete(request,pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return Response("item successfully deleted")    

      
