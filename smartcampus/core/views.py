from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
import sendgrid
import os
from sendgrid.helpers.mail import *
from .models import *


def home(request):
    """
    GET request for the home page.
    Returns the last metric values from the Data table.
    """
    posts = [Data.objects.latest('id')]
    cont = {'posts': posts}
    return render(request, 'home.html', cont)


def select_location(request):
    """
    GET request to the location page
    Returns metrics in the chart displays.
    """
    dataset = Data.objects.all()
    posts = [dataset.latest('id')]

    temps = []
    hums = []
    press = []
    gass = []
    year = 2018
    month = 7
    day = 26
    hour = 4
    minutes = 00

    for i in range(6):
        temps.append(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                          .filter(dt__hour=hour).filter(dt__minute=minutes).first().temp)
        hums.append(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                          .filter(dt__hour=hour).filter(dt__minute=minutes).first().hum)
        press.append(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                          .filter(dt__hour=hour).filter(dt__minute=minutes).first().pres)
        gass.append(round(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                          .filter(dt__hour=hour).filter(dt__minute=minutes).first().gas / 2000000))
        minutes += 10

    return render(request, 'select_location.html', {'posts': posts, 'temps': json.dumps(temps, cls=DjangoJSONEncoder),
                                                    'hums': json.dumps(hums, cls=DjangoJSONEncoder),
                                                    'press': json.dumps(press, cls=DjangoJSONEncoder),
                                                    'gass': json.dumps(gass, cls=DjangoJSONEncoder)})


def campus_report(request):
    """
    GET request for the campus reports page.
    """
    return render(request, 'campus_report.html')


def report_2018_07_28(request):
    """
    GET request for the reports page.
    """
    # daily report only
    # 2018-07-28 00:00 to 2018-07-28 20:59
    dataset = Data.objects.all()
    temps = []
    hums = []
    press = []
    gass = []
    year = 2018
    month = 7
    day = 28
    hour = 00
    minutes = 00

    for h in range(24):
        try:
            temps.append(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                                       .filter(dt__hour=hour).filter(dt__minute=minutes).first().temp)
        except AttributeError:
            temps.append('NA')

        try:
            hums.append(model_to_dict(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                                      .filter(dt__hour=hour).filter(dt__minute=minutes).first())['hum'])
        except AttributeError:
            hums.append('NA')

        try:
            press.append(model_to_dict(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                                       .filter(dt__hour=hour).filter(dt__minute=minutes).first())['pres'])
        except AttributeError:
            press.append('NA')

        try:
            gass.append(round(model_to_dict(dataset.filter(dt__year=year).filter(dt__month=month).filter(dt__day=day)
                                      .filter(dt__hour=hour).filter(dt__minute=minutes).first())['gas'] / 2000000))
        except AttributeError:
            gass.append('NA')

        hour += 1

    times = ['00:00','01:00','02:00','03:00','04:00','05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
             '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    temp_a = [i for i in temps if i != 'NA']
    hum_a = [i for i in hums if i != 'NA']
    pres_a = [i for i in press if i != 'NA']
    gas_a = [i for i in gass if i != 'NA']
    average = [round(sum(temp_a) / len(temp_a), 2), round(sum(hum_a) / len(hum_a), 2),
               round(sum(pres_a) / len(pres_a), 2), sum(gas_a) / len(gas_a)]
    return render(request, 'report_2018_07_28.html', {'times': times, 'temps': temps, 'hums': hums, 'press': press,
                                                      'gass': gass, 'average': average})


def feedback(request):
    """
    GET request returns the form on the feedback page.
    POST request sends an email.
    """

    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        print(feedback_form)
        if feedback_form.is_valid():
            feedback_instance = Feedback()
            feedback_instance.name = feedback_form.cleaned_data['name']
            feedback_instance.email = feedback_form.cleaned_data['email']
            feedback_instance.feedback = feedback_form.cleaned_data['feedback']
            feedback_instance.save()
            print(feedback_instance.name)
            print(feedback_instance.email)
            print(feedback_instance.feedback)

            # === Sendgrid email ===
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email('vporta7@gmail.com')
            to_email = Email("vporta7@yahoo.com")
            subject = "Feedback"
            content = Content("text/plain", "Name: {} \nEmail: {} Feedback: {}".format(feedback_form.cleaned_data['name'],
                                                                             feedback_form.cleaned_data['email'],
                                                                             feedback_form.cleaned_data['feedback']))
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)
            return HttpResponseRedirect('/')
    else:
        feedback_form = FeedbackForm()
        context = {
            'form': feedback_form,
        }
        return render(request, 'feedback.html', context)




