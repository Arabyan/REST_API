from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.

from .models import Update

# def detaiL_view(request):
    # return render(request, template, {}) # render JSon data --> JS object Notation
    # return HttpResponse(get_template().render({}))

def update_model_detaiL_view(request):
    data = {
        "count": 1000,
        "content":"Some new content"
    }
    return JsonResponse(data)