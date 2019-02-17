from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
    print(request.method)  # GET 请求反方式
    print(request.GET)  # {}  []  get()
    print(request.POST)  # {}  []  get()
    print(request.path_info)  # 路径信息   不包含IP和端口、参数
    # print(request.body)
    # print(request.scheme)
    # print(request.META)
    # print(request.get_host())
    print(request.get_full_path())  # 路径信息 + 参数
    return render(request, 'index.html')


# 上传文件
def upload(request):
    if request.method == 'POST':
        # print(request.body)
        file = request.FILES.get('f1')
        with open(file.name, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return HttpResponse('上传成功')

    return render(request, 'upload.html')


import json
from django.http import JsonResponse


def json_test(request):
    data = {'name': 'alex', 'pwd': 'alexdsb'}

    ret = HttpResponse(json.dumps(data))
    ret['Content-Type'] = 'application/json'
    ret['xxx'] = 'axxx'
    return ret
    # return HttpResponse(json.dumps(data), content_type='application/json')  # Content-Type: text/html; charset=utf-8
    # return JsonResponse(data)  # Content-Type: application/json
