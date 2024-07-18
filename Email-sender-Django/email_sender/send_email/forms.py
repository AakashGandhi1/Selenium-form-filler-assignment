from django import forms

class EmailForm(forms.Form):
    to = forms.EmailField(label='To')
    cc = forms.EmailField(label='CC', required=False)
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    attachment1 = forms.FileField(required=False)
    attachment2 = forms.FileField(required=False)
  
