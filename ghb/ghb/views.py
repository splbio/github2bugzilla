import subprocess
from subprocess import Popen, PIPE
import json

from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponse('Hello', status=200)

