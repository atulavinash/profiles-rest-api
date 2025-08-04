from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
