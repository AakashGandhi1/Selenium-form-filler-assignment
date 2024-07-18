from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import EmailForm
# Create your views here.


def send_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            to = form.cleaned_data['to']
            cc = form.cleaned_data['cc']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            email = EmailMessage(
                subject,
                body,
                'aakashgandhi622@gmail.com',
                [to],
                cc=[cc] if cc else None
            )
            for f in ['attachment1', 'attachment2']:
                if form.cleaned_data[f]:
                    email.attach(form.cleaned_data[f].name, form.cleaned_data[f].read(), form.cleaned_data[f].content_type)
            email.send()
            return render(request, 'send_email/success.html')
    else:
        form = EmailForm()
    return render(request, 'send_email/send_email.html', {'form': form})