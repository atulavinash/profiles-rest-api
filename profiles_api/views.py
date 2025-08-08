from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test Api View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format = None):

        """ returns a list of APIViews"""

        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to Django view',
            'gives you the most control over your applicaton logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})

    def post(self,request):
        """ Create a hello message with our name"""

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'messgae': message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST

            )

    def put(self,request, pk= None):
        """Handle update and object """

        return Response({'method': 'PUT'})

    def patch(self,request,pk = None):
        """ handle partial update of an object"""

        return Response({'method': "PATCH"})

    def delete(self, request, pk = None):
        """ Delete an object """

        return Response({'method' : 'delete'})


class HelloViewSet(viewsets.ViewSet):

    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """ return a Hello message"""

        a_viewset = [
            "uses actions (list,create,retreive,update,partial_update,delete)",
            "Automatically maps to URLs using routers",
            "Provides more functionality with less code",

        ]
        return Response({"message": 'Helloview', "a_viewset" : a_viewset})

    def create(self,request):
        """Create a new Hello message"""

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message': message})

        else:

            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST

            )

    def retrieve(self,request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method' : 'GET'})

    def update(self,request,pk = None):
        """handle update an object"""

        return Response({'http_method' : 'PUT'})

    def partial_update(self,request, pk = None):
        """handle Partial update of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self,request,pk = None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email",)
