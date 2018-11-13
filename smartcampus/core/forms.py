from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter your email address'}))
    feedback = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Provide your feedback here'}))

    def clean_name(self):
        """ Sanitize the name field """
        name_data = self.cleaned_data['name']

        return name_data

    def clean_email(self):
        """ Sanitize the email field """
        email_data = self.cleaned_data['email']

        return email_data

    def clean_feedback(self):
        """ Sanitize the feedback field """
        feedback_data = self.cleaned_data['feedback']

        return feedback_data

