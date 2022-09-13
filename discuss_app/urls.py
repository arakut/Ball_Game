from django.urls import path
from . import views

urlpatterns = [
    path('', views.DiscussListView.as_view(), name='discuss-list'),
    path('<int:pk>/', views.DiscussDetailView.as_view(), name='detail-discuss'),
    path('<int:pk>/delete/', views.DiscussDeleteView.as_view(), name='delete-discuss'),
    path('/<int:pk>/', views.AddTextDiscuss.as_view(), name='add_text_discuss'),
    path('new/', views.CreateDiscuss.as_view(), name='create-discuss'),
]