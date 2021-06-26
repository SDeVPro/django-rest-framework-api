from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Rubric
from .serializers import RubricSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET','POST'])
def api_rubrics(request):
    if request.method == 'GET':
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics,many=True)
        return  Response(serializer.data)
    elif request.method=='POST':
        serializer = RubricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','PATCH','DELETE'])
def api_rubric_detail(request,pk):
    rubric = Rubric.objects.get(pk=pk)
    if request.method=='GET':
        serializer = RubricSerializer(rubric)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method=='PATCH':
        serializer = RubricSerializer(rubric,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        rubric.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def api_rubrics(request):
#     if request.method=='GET':
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return Response(serializer.data)
# @api_view(['GET'])
# def api_rubric_detail(request,pk):
#     if request.method=='GET':
#         rubric = Rubric.objects.get(pk=pk)
#         serializer = RubricSerializer(rubric)
#         return Response(serializer.data)
# def api_rubric(request):
#     if request.method=='GET':
#         rubrics = Rubric.objects.all()
#         serializer = RubricSerializer(rubrics, many=True)
#         return JsonResponse(serializer.data,safe=False)
