from django import forms

class Aluno(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    obs = forms.IntegerField(widget=forms.Textarea(), label='Observações')