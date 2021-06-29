from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from .models import Rubric
from .serializers import RubricSerializer
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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


class APIRubrics(APIView):
    def get(self,request):
        rubrics = Rubric.objects.all()
        serializer = RubricSerializer(rubrics,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = RubricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class APIRubric(generics.ListCreateAPIView):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
class APIRubricDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer


class APIRubricViewSet(ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
    permission_classes = (IsAuthenticated,)

class APIRubricViewSetRO(ReadOnlyModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer

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
