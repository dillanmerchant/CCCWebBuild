from django import forms

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length = 12)
    company = forms.CharField(max_length = 50)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)
    force_field = forms.CharField(required = False, widget = forms.HiddenInput, label = "Leave Empty", validators=[should_be_empty])