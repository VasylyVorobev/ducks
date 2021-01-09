from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_url'),
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='detail_item_url'),
    path('create-item/', views.CreateItemView.as_view(), name='create_item_url'),
    path('update/<int:pk>/', views.UpdateItemView.as_view(), name='update_item_url'),

]
