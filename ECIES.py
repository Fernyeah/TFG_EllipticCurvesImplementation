# #pip install eciespy
import time
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

import binascii
import json

start_time = time.perf_counter()

eth_k = generate_eth_key()
sk_hex = eth_k.to_hex()  # hex string
pk_hex = eth_k.public_key.to_hex()  # hex string
data = b'Esto es un mensaje de prueba para el algoritmo ECIES'
#data = b'La criptografia de curvas elipticas es un tema de gran relevancia en el ambito de la seguridad informatica, la ciberseguridad. El uso de curvas elipticas en criptografia ofrece ventajas como un mayor de nivel de seguridad con menores tamanos de claves y menores consumos de recursos computacionales. Por este motivo, el estudio de la criptografia de curvas elipticas y su implementacion en sistemas informaticos es un campo de gran interes y potencial para investigadores y profesionales del sector. El objetivo de este Trabajo de Fin de Grado es profundizar en el estudio de la criptografia de curvas elipticas, asi como una implementacion practica que nos permita analizar diferentes protocolos. En concreto, se estudiara la definicion y conceptos basicos y su aplicacion en diferentes cuerpos, asi como los protocolos mas comunes, como Diffie-Hellman, ECIES y ECDSA. Ademas de un posterior analisis de los diferentes tiempos de computacion de estos protocolos para analizar la eficiencia y el rendimiento de diferentes curvas y cuerpos. El analisis de los protocolos de una manera practica en Python permitira la realizacion de pruebas y analisis en un entorno de laboratorio. Los resultados obtenidos permitiran determinar que curvas y cuerpos son mas adecuados para su implementacion en diferentes aplicaciones o sistemas. Ademas, este TFG proporcionara una base solida para futuras investigaciones en el campo de la criptografia de curvas elipticas y su aplicacion en ciberseguridad.'

encrypted = encrypt(pk_hex, data)
encrypted_hex = binascii.hexlify(encrypted).decode()

secp_k = generate_key()
sk_bytes = secp_k.secret  # bytes
pk_bytes = secp_k.public_key.format(True)  # bytes
decrypted = decrypt(sk_bytes, encrypt(pk_bytes, data))
decrypted_str = decrypted.decode()

tamañoEnc = len(sk_hex)


output = {
    "EncryptionPublickey": sk_hex,
    "DecryptionPrivatekey": pk_hex,
    "Message": data.decode(),
    "Encrypted": encrypted_hex,
    "OriginalMessage": decrypted_str,
    "Curva": 'secp256k1',
    "SizeClaveCifrado": tamañoEnc
}

json_output = json.dumps(output)

end_time = time.perf_counter()
execution_time = end_time - start_time

output_with_time = {
    "EncryptionPublickey": sk_hex,
    "DecryptionPrivatekey": pk_hex,
    "Message": data.decode(),
    "Encrypted": encrypted_hex,
    "OriginalMessage": decrypted_str,
    "ExecutionTime": execution_time,
    "Curva": 'secp256k1',
    "SizeClaveCifrado": tamañoEnc
}

json_output_with_time = json.dumps(output_with_time)

print()
print(json_output_with_time)