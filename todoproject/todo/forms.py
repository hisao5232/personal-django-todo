from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_date']  # モデルに応じて調整
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})  # カレンダー入力に
        }