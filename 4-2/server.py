import socket
from utils import rsa_keygen, rsa_encode, rsa_decode, aes_keygen, aes_encode, aes_decode, aes_transform_key
import sys

password = b'password'
password = aes_transform_key(password)

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 1234))
    while (True):
        sock.listen(1)
        conn, addr = sock.accept()

        # Stage 1
        public_key, private_key = rsa_keygen()
        conn.send(aes_encode(password, public_key))

        # Stage 3
        try:
            K_s = rsa_decode(private_key, aes_decode(password, conn.recv(1024)))
        except:
            print("Permission denied!")
            conn.close()
            continue
        N_A = aes_keygen()
        conn.send(aes_encode(K_s, N_A))

        # Stage 5
        try:
            N = aes_decode(K_s, conn.recv(1024))
        except:
            print("Permission denied!")
            conn.close()
            continue
        N1 = N[:16]
        N2 = N[16:]
        if N1 == N_A:
            conn.send(aes_encode(K_s, N2))
        else:
            print("Permission denied!")
            conn.close()
            continue
        print("common key: ", K_s)
