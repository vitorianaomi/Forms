from django.shortcuts import render
from .forms import AlunoForm, ProfessorForm, ProjetoForm
from .models import Aluno, Professor, Projeto

# Create your views here.
def cadastro_aluno(request): #exibir e cadastrar formulário
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
        print("->>>> Entrou primeiro aqui")
        form = AlunoForm() #instanciando a classe do formulário

    return render(request, 'form/form_aluno.html', {'form': form}) #colocando em um contexto e enviando form para página



def cadastro_professor(request): #exibir e cadastrar formulário
    if request.method == 'POST':  
        form = ProfessorForm(request.POST) #pega tudo da requisição e coloca no form
        if form.is_valid(): #verificação dos valores comparando-os com o model: True ou False
            form.save() #pega o que está no formulário e salva no banco
            form = ProfessorForm() #"limpeza" do formulário e apresentação de um novo em branco
    else: #primeira vez sempre vai ser get; só entra na parte acima quando for dado o primeiro submit
        form = ProfessorForm()

    return render(request, 'form/form_professor.html', {'form': form}) #colocando em um contexto e enviando form para página




def cadastro_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProjetoForm()
    else:
        form = ProjetoForm()
    return render(request, 'form/form_projeto.html', {'form': form})