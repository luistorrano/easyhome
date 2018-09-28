from decimal import Decimal
from mysite.models import Republica
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
    #https://gist.github.com/chronossc/a67517621c2a9d4c2f14
    republicas = Republica.objects.filter(
        latitude__gt=lat - (_range * 9), latitude__lt=lat + (_range * 9),
        longitude__gt=lng - (_range * 9), longitude__lt=lng + (_range * 9)
    )
    return republicas
