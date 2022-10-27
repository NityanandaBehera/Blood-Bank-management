from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Home, name='home'),
    path('donor', DonorView, name='donor'),
    path('login', Login, name='login'),
    path('register', register, name='register'),
    path('logout', Logout, name='logout'),
    path('camping', Camping, name='camping'),
    path('details/<str:pk>', Details, name='details'),
    path('donor-list', DonorList, name='donor-list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
