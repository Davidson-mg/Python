from django import template

register = template.Library()

@register.filter(name='plural_comentarios') #este metodo vai ser usado por exemplo no arquivo index.html nos locais
#onde mostramos os comentarios. Lembrando que no html que formos utilizara este metodo, será necessario efetuar o
#{% load dafilters %}
def plural_comentarios(num_comentarios):
    try:
        num_comentarios = int(num_comentarios)
        if num_comentarios == 0:
            return f'Nenhum comentário'
        elif num_comentarios == 1:
            return f'{num_comentarios} Comentário'
        else:
            return f'{num_comentarios} Comentários'
    except:
        return f'{num_comentarios} coméntario(s)'