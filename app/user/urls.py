"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),

    path(
        'create-gapi-view/',
        views.CreateUserApiView.as_view(),
        name='create_gapi_view'
    ),

    path('token/', views.CreateTokenView.as_view(), name='token'),

    path('me/', views.ManageUserView.as_view(), name='me'),

    path(
        'me-api-view/',
        views.ManageUserApiView.as_view(),
        name='me_api_view'
    ),

    path('list-users', views.ListAllUsersApiView.as_view(), name='all_users')
]
