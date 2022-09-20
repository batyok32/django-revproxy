from django.shortcuts import render

# Create your views here.
from revproxy.views import ProxyView

class TestProxyView(ProxyView):
    upstream = 'http://pm-a6cd1a28.com'
