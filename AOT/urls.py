from django.urls import path 
from .views import AOTListView,AOTDetailView
urlpatterns = [
    path('',AOTListView.as_view(),name='AOT_list'),
    path('<int:pk>',AOTDetailView.as_view(),name='AOT_detail')
]