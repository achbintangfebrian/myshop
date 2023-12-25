from django.http import HttpResponse
from django.template import loader

def beranda(request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())