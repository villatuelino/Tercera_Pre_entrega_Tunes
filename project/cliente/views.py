from django.shortcuts import render

appname = "cliente"
def index(request):
    return render(request, "index_cliente.html")
