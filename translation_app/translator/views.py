from django.http import JsonResponse
from transformers import pipeline
from django.shortcuts import render
def translate(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        translator = pipeline("translation", model='E:/FPTU/OJT/self-project/translation_app/translator/last_8_epoch')
        translated_text = translator(text)
        res = translated_text[0]['translation_text']
        return JsonResponse({'translated_text': res}, status=200)
    return render(request, 'index.html')
