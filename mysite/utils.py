from decimal import Decimal
from mysite.models import Republica, Usuario
PRECISION_MAP = {
    0: Decimal('1.0'),      # -/+ 111  km
    1: Decimal('0.1'),      # -/+ 11.1 km
    2: Decimal('0.01'),     # -/+ 1.11 km
    3: Decimal('0.001'),    # -/+ 111  m
    4: Decimal('0.0001'),   # -/+ 11.1 m
    5: Decimal('0.00001'),  # -/+ 1.11 m
    6: Decimal('0.000001'), # -/+ 11.1 cm
    7: Decimal('11.0'), 
}


def encontrar_republica(lat, lng):
    precison = 1
    _range = PRECISION_MAP[precison]
    lat = Decimal(lat)
    lng = Decimal(lng)
    #https://gist.github.com/chronossc/a67517621c2a9d4c2f14
    republicas = Republica.objects.filter(
        latitude__gte= lat - (_range ), latitude__lte=lat + (_range ),
        longitude__gte=lng - (_range ), longitude__lte=lng + (_range)
    )
    
    return republicas
def busca_filtros(latitude, longitude, qtd_vagas, tipo_imovel, genero, valor):
    if valor:
        valor = valor.replace(',','.')
        valor = Decimal(valor)
    republicas = []
    precison = 1
    _range = PRECISION_MAP[precison]
    import ipdb; ipdb.set_trace()
    if latitude:
        lat = Decimal(latitude)
        lng = Decimal(longitude)
        rep_loc = Republica.objects.filter(
            latitude__gte=lat - (_range ), latitude__lte=lat + (_range ),
            longitude__gte=lng - (_range ), longitude__lte=lng + (_range)
        )
        for rep in rep_loc:
            if rep:
                republicas.append(rep)
    
    if tipo_imovel:
        rep_tipo_imovel = Republica.objects.filter(tipo_imovel=tipo_imovel)
        for rep in rep_tipo_imovel:
            if rep:
                republicas.append(rep)
    if qtd_vagas:
        rep_vagas = Republica.objects.filter(qtd_vagas__gte=qtd_vagas)
        for rep in rep_vagas:
            if rep:
                republicas.append(rep)
    if valor:
        rep_valor = Republica.objects.filter(valor__lte=valor)
        for rep in rep_valor:
            if rep:
                republicas.append(rep)
    if genero:
        rep_genero = Republica.objects.filter(genero=genero)
        for rep in rep_genero:
            if rep:
                republicas.append(rep)
    
    
    
    for index,rep in enumerate(republicas):
        republicas.pop(index)
        if rep in republicas:
            pass
        else:
            if not rep:
                pass
            else:
                republicas.append(rep)

    return republicas
#def enviar_mensagem(mensagem):

