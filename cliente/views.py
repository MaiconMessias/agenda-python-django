from django.shortcuts import get_object_or_404, render
from .models import Cliente
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.hashers import make_password, check_password

@login_required(login_url='/cliente/telalogin/')
def index(request):
    if not request.user.is_authenticated:
        return render(request, 'cliente/telalogin.html')
    return render(request, 'cliente/index.html')

@login_required(login_url='/cliente/telalogin/')
def pesquisacliente(request):
    cliente_list = Cliente.objects.order_by('id')
    template = loader.get_template('cliente/pesquisacliente.html')
    context = {
        'cliente_list': cliente_list,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/cliente/telalogin/')
def adicionar(request):
    #template = loader.get_template('cliente/adicionar.html')
    return render(request, 'cliente/adicionar.html')

@login_required(login_url='/cliente/telalogin/')
def editar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'cliente/editar.html', {'cliente': cliente, 'cliente_id': cliente_id})    

@login_required(login_url='/cliente/telalogin/')
def salvar(request):
    #cliente = Cliente(nome = request.POST['nome'], datanascimento = timezone.now())
    #timezone.now()
    if (request.POST['id'] == ''):
        cliente = Cliente()
        cliente.nome = request.POST['nome']
        cliente.datanascimento = datetime.strptime(request.POST['datanascimento'], "%d/%m/%Y")
        cliente.save()
        return HttpResponseRedirect(reverse('pesquisacliente'))        
    else:    
        cliente = get_object_or_404(Cliente, pk=request.POST['id'])
        cliente.nome = request.POST['nome']
        cliente.datanascimento = datetime.strptime(request.POST['datanascimento'], "%d/%m/%Y")
        cliente.save()
        return HttpResponseRedirect(reverse('pesquisacliente'))        
        #return HttpResponse("Não salvo o cliente: " + request.POST['id'])   

@login_required(login_url='/cliente/telalogin/')
def deletar(request, cliente_id):
    if (request.POST['del'] == 'Sim'):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        cliente.delete()
        return HttpResponseRedirect(reverse('pesquisacliente'))        
    else:    
       return HttpResponseRedirect('/cliente/editar/%d/' % cliente_id) 

def telalogin(request):
    # funções check_password e make_password usadoas para hashs personalisados
    # senhacerta = check_password('teste', make_password('teste'))
    return render(request, 'cliente/telalogin.html')

def logar(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return render(request, 'cliente/index.html')
    else:
        return render(request, 'cliente/telalogin.html')

def logout_view(request):
    logout(request)
    return render(request, 'cliente/telalogin.html')
