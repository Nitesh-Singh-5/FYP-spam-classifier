from django import  forms
from .models import Form_Message

class FeedbackForm(forms.ModelForm):
     class Meta:
        model = Form_Message
        fields = ['message', 'result', 'accuracy']
        