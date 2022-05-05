from django.shortcuts import render

# Add your views here.
from django.http import HttpResponse
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _

def index( request, *args, **kwargs):
    output = _('StatusMsg')
    #print(language_code)
    #self.language_code="kk"
    #print(self.language_code )
    return HttpResponse(output)

def welcome(request):
    return render(request,"lecture15_app/index.html")