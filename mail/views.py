from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SubscribeForm
from subscribe.settings import EMAIL_HOST_USER

# Create your views here.
# def index(request):
#     return render(request,)
def Subscribe(request):
    sub = SubscribeForm()
    if request.method == 'POST':
        sub = SubscribeForm(request.POST)
        subject = 'Welcome to MySite'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['email'].value())
        send_mail(subject,
                  message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form': sub})
