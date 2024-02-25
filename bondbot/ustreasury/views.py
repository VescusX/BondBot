from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import BondType, DailyBond

from datetime import date
from xml.etree import ElementTree

import requests

def index(request):
    if messages:
        return render(request,'ustreasury/index.html')


def refresh(request):

    # day = date.today()
    tday = date(2023,2,23)
    day_str = day.strftime('%m-%d-%Y')
    gov_url = 'https://home.treasury.gov/sites/default/files/interest-rates/yield.xml'
    response = requests.get(url = gov_url)
    tree = ElementTree.fromstring(response.content)
    yield_obj = tree.find("LIST_G_WEEK_OF_MONTH//G_WEEK_OF_MONTH//LIST_G_NEW_DATE//G_NEW_DATE[NEW_DATE='"+day_str+"']")
    if yield_obj:
        messages.success(request, 'Changes successfully saved.' + day_str)
        for node in yield_obj.find("LIST_G_BC_CAT/G_BC_CAT"):
            bto = BondType.objects.get(bc_cat=node.tag)
            if bto:
                r = DailyBond(bond_type=bto, day=tday, yield_rate=node.text)
                
    else:
        messages.warning(request, 'Data for today is unavailable')

    return redirect('index')
