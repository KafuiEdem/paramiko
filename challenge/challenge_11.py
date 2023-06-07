"""
Challenge #11
Consider myparamiko.py script developed in the course.
Add a new function called send_from_list() that receives as an argument a Python list of commands and sends all commands to the remote device to be executed.
"""

import myparamiko_11

commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user','wr']

ssh_clint = myparamiko_11.connect(server_ip="192.168.123.2",server_port="22",user="edem",passwd="cisco")
shell = myparamiko_11.get_shell(ssh_client=ssh_clint)
myparamiko_11.send_from_list(commands,shell)
