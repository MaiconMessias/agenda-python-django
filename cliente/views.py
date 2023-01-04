from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Cliente
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

def index(request):
    cliente_list = Cliente.objects.order_by('id')
    template = loader.get_template('cliente/index.html')
    context = {
        'cliente_list': cliente_list,
    }
    return HttpResponse(template.render(context, request))

def adicionar(request):
    #template = loader.get_template('cliente/adicionar.html')
    return render(request, 'cliente/adicionar.html')

def editar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'cliente/editar.html', {'cliente': cliente, 'cliente_id': cliente_id})    

def salvar(request):
    #cliente = Cliente(nome = request.POST['nome'], datanascimento = timezone.now())
    #timezone.now()
    if (request.POST['id'] == ''):
        cliente = Cliente()
        cliente.nome = request.POST['nome']
        cliente.datanascimento = datetime.strptime(request.POST['datanascimento'], "%d/%m/%Y")
        cliente.save()
        return HttpResponseRedirect(reverse('index'))        
    else:    
        cliente = get_object_or_404(Cliente, pk=request.POST['id'])
        cliente.nome = request.POST['nome']
        cliente.datanascimento = datetime.strptime(request.POST['datanascimento'], "%d/%m/%Y")
        cliente.save()
        return HttpResponseRedirect(reverse('index'))        
        #return HttpResponse("Não salvo o cliente: " + request.POST['id'])   

def deletar(request, cliente_id):
    if (request.POST['del'] == 'Sim'):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        cliente.delete()
        return HttpResponseRedirect(reverse('index'))        
    else:    
       return HttpResponseRedirect('/cliente/editar/%d/' % cliente_id) 