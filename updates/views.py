from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

from .models import Update

# def detaiL_view(request):
    # return render(request, template, {}) # render JSon data --> JS object Notation
    # return HttpResponse(get_template().render({}))

def json_example_view(request):
    """
    URI - for a REST API
    GET - Retrive
    """
    data = {
        "count": 1000,
        "content":"Some new content"
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')