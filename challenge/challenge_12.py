import myparamiko_11

"""
Challenge #12

Consider myparamiko.py script developed in the course.
Add a new function called send_from_file() that receives as an argument a text file with commands and sends all commands to the remote device to be executed.
"""
ssh_client = myparamiko_11.connect(server_ip="192.168.123.2",server_port="22",user="edem",passwd="cisco")
shell = myparamiko_11.get_shell(ssh_client)

myparamiko_11.send_from_file(location="data_serialization\paramiko\challenge\\script",shell=shell)