from django.urls import path
from cards_core.views import ListObjectsView
urlpatterns = [
    path('', ListObjectsView.as_view(), name='card'),
]
