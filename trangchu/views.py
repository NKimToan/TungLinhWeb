from django.shortcuts import render

# Create your views here.
def get_trangchu(request):
    return render(request,'index.html')