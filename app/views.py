__author__ = 'mriegel'

from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
import os
import json

@login_required()
def print_env(request):
    return HttpResponse(json.dumps(os.environ), content_type="application/json")