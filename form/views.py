from django.shortcuts import render
from .forms import AlunoForm
from .models import Aluno

# Create your views here.
def cadastro_aluno(request): #renderizar e cadastrar
    if request.method == 'POST':  
        form = AlunoForm(request.POST) #pega tudo da requisição e coloca no form
        if form.is_valid(): #os valores são válidos? True ou False
            nome = form.cleaned_data['nome'] #form.cleaned_data[]: dicionário com os tipos convertidos e corretos
            email = form.cleaned_data['email']
            data_nascimento = form.cleaned_data['data_nascimento']
            #salvando o aluno no banco.
            #Aluno.objects.create(nome=nome, email=email,data_nascimento=data_nascimento)
            print("Nome: {} - Email: {} - Data de Nascimento: {}".format(nome,email,data_nascimento))
    else: #primeira vez sempre vai ser get; só entra na parte acima quando for dado o primeiro submit
        print("->>>> entrou primeiro aqui")
        form = AlunoForm() #instanciando a classe do formulário

    return render(request, 'form/form_aluno.html', {'form': form}) #colocando em um contexto e enviando form para página