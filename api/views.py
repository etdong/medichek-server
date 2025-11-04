from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def health(request):
    return JsonResponse({"status": "ok", "service": "medichek-server"})


@csrf_exempt
def receive_json(request):
    """Receive JSON payload via POST and return an acknowledgement.

    - Accepts: POST with a JSON body (Content-Type: application/json), OPTIONS for CORS preflight
    - Returns: 201 with the parsed payload echoed under `received` on success
    - Errors: 400 for invalid JSON, 405 for non-POST/OPTIONS methods
    """
    if request.method == "OPTIONS":
        # Handle CORS preflight request
        response = JsonResponse({})
        response["Allow"] = "POST, OPTIONS"
        return response
    
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    try:
        # request.body is bytes; decode and parse JSON
        body = request.body.decode("utf-8") if request.body else ""
        data = json.loads(body) if body else {}
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    # TODO: add validation or processing here. For now echo back the payload.
    return JsonResponse({"received": data}, status=201)
