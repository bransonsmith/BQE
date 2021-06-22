from django.db.models import query
from rest_framework import routers, serializers, viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .serializers import *
from ..models import *
import random
class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all() 
    
    @action(detail=False, methods=['GET'], name='Random')
    def random(self, request):
        random_word_id = random.choice(list(self.queryset)).id
        random_word = Word.objects.filter(id=random_word_id).first()
        serializer = self.get_serializer(random_word)
        return Response(serializer.data)
class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()