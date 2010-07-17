from django import forms
from servee.contrib.media.document.models import Document

class DocumentUpload(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)