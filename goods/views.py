from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'goods/mainpage.html')

def company(request):
    return render(request, 'goods/company_info.html')