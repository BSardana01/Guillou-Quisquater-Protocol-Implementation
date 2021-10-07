import socket
import random
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '127.0.0.1'
port = 1111

server_socket.bind((LOCALHOST,port))
server_socket.listen(5)

print("Verifer started...")

client_sockets,addr=server_socket.accept()
while True:
    msg_received = client_sockets.recv(4096)
    msg_received = msg_received.decode()
    message = msg_received.split(',')

    # sending random value to prover
    if(message[0] == "getR"):
        r = random.randint(1, int(message[1]))
        r = str(r)
        print("[*] Sending r to prover: " + r)
        client_sockets.send(r.encode("ascii"))

    # getting values from prover
    else:
        ciphertext = int(message[0])
        random_val_enc = int(message[1])
        enc = int(message[2])
        e = int(message[3])
        n = int(message[4])
        r = int(message[5])

        print("[*] Ciphertexts and enc value received from prover\n Verifying...\n")
        firstVal = (enc**e) % n
        secondVal = (random_val_enc*ciphertext**r) % n

        print("[*] (enc**e) % n: " + str(firstVal))
        print("\n[*] (random_val_enc*ciphertext**r) % n: " + str(secondVal))

        if firstVal == secondVal:
            success = "Verified Successfully!"
            client_sockets.send(success.encode("ascii"))
        else:
            failure = "Not Verified!"
            client_sockets.send(failure.encode("ascii"))
            
        # breaking for demo
        client_sockets.close()
        break

client_sockets.close()