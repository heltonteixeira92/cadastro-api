from api_project.cadastro.models import CadastroCli
from api_project.cadastro.serializers import CadastroSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny


class ClientList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request):
        cliente = CadastroCli.objects.all()
        seralizer = CadastroSerializer(cliente, many=True)
        return Response(seralizer.data)


class ClientDetail(APIView):
    def get(self, request, pk):
        cliente = CadastroCli.objects.get(pk=pk)
        seralizer = CadastroSerializer(cliente, many=False)
        return Response(seralizer.data)


class ClientCreate(APIView):
    def post(self, request):
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientUpdate(APIView):
    def put(self, request, pk):
        cliente = CadastroCli.objects.get(pk=pk)
        serializer = CadastroSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDelete(APIView):
    def delete(self, request, pk):
        cliente = CadastroCli.objects.get(pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
