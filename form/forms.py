from django import forms
from.models import Professor, Projeto

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length = 150)
    email = forms.EmailField()
    data_nascimento = forms.DateField()
    

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = '__all__' #ou ['nome', 'disciplina']


class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = '__all__' #ou ['nome', 'disciplina']
