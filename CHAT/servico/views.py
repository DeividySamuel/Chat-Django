
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML




def servico(request):
    if request.method == 'GET':
        return render(request, 'servico.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        bairro = request.POST.get('bairro')
        cep = request.POST.get('cep')
        email = request.POST.get('email')
        modelo =request.POST.get('modelo')
        detalhes = request.POST.get('detalhes')
        relato_do_cliente = request.POST.get('relato_do_cliente')
        servico_a_ser_prestado = request.POST.get('servico_a_ser_prestado')
        observacao = request.POST.get('observacao')
        valor_dos_servico =request.POST.get('valor_dos_servico')
        valor_das_pecas = request.POST.get('valor_das_pecas')
        valor_total =request.POST.get('valor_total')
    
         
        paragraphs = [nome, endereco, cidade, telefone, cpf, bairro, cep, email, modelo,
                    detalhes, relato_do_cliente, servico_a_ser_prestado, observacao, 
                    valor_dos_servico, valor_das_pecas, valor_total,]
        html_string = render_to_string('pdf.html', {'paragraphs': paragraphs})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/mypdf.pdf')

        fs = FileSystemStorage('/tmp')
        with fs.open('mypdf.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

       
def pdf(request):
    context = {}
    return render(request, "pdf.html", context=context)



    
