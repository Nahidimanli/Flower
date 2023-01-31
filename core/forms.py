from django import forms
from core.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'d-flex mt-4', 'placeholder' : 'Name' }),
            'email': forms.EmailInput(attrs={'class':'d-flex mt-4','placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'd-flex mt-4', 'placeholder': 'Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'd-flex mt-4', 'placeholder': 'Message'})

            
            }