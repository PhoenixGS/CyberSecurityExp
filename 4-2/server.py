import socket
from utils import rsa_keygen, rsa_encode, rsa_decode, aes_keygen, aes_encode, aes_decode
import sys

password = b'passwordpassword'

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 1234))
    sock.listen(1)
    conn, addr = sock.accept()

    # Stage 1
    public_key, private_key = rsa_keygen()
    print("public key: ", public_key)
    conn.send(aes_encode(password, public_key))

    # Stage 3
    K_s = rsa_decode(private_key, aes_decode(password, conn.recv(1024)))
    print("common key: ", K_s)
    N_A = aes_keygen()
    print("N_A: ", N_A)
    conn.send(aes_encode(K_s, N_A))

    # Stage 5
    N = aes_decode(K_s, conn.recv(1024))
    N1 = N[:16]
    N2 = N[16:]
    if N1 == N_A:
        conn.send(aes_encode(K_s, N2))
    else:
        print("Permission denied!")
        conn.close()
        sys.exit(0)
    print("common key: ", K_s)