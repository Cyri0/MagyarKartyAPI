from django.shortcuts import render
from django.http import JsonResponse
from .models import Card, Deck

def base(request):
    return JsonResponse(
            {
                '/':'open this page',
                'cards/':'get all card types',
                'getcard/<id>/':'return specific card by id',
                'getnewdeck/':'create a new, fully filled deck for a game and return the id',
                'getdeck/<id>/':'return specific deck by id'
            }
        )

def getcards(request):
    data = {'cards':[]}
    cards = Card.objects.all()
    for card in cards:
        data['cards'].append(card.serialize())
    return JsonResponse(data)

def getcard(reques, id):
    card = Card.objects.get(id = id)
    return JsonResponse(card.serialize())

def getdeck(request, id):
    try:
        return JsonResponse(Deck.objects.get(id=id).serialize())
    except Deck.DoesNotExist:
        return JsonResponse({'result':'Deck does not exist!'})

def getnewdeck(request):
    newdeck = Deck()
    newdeck.save()
    newdeck.cards.set(Card.objects.all())
    newdeck.save()
    return JsonResponse(
        {
            'result':'deck created',
            'deck_id': newdeck.id
        })

