from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of API View features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to traditional django view',
            'Gives you the most control over your application logic',
            'Is Mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
