from cryptography.hazmat.primitives import hashes
import time

nonce = 0
minzeroes = 6

start_time = time.time()  # Start timing

while True:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(b"Alice->Bob, 5 BTC   Carol->Dave, 2 BTC ...")
    s = bytearray(str(nonce), encoding='ISO-8859-1')
    digest.update(s)
    b = digest.finalize()
    h = b.hex()
    print("Iteration: %3d" % nonce, "Hash: %s" % h)

    nonce += 1

    if str(h)[:minzeroes] == '0' * minzeroes:  # Changed to generalize the check for any number of zeroes
        print(f"Hash starting with at least {minzeroes} zeroes found!!!")
        break

end_time = time.time()  # End timing
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")
