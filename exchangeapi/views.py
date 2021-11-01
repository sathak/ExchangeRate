from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExchangeInfo
from .serializer import ExchangeInfoSerializer

@api_view(['GET', 'POST'])
def exchange_list(request):
    """
    List all exchange list, or create a new exchange list.
    """
    if request.method == 'GET':
        snippets = ExchangeInfo.objects.all()
        serializer = ExchangeInfoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExchangeInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
