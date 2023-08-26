from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.

def display_topic(request):
    QSTO = Topic.objects.all()
    d={'TO':QSTO}
    return render(request,'display_topic.html',d)


def dispaly_webpage(request):
    QSWO = webpage.objects.all()
    QSWO = webpage.objects.order_by('topic_name')

    QSWO = webpage.objects.order_by('-name')

    QSWO = webpage.objects.order_by(Length('name'))

    QSWO = webpage.objects.all().order_by(Length('name').desc())
    d={'QSWO':QSWO}
    return render(request,'dispaly_webpage.html',d)


def dispaly_Access(request):
    QSAO = AccessRecord.objects.all()

    QSAO = AccessRecord.objects.exclude(author='VK')
    d={'QSAO':QSAO}
    return render(request,'dispaly_Access.html',d)