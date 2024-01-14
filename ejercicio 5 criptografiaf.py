import hashlib

m = hashlib.sha3_224()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha3_224:    " + m.digest().hex())

m = hashlib.sha3_256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha3_256:    " + m.digest().hex())

