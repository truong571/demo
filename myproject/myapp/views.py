from django.shortcuts import render

# Create your views here.

def my_view(request):
    context = {}
    return render(request, 'my_template.html', context)