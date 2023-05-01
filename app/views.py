from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'displaytopics.html',d)


def webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'displaywebpage.html',d)

def access(request):
    LOA=AccessRecord.objects.all()
    d={'access':LOA}
    return render(request,'displayaccess.html',d)


def updatewebpage(request):
    Webpage.objects.filter(name='dhoni').update(email='MSD@gmail.com')
    Webpage.objects.filter(name='zehra').update(email='zehra@gmail.in')
    TO=Topic.objects.get_or_create(topic_name='cricket')[0]
    TO.save()
    Webpage.objects.update_or_create(name='gunes',defaults={'topic_name'=TO,'url':'http://gunes.com','email':'gunes@gmail.com'})



    d={'webpage':Webpage.objects.all()}
    return HttpResponse('update webpage data successfully')

    return render(request,'displaywebpage.html',d)

def deletewebpage(request):
    Webpage.objects.filter(topic_name='cricket').delete()

    d={'webpage':Webpage.objects.all()}
    return HttpResponse('Data deleted successfully')
    return render(request,'displaywebpage.html',d)