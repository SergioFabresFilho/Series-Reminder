from django.urls import path

from series import views


app_name = 'series'

urlpatterns = [
    path('create_series/', views.create_series, name='create_series'),
    path('list_series/', views.list_series, name='list_series'),
    path('<int:series_id>/delete_series/', views.delete_series, name='delete_series'),
    path('<int:series_id>/update_series', views.update_series, name='update_series'),
]
