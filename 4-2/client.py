import socket
from utils import rsa_keygen, rsa_encode, rsa_decode, aes_keygen, aes_encode, aes_decode
import sys

if __name__ == "__main__":
    password = b'passwordpassword'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 1234))

    # Stage 2
    public_key = aes_decode(password, sock.recv(1024))
    print("public key: ", public_key)
    K_s = aes_keygen()
    print("common key: ", K_s)
    sock.send(aes_encode(password, rsa_encode(public_key, K_s)))

    # Stage 4
    N_A = aes_decode(K_s, sock.recv(1024))
    print("N_A: ", N_A)
    N_B = aes_keygen()
    sock.send(aes_encode(K_s, N_A + N_B))

    # Stage 6
    N2 = aes_decode(K_s, sock.recv(1024))
    if N2 != N_B:
        print("Permission denied!")
        sock.close()
        sys.exit(0)
    print("common key: ", K_s)
