import paramiko
import time
import getpass
from scp import SCPClient


ssh_client = paramiko.SSHClient()

password = getpass.getpass("Enter password:")
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname="192.168.123.2",username="edem",password="cisco",port="22",look_for_keys=False,allow_agent=False)

router = {"hostname":"192.168.123.200","username":"edem","password": password,"port":"22"}
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)


scp = SCPClient(ssh_client.get_transport())
# scp.put("data_serialization\paramiko\orouter1.txt","/tmp/device.txt")
# scp.put("data_serialization\paramiko\directory1",recursive=True,remote_path='/tmp')
scp.get('/etc/passwd','data_serialization\paramiko\passwd')

scp.close()