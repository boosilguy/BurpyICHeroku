import numpy as np
from PIL import Image
import io

def process_result_dict(result, size):
    temp_result = result
    sorted_list = list()
    
    # 결과 List 사이즈를 조절할 수 있습니다. 다만 Unity 프로젝트의 변수도 고려되어야 합니다.
    for i in range(size):
        highest_predict_key = max(temp_result.keys(), key=(lambda k: temp_result[k]))
        highest_predict_value = temp_result[highest_predict_key]
        del temp_result[highest_predict_key]

        sorted_list.append({"id":highest_predict_key,"percentage":highest_predict_value})

    return sorted_list
