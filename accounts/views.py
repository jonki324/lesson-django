from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/index.html', {'msg': 'templete'})

index = IndexView.as_view()
