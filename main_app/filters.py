import django_filters
from django import forms

from django_filters import CharFilter

from main_app.models import Receiver_Request


class BloodFilter(django_filters.FilterSet):
    blood_groups =CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={

        'placeholder':'search blood group', 'class':'form-control'}))
    class Meta:
        model =Receiver_Request
        fields =('blood_groups',)