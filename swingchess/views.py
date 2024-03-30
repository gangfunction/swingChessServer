from django.http import JsonResponse
from django.http import HttpResponse


def log_message(request):
    if request.method == "POST":
        log_message_directed = request.POST.get("log_message")
        print(f"Log message: {log_message_directed}")
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})


def hello_django(request):
    return HttpResponse("Hello")
