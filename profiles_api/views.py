from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self,request,format = None):

        """ returns a list of APIViews"""

        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to Django view',
            'gives you the most control over your applicaton logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message': 'Hello', 'an_apiview' : an_apiview})
