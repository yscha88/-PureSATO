from winreg import *
import win32com.client


def get_usb_device() -> dict:
    try:
        usb_list = []
        wmi = win32com.client.GetObject("winmgmts:")
        for usb in wmi.InstancesOf("Win32_USBHub"):
            if str(usb.DeviceID).endswith("LTNX3393"):
                text = str(usb.DeviceID)
                VID = str(usb.DeviceID)[str(usb.DeviceID).find("VID_") + 4: str(usb.DeviceID).find("VID_") + 4 + 4]
                PID = str(usb.DeviceID)[str(usb.DeviceID).find("PID_") + 4: str(usb.DeviceID).find("PID_") + 4 + 4]
                return {
                    "VID" : VID,
                    "PID" : PID,
                    "Name" : "LTNX3393",
                    "status": "ok"
                }
    except Exception as error:
        print('error', error)

    return {
        "status": "bad"
    }


def get_extend_sato_data() -> dict:
    sato = get_usb_device()
    # SATO.Printer.GetUSBInfo.USBSender.GetPortName
    if sato['status'] == "ok":
        root_reg = OpenKeyEx(
            key=HKEY_LOCAL_MACHINE,
            sub_key="SYSTEM\\CurrentControlSet\\Control\\DeviceClasses\\{28d78fad-5a12-11d1-ae5b-0000f803a8c2}",
            access=KEY_ALL_ACCESS)

        """ ##?#USB#VID_0828&PID_0122#LTNX3393#{28d78fad-5a12-11d1-ae5b-0000f803a8c2 """
        root_child_1 = str(EnumKey(root_reg, 0))
        print(root_child_1)

        """ # """
        child_root_1 = OpenKeyEx(key=root_reg, sub_key=root_child_1, access=KEY_READ)
        root_child_2 = str(EnumKey(child_root_1, 0))
        print(root_child_2)

        """ Device Parameters """
        child_root_2 = OpenKeyEx(key=child_root_1, sub_key=root_child_2, access=KEY_READ)
        root_child_3 = str(EnumKey(child_root_2, 0))
        print(root_child_3)

        chilr_root_3 = OpenKeyEx(key=child_root_2, sub_key=root_child_3, access=KEY_READ)
        for i in range(0, 5):
            name, value, type = EnumValue(chilr_root_3, i)
            name = str(name).replace(" ", "_")
            value = str(value)
            sato[name] = value

    return sato

