from django.shortcuts import render
from .forms import LatLngForm
from .models import Republica
from .utils import find_nearest_storen
from django.views.decorators.csrf import csrf_exempt
import json
from decimal import Decimal

def index(request):
    form = LatLngForm()

    return render(request,'index.html', {'form':form})

@csrf_exempt
def estudante(request):
    filename = 'pontos.json'
    json = """
        {
        "Latitude": {0},
        "Longitude": {1}
    },
    """

    PRECISION_MAP = {
    0: Decimal('1.0'),      # -/+ 111  km
    1: Decimal('0.1'),      # -/+ 11.1 km
    2: Decimal('0.01'),     # -/+ 1.11 km
    3: Decimal('0.001'),    # -/+ 111  m
    4: Decimal('0.0001'),   # -/+ 11.1 m
    5: Decimal('0.00001'),  # -/+ 1.11 m
    6: Decimal('0.000001')  # -/+ 11.1 cm
    }

    if request.POST:
        republicas = []

        precison = 1
    
        results = {}  # dict is already sorted from lower to greater ;)
        # now I would love a graph database ;)
        _range = PRECISION_MAP[precison]
        stores = Republica.objects.filter(
            # Here we search around a range. 9 is a modifier in _range to
            # be a bit more wide, specially in depth precisions. More stations
            # per loop means less queries.
            latitude__gt=Decimal(float(request.POST.get('latitude'))) - (_range * 9), latitude__lt=Decimal(float(request.POST.get('latitude'))) + (_range * 9),
            longitude__gt=Decimal(float(request.POST.get('longitude'))) - (_range * 9), longitude__lt=Decimal(float(request.POST.get('longitude'))) + (_range * 9)
        )
        print (stores)
        #if republicas:
         #   for republica in republicas:
          #      with open(filename,'w') as f:
           #         import pdb; pdb.set_trace()
            #        conteudo = f.writelines(json.format(republica.latitude,republica.longitude))
            
    return render(request,'estudante.html', {'republicas':republicas})
