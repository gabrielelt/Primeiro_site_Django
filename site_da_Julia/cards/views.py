from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Card
from django.contrib.auth.decorators import login_required

@login_required
def cards(request):
    usuario_logado = request.user
    if request.method == "GET":
        dados = Card.objects.order_by('-id').filter(publicada=True).all
        return render(request, 'cards/cards.html', {'cards': dados})
    else:
        nome_do_card = request.POST.get('nome_do_card')
        card = get_object_or_404(Card, nome_do_card=nome_do_card)
        resposta = request.POST.get('resposta') 

        if resposta == card.resposta_correta:
            usuario_logado.cards_respondidos.add(card, through_defaults={'acertou': True})
            usuario_logado.save()
            return HttpResponse(usuario_logado.aluno_card.all())
        else:
            usuario_logado.cards_respondidos.add(card=card, through_defaults={'acertou': False})
            usuario_logado.save()
            return HttpResponse(usuario_logado.aluno_card.all())
    # Path: site_da_julia/cards/urls.py