from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("<h1>Hello World!</h1>")


def today_view(request):
    import datetime
    today = datetime.date.today()
    context = {
        'today': today
    }
    return render(request, 'today.html', context)


def home_view(request):
    return render(request, 'home.html')


def talabalar_view(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar
    }
    return render(request, 'talabalar.html', context)


def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_details.html', context)


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'mualliflar.html', context)


def muallif_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    kitoblar = Kitob.objects.filter(muallif=muallif)
    context = {
        'muallif': muallif,
        'kitoblar': kitoblar
    }
    return render(request, 'muallif_details.html', context)


def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'kitoblar_view.html', context)


def top3_kitoblar_view(request):
    kitoblar = Kitob.objects.order_by('-sahifa')[:3]
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'top3-kitoblar.html', context)


def recordlar_view(request):
    recordlar = Record.objects.all()
    context = {
        'record': recordlar
    }
    return render(request, 'recordlar_view.html', context)













