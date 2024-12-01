from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def hallo(request):
    return render(request, 'class_template.html')

class Hallo(TemplateView):
    template_name =('second_task/func_template.html')
