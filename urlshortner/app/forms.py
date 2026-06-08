from django import forms
from .models import ShortURL

class URLForm(forms.ModelForm):
    short_code = forms.CharField(required=False,empty_value=None)
    class Meta:
        model = ShortURL

        fields = [
            "original_url",
            "expires_at",
            "short_code"
        ]

    #called automatically
    def clean_short_code(self):
        code = self.cleaned_data.get("short_code")

        if code and ShortURL.objects.filter(short_code=code).exists():

            raise forms.ValidationError(
                "This short code is already taken."
            )
        if not code:
            return None
        return code