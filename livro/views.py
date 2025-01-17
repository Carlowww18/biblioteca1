from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuarios
from .models import Livros, Categoria, Emprestimos
from .forms import CadastroLivro, CategoriaLivro
from django import forms


def home(request):
    if request.session.get('usuario'):
         usuario = Usuarios.objects.get(id = request.session['usuario'])
         status_categoria = request.GET.get('cadastro_categoria')
         livros = Livros.objects.filter(usuario = usuario)
         form = CadastroLivro()
         form_categoria = CategoriaLivro()

         usuarios = Usuarios.objects.all()

         form.fields['usuario'].initial = request.session['usuario']
         form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)

         livros_emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
         
         return render(request, 'home.html', {'livros': livros,
                                             'usuario_logado': request.session.get('usuario'),
                                              'form': form,
                                              'form_categoria': form_categoria,
                                              'status_categoria': status_categoria,
                                              'usuarios': usuarios,
                                              'livros_emprestar': livros_emprestar})
    else:
         return redirect('/auth/login/?status=2')
    
def ver_livro(request, id):
     if request.session.get('usuario'):
          livro = Livros.objects.get(id=id)

          if request.session.get('usuario') == livro.usuario.id:
               categoria_livro = Categoria.objects.filter(usuario_id = request.session.get('usuario'))
               emprestimos = Emprestimos.objects.filter(livro = livro)
               form_categoria = CategoriaLivro()
               usuarios = Usuarios.objects.all()
               form = CadastroLivro()
               usuario = Usuarios.objects.get(id = request.session['usuario'])
               form.fields['usuario'].initial = request.session['usuario']
               form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
               livros = Livros.objects.filter(usuario = usuario)
               livros_emprestar = Livros.objects.filter(usuario = usuario).filter(emprestado = False)
         


               return render(request, 'ver_livro.html',{'livro': livro,
                                                       'categoria_livro': categoria_livro,
                                                       'emprestimos': emprestimos, 
                                                       'usuario_logado': request.session.get('usuario'),
                                                       'form': form,
                                                       'id_livro': id,
                                                       'form_categoria': form_categoria,
                                                       'usuarios': usuarios,
                                                       'livros': livros,
                                                       'livros_emprestar': livros_emprestar})
          else:
               return HttpResponse('esse livro não é seu')
     return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
     if request.method == 'POST':
          form = CadastroLivro(request.POST)
     
          if form.is_valid():
            form.save()
            return redirect('/livro/home')
          else:
            return HttpResponse('DADOS INVÁLIDOS')
          
def excluir_livro(request, id):
    livro =  Livros.objects.get(id= id).delete()
    return redirect('/livro/home')

def cadastrar_categoria(request):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
     
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuarios.objects.get(id = id_usuario)
        categoria = Categoria(nome = nome, descricao = descricao, usuario = user)
        categoria.save()
        return redirect('/livro/home')
    else:
        return HttpResponse('DEU ERRO SEU LIXO')

def cadastrar_emprestimo(request):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
        livro_emprestado = request.POST.get('livro_emprestado')
        
        if nome_emprestado_anonimo:
               emprestimo = Emprestimos(nome_emprestado_anonimo = nome_emprestado_anonimo, livro_id = livro_emprestado)
        else:
            emprestimo = Emprestimos(nome_emprestado_id = nome_emprestado, livro_id = livro_emprestado)

        emprestimo.save()

        livro = Livros.objects.get(id = livro_emprestado)
        livro.emprestado = True
        livro.save()

        return HttpResponse('Emprestimo realizado com sucesso')