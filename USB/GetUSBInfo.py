from dataclasses import dataclass
from typing import Optional
from USB.customType import UnmanagedType
import serial
import usb

@dataclass
class USBIds:
    SatoVendorID: int = 2088
    OKIVendorID: int = 1724
    LexmarkVendorID: int = 1085
    ATenVendorID: int = 1367
    Valid_VIDs = [
        LexmarkVendorID,
        ATenVendorID,
        OKIVendorID,
        SatoVendorID
    ]


class USBInfo:
    def __init__(self):
        self.__name = ""
        self.__uportid = ""
        self.Name: str = self.__name
        self.PortID: str = self.__uportid

    def set_usb_info(self, name:str, portid:str) -> ():
        self.__name = name
        self.__uportid = portid

    def get_usb_name(self) -> str:
        return str(self.__name)


class USBPort:
    def __init__(self):
        self.hUSB_IN : Optional
        self.hUSB_OUT: Optional
        self.portID: str
        self.isOpen: bool

    def IsOpen(self) -> bool:
        return UnmanagedType.U1


@dataclass
class STAO_USB_Info:
    VID = int("0828")
    PID = int("0122")


