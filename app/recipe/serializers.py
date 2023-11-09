"""
Serializers for recipe APIs
"""
from email.mime import image
from rest_framework import serializers

from core.models import Breed, Dog, Answer



class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = [
            'id', 'name']
        read_only_fields = ['id']


class DogSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Dog
        fields = [
            'id', 'name','breed']
        read_only_fields = ['id']


class AnswerSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Answer
        fields = [
            'totalBreeds', 'totalDogs','commonBreed', 'commonDogName']
        read_only_fields = ['id']


    def create(self, validated_data):

        answer = Answer.objects.create(**validated_data)

        return answer
