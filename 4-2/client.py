import socket
from utils import rsa_keygen, rsa_encode, rsa_decode, aes_keygen, aes_encode, aes_decode, aes_transform_key
import sys

if __name__ == "__main__":
    password = input("Enter password: ").encode()
    password = aes_transform_key(password)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 1234))

    # Stage 2
    try:
        public_key = aes_decode(password, sock.recv(1024))
    except:
        print("Permission denied!")
        sock.close()
        sys.exit(0)
    K_s = aes_keygen()
    sock.send(aes_encode(password, rsa_encode(public_key, K_s)))

    # Stage 4
    try:
        N_A = aes_decode(K_s, sock.recv(1024))
    except:
        print("Permission denied!")
        sock.close()
        sys.exit(0)
    N_B = aes_keygen()
    sock.send(aes_encode(K_s, N_A + N_B))

    # Stage 6
    try:
        N2 = aes_decode(K_s, sock.recv(1024))
    except:
        print("Permission denied!")
        sock.close()
        sys.exit(0)
    if N2 != N_B:
        print("Permission denied!")
        sock.close()
        sys.exit(0)
    print("common key: ", K_s)
