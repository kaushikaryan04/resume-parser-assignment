from rest_framework import serializers
from .models import Candidate

class CandidateSerialize(serializers.ModelSerializer) :
    class Meta :
        model = Candidate
        fields = ['first_name','email','phone_number']
