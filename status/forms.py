from django import forms
from .views import Post

class PostForm(forms.ModelForm):
    Author = forms.CharField()
    Title = forms.CharField()
    Text = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Post
        fields = ('title', 'text',)

