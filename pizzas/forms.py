from django import forms

from .models import Comment

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment              #base the form of the comment model
        fields = ['text']            #don't have to show all fields from topic model
        labels = {'text':''}                
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        