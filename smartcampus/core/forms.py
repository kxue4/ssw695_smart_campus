from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(help_text="Enter a name.")
    email = forms.EmailField(help_text="Enter a and email.")
    feedback = forms.CharField(help_text="Provide some feedback.")

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

