from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about', views.about),
    path('', views.homepage),
    path('event/', views.read_events, name='read_events'),
    path('event/create/', views.create_events, name='create_events'),
    path('event/update/<int:event_id>/', views.update_events, name='update_events'),
    path('event/delete/<int:event_id>', views.delete_events, name='delete_events'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)