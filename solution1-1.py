import winreg
from winreg import *

def find_sato_devices():
    update_id_list = []
    for i in range(0, 1024):
        try:
            connected = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            root_key = OpenKey(key=connected, sub_key="SYSTEM\\CurrentControlSet\\Control\\DeviceClasses\\")
            keyname = str(EnumKey(root_key, i))
            update_id_list.append(keyname)
        except Exception as e:
            pass

    for key_name in update_id_list:
        try:
            connected = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
            root_key = OpenKey(key=connected, sub_key="SYSTEM\\CurrentControlSet\\Control\\DeviceClasses\\")
            print(key_name)
            for i in range(0, 10):
                try:
                    sub_key_name = str(EnumKey(OpenKeyEx(root_key, key_name), i))
                    print("    " + sub_key_name)
                except Exception as e:
                    pass
        except:
            pass


if __name__ == "__main__":
    find_sato_devices()
    #  {0ecef634-6ef0-472a-8085-5ad023ecbccd}
    #        ##?#SWD#PRINTENUM#{0CB311C8-124C-4784-A039-6DDA34DB11F7}#{0ecef634-6ef0-472a-8085-5ad023ecbccd} < -- sato
    #        ##?#SWD#PRINTENUM#{3F7CE687-766E-49F8-A127-CA7C2016E51E}#{0ecef634-6ef0-472a-8085-5ad023ecbccd}
    #        ##?#SWD#PRINTENUM#{79D256E0-5AC4-4BEC-B12D-CF0A94FB31AF}#{0ecef634-6ef0-472a-8085-5ad023ecbccd}
    #        ##?#SWD#PRINTENUM#{A2FF8CD2-D356-464B-A751-FF50DE622DEA}#{0ecef634-6ef0-472a-8085-5ad023ecbccd}
    #        ##?#SWD#PRINTENUM#{F813D574-0430-45C6-B1A7-78AA5C191F45}#{0ecef634-6ef0-472a-8085-5ad023ecbccd}

    #  {28d78fad-5a12-11d1-ae5b-0000f803a8c2}
    #    ##?#USB#VID_0828&PID_0122#LTNX3393#{28d78fad-5a12-11d1-ae5b-0000f803a8c2}
