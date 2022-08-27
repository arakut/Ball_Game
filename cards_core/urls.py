from django.urls import path
from cards_core.views import ListObjectsView, DetailObectView
urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('<int:pk>', DetailObectView.as_view(), name='detail'),
]
