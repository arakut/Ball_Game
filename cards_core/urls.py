from django.urls import path
from cards_core.views import ListObjectsView, DetailObectView, PlaygroundCreateView
urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('<int:pk>', DetailObectView.as_view(), name='detail'),
    path('create/', PlaygroundCreateView.as_view(), name='create_pg'),
]
