from .views import RegisterAPI
from django.urls import path

from knox import views as knox_views
from .views import LoginAPI
from accounts import views
from django.urls import include, re_path
urlpatterns = [
    # get post delete
    re_path(r'^api/profile$', views.profile_list),

    #get put
    re_path(r'^api/profile/(?P<pk>[0-9]+)$', views.profile_detail),


    #register
    path('api/register/', RegisterAPI.as_view(), name='register'),

    #login
    path('api/login/', LoginAPI.as_view(), name='login'),
    
    #logout
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/profiles',views.profile_list),
]