from django.shortcuts import render

appname = "clientes"
def index(request):
    return render(request, "index_cliete.html")
