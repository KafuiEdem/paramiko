import myparamiko

client = myparamiko.connect(server_ip="192.168.123.200",login="edem",passwd="1234",port_num="22")
shell = myparamiko.ssh_shell(client)
myparamiko.send_command(shell,commend="pwd")
output = myparamiko.show(shell=shell)
print(output)