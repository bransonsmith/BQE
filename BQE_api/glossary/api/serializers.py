from django.db.models import fields
from rest_framework import serializers
from ..models import *

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'name']

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'word', 'book', 'chapter', 'verse']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Answer
        fields = ['id','question_id', 'book', 'chapter', 'verse']

