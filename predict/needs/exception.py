import sys
import traceback

def config_except_info():
    e_type, e_value, e_traceback = sys.exc_info()
    
<<<<<<< HEAD
    # 오류 스택들 추출
=======
    # 오류 스택을 리스트로 추출
>>>>>>> 580ab38780ad7968f7506ee2e5cc68f46da644e8
    e_traceback = traceback.extract_tb(e_traceback)

    stack_trace = list()

    for t in e_traceback:
        stack_trace.append("File : %s, line : %d, Function : %s, Message : %s \n" % (t[0], t[1], t[2], t[3]))
    
    trace_string = "\n"
    
    for stack in stack_trace:
        trace_string = trace_string + str(stack)

    exception = dict()
    exception["Exception type"] = str(e_type)
    exception["Exception message"] = str(e_value)    
    exception["Stack trace"] = trace_string

    return exception

def print_except_info(dict):
<<<<<<< HEAD
    print("Burpy Image Classification Server Error")
    print("Exception type - %s" % dict["Exception type"])
    print("Exception message - %s" % dict["Exception message"])
    print("Stack trace - %s" % dict["Stack trace"])
    
=======
    print(" ")
    print(" Exception type - %s" % dict["Exception type"])
    print(" Exception message - %s" % dict["Exception message"])
    print(" Stack trace - %s" % dict["Stack trace"])
    print(" ")
>>>>>>> 580ab38780ad7968f7506ee2e5cc68f46da644e8
