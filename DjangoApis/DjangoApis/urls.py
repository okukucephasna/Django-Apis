from django.urls import path
from myapp import views

urlpatterns = [
    path('api/data/', views.get_data, name='get_data'),
    path('api/data/create/', views.create_data, name='create_data'),
    path('api/data/update/<int:id>/', views.update_data, name='update_data'),
    path('api/data/delete/<int:id>/', views.delete_data, name='delete_data'),
]
