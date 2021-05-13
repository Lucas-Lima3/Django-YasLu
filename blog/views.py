from django.shortcuts import render

from blog.models import Publication


def render_index(request):
    return render(request, 'index.html', {})


def render_publication_done(request):
    publication_data = {
        'nome': request.POST.get('nome'),
        'cwid': request.POST.get('cwid'),
        'opicoes_bayflex': request.POST.get('opicoes_bayflex'),
        'email': request.POST.get('email'),
    }
    publication = Publication(**publication_data)
    publication.save()
    return render(request, 'publication_done.html', {'nome': publication.nome})
