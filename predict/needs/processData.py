import numpy as np
from PIL import Image
import io

def process_result_dict(result, size):
    temp_result = result
    sorted_list = list()
    
<<<<<<< HEAD
    # 결과 List 사이즈를 조절할 수 있습니다. 다만 Unity 프로젝트의 변수도 고려되어야 합니다.
=======
    # 만약 list size를 조절하고 싶다면, Unity 프로젝트의 결과 size도 고려해야 한다.
>>>>>>> 580ab38780ad7968f7506ee2e5cc68f46da644e8
    for i in range(size):
        highest_predict_key = max(temp_result.keys(), key=(lambda k: temp_result[k]))
        highest_predict_value = temp_result[highest_predict_key]
        del temp_result[highest_predict_key]

        sorted_list.append({"id":highest_predict_key,"percentage":highest_predict_value})

    return sorted_list
