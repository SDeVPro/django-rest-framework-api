
from django.urls import path
from .views import api_rubrics,api_rubric_detail
urlpatterns = [
    path('rubrics/', api_rubrics),
    path('rubrics/<int:pk>',api_rubric_detail),
]