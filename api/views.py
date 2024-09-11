from django.http.response import JsonResponse
from django.shortcuts import render
import re
from pymupdf.mupdf import FzIrect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import tempfile
import os
import fitz
from .serializers import CandidateSerialize


def extract_info_from_text(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    phone_pattern = r'\b(?:\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}\b'
    name_pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

    name = re.findall(name_pattern , text)
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    return name , emails, phones

def extract_text_from_pdf(pdf_path) :
    text = ''
    with fitz.open(pdf_path) as doc :
        for page in doc :
            text += page.get_text()
    return text



@api_view(['POST'])
def UploadView(request) :
    pdf_file = request.FILES.get('resume')
    data = []
    with tempfile.TemporaryDirectory() as temp_dir :
        file_path = os.path.join(temp_dir , pdf_file.name )
        with open(file_path, 'wb') as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)
        text = extract_text_from_pdf(file_path)
        name , email , phone = extract_info_from_text(text)
        first_name = name[0].split(" ")[0]
        data.append(name[0])
        data.append(email[0])
        data.append(phone[0])

    response = {"first_name" : first_name , "email" : data[1] , "phone_number" : data[2]}
    candidate_serializer = CandidateSerialize(data = response )
    if candidate_serializer.is_valid() :
        candidate_serializer.save()
        return JsonResponse(response)
    else :
        return Response(candidate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
