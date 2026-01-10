from django import forms


class NewTaskForm(forms.Form):
    title = forms.CharField(label='Task', max_length=100)
    description = forms.CharField(label='Description', max_length=200)
