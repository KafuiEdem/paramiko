import myparamiko
from datetime import datetime

router = {"server_ip":"192.168.123.2","login":"edem","passwd":"cisco","port_num":"22"}
client = myparamiko.connect(**router)
shell = myparamiko.ssh_shell(client)
myparamiko.send_command(shell,"enable")
myparamiko.send_command(shell,"cisco")
myparamiko.send_command(shell,"termi leng 0")
myparamiko.send_command(shell,commend="sh run")
output = myparamiko.show(shell)

output_list = output.splitlines()

output_list = output_list[10:-1]
output_ = "\n".join(output_list)

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
file = f"{router['server_ip']}_{year}-{month}-{day}.txt"
with open(f"data_serialization\paramiko\{file}","w") as f:
    f.write(output_)

myparamiko.close(client)