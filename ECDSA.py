import time
import json
from ecdsa import SigningKey, VerifyingKey, NIST521p, BRAINPOOLP256r1, NIST192p, SECP256k1

start_time = time.perf_counter()

#c='NIST192p'
#c='NIST521p'
#c='SECP256k1'
c='BRAINPOOLP256r1'

# El usuario U genera su par de claves pubica y privada
sk = SigningKey.generate(curve=BRAINPOOLP256r1)
verifying_key_hex_string = sk.verifying_key.to_string().hex()
signing_key_hex_string = sk.to_string().hex()

# El usuario U firma el mensaje 
#sk = SigningKey.from_string(bytearray.fromhex(signing_key_hex_string))
text = "Esto es un mensaje de prueba para el algoritmo ECDSA"
#text = "La criptografia de curvas elipticas es un tema de gran relevancia en el ambito de la seguridad informatica, la ciberseguridad. El uso de curvas elipticas en criptografia ofrece ventajas como un mayor de nivel de seguridad con menores tamanos de claves y menores consumos de recursos computacionales. Por este motivo, el estudio de la criptografia de curvas elipticas y su implementacion en sistemas informaticos es un campo de gran interes y potencial para investigadores y profesionales del sector. El objetivo de este Trabajo de Fin de Grado es profundizar en el estudio de la criptografia de curvas elipticas, asi como una implementacion practica que nos permita analizar diferentes protocolos. En concreto, se estudiara la definicion y conceptos basicos y su aplicacion en diferentes cuerpos, asi como los protocolos mas comunes, como Diffie-Hellman, ECIES y ECDSA. Ademas de un posterior analisis de los diferentes tiempos de computacion de estos protocolos para analizar la eficiencia y el rendimiento de diferentes curvas y cuerpos. El analisis de los protocolos de una manera practica en Python permitira la realizacion de pruebas y analisis en un entorno de laboratorio. Los resultados obtenidos permitiran determinar que curvas y cuerpos son mas adecuados para su implementacion en diferentes aplicaciones o sistemas. Ademas, este TFG proporcionara una base solida para futuras investigaciones en el campo de la criptografia de curvas elipticas y su aplicacion en ciberseguridad."

tamañoClave = len(signing_key_hex_string)

signature = sk.sign(text.encode('utf-8'))
signature_hex_string = signature.hex()

# El usuario V verifica el mensaje emitido por U
#verifying_key = VerifyingKey.from_string(bytearray.fromhex(verifying_key_hex_string))
signature = bytearray.fromhex(signature_hex_string)
#verification_result = verifying_key.verify(signature, text.encode('utf-8'))
verification_result = sk.verifying_key.verify(signature, text.encode('utf-8'))

output = {
    "SigningKey_private": signing_key_hex_string,
    "VerificationKey_public": verifying_key_hex_string,
    "Signature": signature_hex_string,
    "VerificationResult": verification_result,
    "Curva": c,
    "SizeClavefirma": tamañoClave
}

json_output = json.dumps(output)

end_time = time.perf_counter()
execution_time = end_time - start_time

output_with_time = {
    "SigningKey_private": signing_key_hex_string,
    "VerificationKey_public": verifying_key_hex_string,
    "Signature": signature_hex_string,
    "VerificationResult": verification_result,
    "ExecutionTime": execution_time,
    "Curva": c,
    "SizeClavefirma": tamañoClave
}

json_output_with_time = json.dumps(output_with_time)

print()
print(json_output_with_time)
