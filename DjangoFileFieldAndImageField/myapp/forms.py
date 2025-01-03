from django import forms
from .models import Document, Photo

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']