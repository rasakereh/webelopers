from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


def index(request):
    return HttpResponse("Salaam, donya!")

def homepage_view(request):
    return render(request, 'staticpages/homepage.html')
'''	
def about_view(request):
    return render(request, 'staticpages/about.html')
'''

class about_view(TemplateView):
	template_name = "staticpages/about.html";

