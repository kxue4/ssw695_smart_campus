from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json


def home(request):
    # data = Data.objects.filter(dt__lte='2018-01-01')
    # print(data)
    posts = [Data.objects.latest('id')]
    cont = {'posts': posts}
    return render(request, 'home.html',cont)


def select_location(request):
    dataset = Data.objects.all()
    posts = [dataset.latest('id')]
    zeros = model_to_dict(dataset.get(id=911))
    tens = model_to_dict(dataset.get(id=921))
    twenties = model_to_dict(dataset.get(id=931))
    thirties = model_to_dict(dataset.get(id=941))
    forties = model_to_dict(dataset.get(id=951))
    fifties = model_to_dict(dataset.get(id=961))
    temps = [zeros['temp'], tens['temp'], twenties['temp'], thirties['temp'], forties['temp'], fifties['temp']]
    hums = [zeros['hum'], tens['hum'], twenties['hum'], thirties['hum'], forties['hum'], fifties['hum']]
    press = [zeros['pres'], tens['pres'], twenties['pres'], thirties['pres'], forties['pres'], fifties['pres']]
    gass = [zeros['gas']/1000000, tens['gas']/1000000, twenties['gas']/1000000, thirties['gas']/1000000, forties['gas']/1000000, fifties['gas']/1000000]
    return render(request, 'select_location.html', {'posts': posts, 'temps': json.dumps(temps, cls=DjangoJSONEncoder),
                                                    'hums': json.dumps(hums, cls=DjangoJSONEncoder),
                                                    'press': json.dumps(press, cls=DjangoJSONEncoder),
                                                    'gass': json.dumps(gass, cls=DjangoJSONEncoder)})


def campus_report(request):
    return render(request, 'campus_report.html')


def feedback(request):
    return render(request, 'feedback.html')