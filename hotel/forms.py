from django import forms

#if  room is available book straight away,otherwise redirect to other section

class AvailabilityForm(forms.Form):
    
    check_in=forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M" ,])
    check_out=forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M" ,])