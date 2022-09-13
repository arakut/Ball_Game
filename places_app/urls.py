from django.urls import path
from . import views


urlpatterns = [
    path('', views.PlaceListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contact'),
    path('place/<int:pk>/', views.PlaceDetailView.as_view(), name='detail'),
    path('place/<int:pk>/update/', views.PlaceUpdateView.as_view(), name='update'),
    path('place/<int:pk>/delete/', views.PlaceDeleteView.as_view(), name='delete'),
    path('place/new', views.PlaceCreateView.as_view(), name='new_place'),
    path('search/', views.SearchPlacesView.as_view(), name='search'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
]
