from django import forms
from .models import ShortURL

class URLForm(forms.ModelForm):

    custom_code = forms.CharField(
        required=False
    )

    class Meta:
        model = ShortURL

        fields = [
            "original_url",
            "expires_at"
        ]