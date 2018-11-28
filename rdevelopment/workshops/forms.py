"""Post forms."""

# Django
from django import forms

# Models
from workshops.models import Workshop




class PostForm(forms.ModelForm):
    """Post model form."""

    class Meta:
        """Form settings."""

        model = Workshop
        fields = ('user', 'profile', 'title','description', 'txt')
