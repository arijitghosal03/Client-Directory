from django import forms
from .models import CustomerModel

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = [
            'customer_name', 'customer_category', 'website_link', 'socialmedia_link',
            'description', 'phone_number', 'email', 'file_upload'
        ]
