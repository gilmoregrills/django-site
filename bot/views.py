from django.shortcuts import render
from django.utils import timezone
from .models import Message
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def message_history(request):
   messages = Message.objects.filter(sent_date__lte=timezone.now()).order_by('-sent_date')
   return render(request, 'bot/message_history.html', {'messages' : messages})
