from django.forms import ModelForm
from .models import Review

class ReviewPost(ModelForm):

    class Meta:
        fields = ('name', 'email', 'text')
        model = Review
