from django import forms

SHIFTS=(
    ('1','Morning'),
    ('2','Afternoon'),
    ('3','Evening'),
)

class InputForm(forms.Form):
    firs_name=forms.CharField(max_length=200, required=False)
    last_name=forms.CharField(max_length=200, required=False)
    shift=forms.ChoiceField(choices=SHIFTS, required=False)
    time_log=forms.TimeField(required=False)