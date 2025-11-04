from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def health(request):
    return JsonResponse({"status": "ok", "service": "medichek-server"})


@api_view(['POST'])
def receive_data(request):
    """Receive JSON data from client."""
    data = request.data
    
    # Process the received data here
    # For now, just echo it back with a success message
    return Response({
        "status": "success",
        "message": "Data received successfully",
        "received_data": data
    })
