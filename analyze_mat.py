import scipy.io as sio
import pandas as pd
import uuid
import time

def generate_GUID():
    version = "v1.0"
    user = "czs"
    domin = ["require","design","manufacture","experient"]
    global_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    global data01_guid
    data01_guid = uuid.uuid1()
    global data01_new_guid
    data01_new_guid= str(data01_guid) + '-' + version + "-" + domin[1] + "-" + user + "-" + global_time
    return data01_new_guid
    pass

if __name__ == '__main__':
    mat_data = sio.loadmat("matlab.mat")



    data = mat_data['l1']
    print('l1',data)

    data = mat_data['l2']
    print('l2',data)

    data = mat_data['l3']
    print('l3',data)

    data = mat_data['qn']
    print('qn',data)

    data = mat_data['t1']
    print('t1',data)

    data = mat_data['t2']
    print('t2',data)

    data = mat_data['t3']
    print('t3',data)

    ######  GUID   FOLLOWING

    print("    ")

    generate_GUID()
    data = mat_data['l1']
    print("变量名=l1", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

    generate_GUID()
    data = mat_data['l2']
    print("变量名=l2", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

    generate_GUID()
    data = mat_data['l3']
    print("变量名=l3", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

    generate_GUID()
    data = mat_data['qn']
    print("变量名=qn", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

    generate_GUID()
    data = mat_data['t1']
    print("变量名=t1", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

    generate_GUID()
    data = mat_data['t2']
    print("变量名=t2", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

    generate_GUID()
    data = mat_data['t3']
    print("变量名=t3", " ", "GUID=%s" % data01_new_guid)
    generate_GUID()
    print("value=%s"%data," ", "GUID=%s" % data01_new_guid)

