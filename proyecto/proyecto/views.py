from django.shortcuts import render 


def inicio(request):
    template_name = "index.html"
""""
def login(request):
    print(request.method == "GET")

    print("entre a login")
    print(request.POST.get("pass", None))
    return render(request, "login.html", {})
"""