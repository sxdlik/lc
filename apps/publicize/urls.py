from django.urls import path

from .import views

app_name = 'publicize'

urlpatterns = [
    path('', views.index, name='publicize-index'),
    path('flow_detail/<int:pk>/', views.flow_detail, name='publicize-flow-detail'),
]
