import subprocess, json
from pprint import pprint


cmd = """PowerShell -Command "Get-PnpDevice | Select-Object status,class,FriendlyName,InstanceID | ConvertTo-Json" """
out = subprocess.getoutput(cmd)
list = json.loads(out)

for item in list:
    try:
        if item['FriendlyName'].find("SATO") > -1:
            print(item)
    except Exception as e:
        pass
