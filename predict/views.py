from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from predict.needs.processData import *
from predict.needs.predict import *
from predict.needs.recommendation import *
from predict.needs.jsonProcess import *
from predict.needs.exception import * 

import json


def inappropriate_access(request):
    print(request)
    return render(request, 'inappropriate.html', {})

def image_classification(request):
<<<<<<< HEAD
=======
    # try-except의 주석
>>>>>>> 580ab38780ad7968f7506ee2e5cc68f46da644e8
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
    
<<<<<<< HEAD
=======
    return JsonResponse(result, safe=False)

def on_recommend_train_data(request):
    result = save_train_data(request.body)
    result = encode_json(result)
    return JsonResponse(result, safe=False)

def on_recommend_train(request):
    user_list = json.loads(request.body.decode("utf-8"))
    for user in user_list:
        print(user)
        result = train_recommendation(user['_id'])
    
    result = encode_json(result)
    return JsonResponse(result, safe=False)

def on_recommend_predict_data(request):
    result = save_predict_data(request.body)
    result = encode_json(result)
    return JsonResponse(result, safe=False)

def on_recommend_predict(request):
    user_list = json.loads(request.body.decode("utf-8"))
    for user in user_list:
        result = predict_recommendation(user['_id'])
    
    result = encode_json(result)
    return JsonResponse(result, safe=False)

def on_recommend_predict_result(request):
    user_id = request.body.decode("utf-8")
    result = fetch_predict_result(user_id)
    result = encode_json(result)
>>>>>>> 580ab38780ad7968f7506ee2e5cc68f46da644e8
    return JsonResponse(result, safe=False)