from pywinusb import hid
import time


for item in hid.find_all_hid_devices():
    print(item.vendor_id, item.product_id, item.product_name)


# 해봤는데 HID만 지원하는 거래서 키보드 마우스 같은것만 나온당..ㅠ