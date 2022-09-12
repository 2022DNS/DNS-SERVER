from django.urls import path
from . import views



urlpatterns = [
    path('coordinate/', views.RoadListAPIView.as_view()),
    path('coordinate/<int:pk>/', views.RoadDetailAPIView.as_view()),
    path('coordinate/create', views.RoadCreateAPIView.as_view())
]