from django import template

register = template.Library()

@register.filter
def last(vetor):
    return vetor[-1]
@register.filter
def tamanho(vetor):
    return len(vetor)