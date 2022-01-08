from django import forms


from .models import ocr


class ImageUpload(forms.ModelForm):
    class Meta:
        model = ocr
        fields = ['image']
