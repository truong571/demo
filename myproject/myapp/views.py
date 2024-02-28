from django.http import HttpResponse
from django.template import loader
# Create your views here.

def my_view(request):
  template = loader.get_template('my_template.html')
  return HttpResponse(template.render())