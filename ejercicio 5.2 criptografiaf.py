import hashlib

m = hashlib.sha256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha256:    " + m.digest().hex())

m = hashlib.sha256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha256:    " + m.digest().hex())

m = hashlib.sha512()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","utf8"))
print("sha512:    " + m.digest().hex())