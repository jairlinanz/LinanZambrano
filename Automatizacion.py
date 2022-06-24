from pdb import line_prefix
from pydoc import importfile
import telnetlib
import getpass

def seguridad():

    tn1.write(b'configure terminal\n')    
    tn1.write(b'service password-encryption\n')
    tn1.write(b'security passwords min-length 12\n')
    tn1.write(b'banner motd *** "ADVERRTENCIA: Si no es personal utorizado, favor retirarse. El ingreso no autorizado a este dispositivo conllevara accione legales" ***\n')

    tn1.write(b'username AdminTI privilege 15 secret Sen@grd2236881\n')

    tn1.write(b'username TecnicoTI privilege 4 secret Sen@grd2236881\n')

    tn1.write(b'privilege exec level 4 configure terminal\n')

    tn1.write(b'privilege exec level 4 show running\n')
    tn1.write(b'privilege exec all level 4 debug\n')
    tn1.write(b'privilege exec all level 4 undebug\n')

    tn1.write(b'login block-for 120 attempts 2 within 60\n')
    tn1.write(b'login on-success log\n')
    tn1.write(b'login on-failure log\n')

    tn1.write(b'ip domain-name sena.edu.co\n')
    tn1.write(b'crypto key generate rsa general-keys modulus 2048\n')
    tn1.write(b'ip ssh version 2\n')
    tn1.write(b'ip ssh authentication-retries 2\n')
    tn1.write(b'ip ssh time-out 120\n')

    tn1.write(b'line console 0\n')
    tn1.write(b'login local\n')
    tn1.write(b'exec-timeout 4 30\n')

    tn1.write(b'line vty 0 4\n')
    tn1.write(b'login local\n')
    tn1.write(b'exec-timeout 4 30\n')
    tn1.write(b'transport input ssh\n')

    tn1.write(b'line aux 0\n')
    tn1.write(b'login local\n')
    tn1.write(b'exec-timeout 4 30\n')
    tn1.write(b'exit\n')

    tn1.write(b'secure boot-image\n')
    tn1.write(b'secure boot-config\n')
    tn1.write(b'end\n')
    tn1.write(b'wr\n')
    print(tn1.read_all().decode('ascii'))

ruta = ''
HOST1 = "200.100.10.1"
HOST2 = "200.100.10.2"
HOST3 = "200.100.20.2"
HOST4 = "200.100.30.2"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn1 = telnetlib.Telnet(HOST1)
tn2 = telnetlib.Telnet(HOST2)
tn3 = telnetlib.Telnet(HOST3)
tn4 = telnetlib.Telnet(HOST4)

tn1.read_until(b"Username: ")
tn1.write(user.encode('ascii') + b"\n")
if password:
    tn1.read_until(b"password: ")
    tn1.write(password.encode('ascii') + b"\n")
seguridad()

tn2.read_until(b"Username: ")
tn2.write(user.encode('ascii') + b"\n")
if password:
    tn2.read_until(b"password: ")
    tn2.write(password.encode('ascii') + b"\n")
seguridad()

tn3.read_until(b"Username: ")
tn3.write(user.encode('ascii') + b"\n")
if password:
    tn3.read_until(b"password: ")
    tn3.write(password.encode('ascii') + b"\n")
seguridad()

tn4.read_until(b"Username: ")
tn4.write(user.encode('ascii') + b"\n")
if password:
    tn4.read_until(b"password: ")
    tn1.write(password.encode('ascii') + b"\n")
seguridad()
