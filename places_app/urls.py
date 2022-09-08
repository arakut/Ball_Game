from django.urls import path
from . import views


urlpatterns = [
    path('', views.PlaceListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name='detail'),
    path('place/<int:pk>/update/', views.PlaceUpdateView.as_view(), name='update'),
    path('place/<int:pk>/delete/', views.PlaceDeleteView.as_view(), name='delete'),
    path('place/new', views.PlaceCreateView.as_view(), name='new_place'),
    # path('about/', views.about, name='blog-about'),
]
