from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        import json
        mail = request.POST['mail']
        msg = request.POST["comment"]
        print(mail, msg)
    return render(request, 'feedbck/index.html')
