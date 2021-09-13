from django.urls import path
from .views import ClientListAndCreate, ClientDetailChangeAndDelete


urlpatterns = [
    path('', ClientListAndCreate.as_view()),
    path('<int:pk>/', ClientDetailChangeAndDelete.as_view()),
]
