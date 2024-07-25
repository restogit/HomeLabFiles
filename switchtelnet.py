import getpass
import telnetlib

HOST = "ip-address-here
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"password\n")
tn.write(b"conf t\n")

# Adding for-loop to create 5 VLANs
for v in range(2,6):
    tn.write(b"vlan " + str(v).encode('ascii') + b"\n")
    tn.write(b"name VLAN_" + str(v).encode('ascii') + b"\n")
    
tn.write(b"end\n")

# Getting confirmation that VLANs were created
tn.write(b"show vlan brief\n")

tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
