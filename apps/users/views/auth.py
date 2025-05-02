from rest_framework.views import APIView
from rest_framework.response import Response

class AuthView(APIView):
    def post(self, request):
        # Lógica de autenticación aquí (ej: login con JWT)
        return Response({"message": "Auth endpoint works!"})