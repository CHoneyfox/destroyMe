from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.utils.datetime_safe import new_datetime, datetime
from django.views import generic

import os
from .models import File

# Create your views here.

def index(request):
    return render(request, "index.html", {})


def delete(request):
    username = request.POST["username"]
    file = request.POST["file"]
    message = request.POST["message"]
    if message == "Optional Message" or message == "":
        message = "<no message supplied>"

    try:
        os.remove(file)
    except OSError as error:
        return render(request, "failed.html", {"reason": error})
    else:
        File.objects.create(destroyed_by=username, message=message, path=file, time_stamp=new_datetime(datetime.now()))
    return HttpResponseRedirect("/")

class List(generic.ListView):
    template_name = "list.html"
    context_object_name = "files"

    def get_queryset(self):
        return File.objects.all()

def details(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    return render(request, "details.html", {"file": file})