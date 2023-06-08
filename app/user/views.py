"""
Views for the user API
"""
from rest_framework import mixins, generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    ListUserSerializer,
    )


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateUserApiView(generics.GenericAPIView, mixins.CreateModelMixin):
    """Create a new user in the system. Same as above, but explicit."""

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class ManageUserApiView(APIView):
    """APIView version of generic classes"""

    serializer_class = UserSerializer

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # For Swagger documentation
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self):
        assert self.serializer_class is not None, (
            "'%s' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
            % self.__class__.__name__
        )

        return self.serializer_class

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
    # For Swagger documentation

    def get(self, request, *args, **kwargs):
        return Response(UserSerializer(self.request.user).data)

    def put(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            self.request.user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            self.request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ListAllUsersApiView(APIView):

    def get(self, request, *args, **kwargs):

        queryset = get_user_model().objects.all()

        serializer = ListUserSerializer(queryset, many=True)

        return Response(serializer.data)
