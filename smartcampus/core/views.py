from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FeedbackForm
import sendgrid
import os
from sendgrid.helpers.mail import *


def home(request):
    """ GET request for the homepage that renders latest metrics data. """
    # data = Data.objects.filter(dt__lte='2018-01-01')
    # print(data)
    posts = [Data.objects.latest('id')]
    cont = {'posts': posts}
    return render(request, 'home.html', cont)


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
    """ GET request for the campus reports page. """
    return render(request, 'campus_report.html')


def feedback(request):
    """ GET and POST requests for the feedback.html page. """

    if request.method == 'POST':
        feedback_instance = get_object_or_404(Feedback)
        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():
            feedback_instance.name = feedback_form.cleaned_data['name']
            feedback_instance.email = feedback_form.cleaned_data['email']
            feedback_instance.feedback = feedback_form.cleaned_data['feedback']
            feedback_instance.save()

            # === Sendgrid email ===
            # sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            # from_email = Email(feedback_form.cleaned_data['email'])
            # to_email = Email("vporta7@gmail.com")
            # subject = "Feedback"
            # content = Content("text/plain", "Name: {} \nFeedback: {}".format(feedback_form.cleaned_data['name'], feedback_form.cleaned_data['feedback']))
            # mail = Mail(from_email, subject, to_email, content)
            # response = sg.client.mail.send.post(request_body=mail.get())
            # print(response.status_code)
            # print(response.body)
            # print(response.headers)
            return HttpResponseRedirect(reverse('/'))

    feedback_form = FeedbackForm()

    context = {
        'form': feedback_form,
    }
    return render(request, 'feedback.html', context)




