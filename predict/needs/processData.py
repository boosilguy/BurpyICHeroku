import numpy as np
from PIL import Image
import io

def process_result_dict(result, size):
    temp_result = result
    sorted_list = list()
    
    # 만약 list size를 조절하고 싶다면, Unity 프로젝트의 결과 size도 고려해야 한다.
    for i in range(size):
        highest_predict_key = max(temp_result.keys(), key=(lambda k: temp_result[k]))
        highest_predict_value = temp_result[highest_predict_key]
        del temp_result[highest_predict_key]

        sorted_list.append({"id":highest_predict_key,"percentage":highest_predict_value})

    return sorted_list
