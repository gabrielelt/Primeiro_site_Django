from django.contrib import admin
from cards.models import Card

class listando_cards(admin.ModelAdmin):
    list_display = ('id', 'nome_do_card', 'resposta_correta', 'publicada')
    list_display_links = ('id', 'nome_do_card')
    search_fields = ('nome_do_card',)
    list_filter = ('classe_do_card',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Card, listando_cards)
