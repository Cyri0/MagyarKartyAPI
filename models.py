from django.db import models
import uuid

COLORS = [
    ('PIROS','piros'),
    ('TÖK','tök'),
    ('ZÖLD','zöld'),
    ('MAKK','makk'),
]

NAMES = [
    ('7','VII'),
    ('8','VIII'),
    ('9','IX'),
    ('10','X'),
    ('ALSO','also'),
    ('FELSO','felso'),
    ('KIRALY','kiraly'),
    ('ASZ','asz')
]

class Card(models.Model):
    name = models.CharField(max_length=6,
    choices = NAMES)
    color = models.CharField(
        max_length=5,
        choices=COLORS)
    image = models.TextField( default = '-')
    code = models.CharField(max_length=4, default='-')

    def __str__(self):
        return self.color + ' ' + self.name

    def save(self, *args, **kwargs):
        self.code=self.color[0] + self.name[0]
        super(Card, self).save(*args, **kwargs)

    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'img':self.image,
            'color':self.color,
            'code': self.code
        }
    
class Deck(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    cards = models.ManyToManyField(Card)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'pakli'+str(self.id)

    def serialize(self):
        result = []

        for card in self.cards.all():
            result.append(card.serialize())

        return {
            'id':self.id,
            'cards':result,
            'created':self.created
        }