from api_project.cadastro.models import CadastroCli
from api_project.cadastro.serializers import CadastroSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny


class ClientListAndCreate(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request):
        cliente = CadastroCli.objects.all()
        seralizer = CadastroSerializer(cliente, many=True)
        return Response(seralizer.data)

    def post(self, request):
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailChangeAndDelete(APIView):

    def get_object(self, pk):
        try:
            return CadastroCli.objects.get(pk=pk)
        except CadastroCli.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        cliente = self.get_object(pk)
        serializer = CadastroSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, pk):
        cliente = self.get_object(pk)
        serializer = CadastroSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
