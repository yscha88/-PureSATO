import subprocess, json
from pprint import pprint


cmd = """PowerShell -Command "Get-PnpDevice | Select-Object status,class,FriendlyName,InstanceID | ConvertTo-Json" """
out = subprocess.getoutput(cmd)
list = json.loads(out)

for item in list:
    if item['Class'] == "USB" and item['FriendlyName'] == "USB 인쇄 지원":
        pprint(item, indent=2)
