import socket
# install library with: pip install pycryptodome
from Crypto.Util.number import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '127.0.0.1'
port = 1111

plaintext = bytes_to_long(b"secret-password")
random_value = bytes_to_long(b"random-val")
s.connect((LOCALHOST,port))

# generating public and private key
e = 65537
p = getPrime(1024)
q = getPrime(1024)

n = p * q

print("[*] Public key: " + str(n) + "\ne: " + str(e))
ciphertext = (plaintext**e) % n
print("[*] First ciphertext: " + str(ciphertext) + "\n")

random_value_enc = (random_value**e) % n
print("[*] Random value: " + str(random_value_enc) + "\n")

while True:
    # get r from verifier
    message = "getR," + str(e)
    s.send(message.encode())

    msg_received = s.recv(1024)
    msg_received = msg_received.decode()
    r = int(msg_received)

    print("[*] r value received from verifier: " + msg_received)

    # Sending enc to verifier
    enc = (random_value* plaintext**r) % n
    data = str(ciphertext) + "," + str(random_value_enc) + "," + str(enc) + "," + str(e) + "," + str(n) + "," + str(r)
    print("[*] Sending values to verifier\n")
    s.send(data.encode())
    
    doneMessage = s.recv(1024)
    doneMessage = doneMessage.decode()
    print(doneMessage)
    
    # breaking for demo
    s.close()
    break
s.close()