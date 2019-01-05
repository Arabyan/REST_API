import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

from grgapi.mixins import JsonResponseMixin

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

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }

        # return JsonResponse(data)
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }

        return self.render_to_json_response(data)