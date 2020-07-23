from django.shortcuts import render, HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')

index = IndexView.as_view()
