from ..models import *
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from ..serializers import *
import random
from rest_framework.permissions import AllowAny

class WordViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    queryset = Word.objects.all() 
    
    @action(detail=False, methods=['GET'], name='Random')
    def random(self, request):
        random_word_id = random.choice(list(self.queryset)).id
        random_word = Word.objects.filter(id=random_word_id).first()
        serializer = self.get_serializer(random_word)
        return Response(serializer.data)
        
    @action(detail=False, methods=['POST'], name='Answer') 
    @permission_classes([AllowAny])
    def answer(self,  request):
        question_id = request.data['question_id']
        book = request.data['book']
        chapter= request.data['chapter']
        verse= request.data['verse']

        answer = {'question_id': question_id, 'book': book, 'chapter': chapter, 'verse' : verse}
        return Response(answer)
