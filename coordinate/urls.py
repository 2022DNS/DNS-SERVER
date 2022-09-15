from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('coordinate/', views.RoadListAPIView.as_view()),
    path('coordinate/lo/<str:pk>/la/<str:post_pk>', views.RoadDetailAPIView.as_view()),
    path('coordinate/create', views.RoadCreateAPIView.as_view())
]