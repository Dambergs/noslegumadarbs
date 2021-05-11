from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

# demo function_based view
from django.views import View


def demo_function_based_view(request):
    random_integer = randint(0,10)
    if request.method == 'GET':
        response=render(
            request=request,
            template_name='demo_fbv.html',
            context={
                'random_integer' : random_integer,
            },
        )
    else:
        response = HttpResponse('Incoming request')

    return response


class DemoView(View):
    def get(self, request):
        random_integer = randint(0, 10)
        return render(
            request=request,
            template_name='demo_cbv.html',
            context={
                'random_integer' : random_integer,
            },
        )

    def post(self, request):
        pass