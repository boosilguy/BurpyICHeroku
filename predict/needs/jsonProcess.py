from django.http import HttpResponse
import json
import base64

# Json 타입 디코딩
def decode_json(request, json_field):
    json_data = json.loads(request.body.decode('utf-8'))
    json_data = json_data[json_field]
    return base64.b64decode(json_data)

# Json 타입 인코딩
def encode_json(target):
    result = dict()
    if len(target) != 0:
        result['result'] = target
    else:
        e = Exception('Result-dict\'s length is 0')
        raise e
    return result