from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Card

def cards(request):
    if request.method == "GET":
        dados = Card.objects.order_by('-id').filter(publicada=True).all
        return render(request, 'cards/cards.html', {'cards': dados})
    else:
        nome_do_card = request.POST.get('nome_do_card')
        card = get_object_or_404(Card, nome_do_card=nome_do_card)
        resposta = request.POST.get('resposta') 

        if resposta == card.resposta_correta:
            return HttpResponse(' é a resposta correta!')
        else:
            return HttpResponse(' é a resposta errada!')
    # Path: site_da_julia/cards/urls.py