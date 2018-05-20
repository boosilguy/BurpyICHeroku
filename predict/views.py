from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from predict.needs.processData import *
from predict.needs.predict import *
from predict.needs.jsonProcess import *
from predict.needs.exception import * 


def inappropriate_access(request):
    print(request)
    return render(request, 'inappropriate.html', {})

def image_classification(request):
    print(request)
    try:
        img_file = decode_json(request, 'image')
        result = inception_predict(img_file)
        result = encode_json(result)
        print(result)
    
    except Exception as e:
        except_info = config_except_info()
        print_except_info(except_info)
        result = encode_json(except_info)
    
    return JsonResponse(result, safe=False)