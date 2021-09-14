from django.urls import path
from .views import ClientList, ClientDetail, ClientCreate, ClientUpdate, ClientDelete


urlpatterns = [
    path('',ClientList.as_view()),
    path('detail/<int:pk>/',ClientDetail.as_view(),name='detail'),
    path('create',ClientCreate.as_view(),name='create'),
    path('update/<int:pk>/',ClientUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',ClientDelete.as_view(),name='delete'),
]
