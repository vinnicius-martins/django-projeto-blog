from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        qs = qs.filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios = Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs    
class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

class PostDetalhes(UpdateView):
    pass