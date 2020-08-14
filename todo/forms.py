from .models import Todo
from django import forms

class CreateTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        widgets = {
            'Todo_item': forms.TextInput(attrs={'placeholder': 'Create todo items...'}),
        }