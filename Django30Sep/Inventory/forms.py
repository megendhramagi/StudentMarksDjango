from django.forms import ModelForm
from .models import StuMarks

class MarkForm(ModelForm):
    class Meta:
        model = StuMarks
        fields = "__all__"