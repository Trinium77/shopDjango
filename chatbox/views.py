from django.shortcuts import render
from django.http import JsonResponse
from .models import FAQ

def chatbot(request):
    if request.method == "POST":
        user_question = request.POST.get('question', '').lower()

        # Recherche la question dans la FAQ
        faqs = FAQ.objects.all()
        response = None
        
        for faq in faqs:
            if user_question in faq.question.lower():
                response = faq.answer
                break

        if not response:
            response = "Désolé, je n'ai pas la réponse à cette question."

        return JsonResponse({"response": response})
    
    return render(request, 'chatbox/chatbot.html')
