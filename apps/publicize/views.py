import markdown

from django.shortcuts import render

from .import models


def index(request):
    return render(request, 'publicize/index.html')


def flow_detail(request, pk):
    """ 单个流程 """

    flow_all = models.FlowPath.objects.all()
    f_detail = models.FlowPath.objects.get(pk=pk)

    return render(request, 'publicize/flow_detail.html', locals())
