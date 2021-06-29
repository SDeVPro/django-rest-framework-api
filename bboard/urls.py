from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import APIRubricViewSet,APIRubricViewSetRO, api_rubrics,api_rubric_detail, APIRubrics, APIRubric, APIRubricDetail
router = DefaultRouter()
router.register('rubricssss',APIRubricViewSet)

urlpatterns = [
    path('rubrics/', api_rubrics),
    path('rubrics/<int:pk>',api_rubric_detail),
    path('rubricss/',APIRubrics.as_view()),
    path('rubricsss/<int:pk>',APIRubricDetail.as_view()),
    path('rubricsss/',APIRubric.as_view()),
    path('',include(router.urls)),

    

]