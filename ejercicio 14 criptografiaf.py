from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets
from Crypto.Random import get_random_bytes

elemento_diversificacion = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")

master_secret = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

keys = HKDF(master_secret, 32, elemento_diversificacion, SHA512, 1)

print("Clave key1:", bytearray(keys).hex())
