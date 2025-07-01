from http import client
import re
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings

# Create your views here.
client=OpenAI(api_key=settings.OPENAI_API_KEY)

def chat_view(request):
    if request.method=='POST':
        user_message=request.POST.get('message','')
        response=client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role":"system", "content":"You are a helpful assistant."},
                {"role":"user", "content":user_message},
            ],
            max_tokens=150
        )
        ai_message=response.choices[0].message.content
        
        return JsonResponse({'message': ai_message})
    return render(request, 'chat/chat.html')
    
