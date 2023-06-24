import sys
from tinyec import registry
import secrets
import json

import time

start_time = time.perf_counter()

def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]


#c='secp192r1'
#c ='secp256r1'
c='brainpoolP256r1' # curva a utilizar
curve = registry.get_curve('brainpoolP256r1')

Ka = secrets.randbelow(curve.field.n) # valor aleatorio secreto u
Kb = secrets.randbelow(curve.field.n) # valor aleatorio secreto v

X = Ka * curve.g #punto uG de la curva
output_X = {"x": compress(X)}

Y = Kb * curve.g #punto vG de la curva
output_Y = {"x": compress(Y)}


aliceSharedKey = Ka * Y # punto u(vG)
output_aliceSharedKey = {"x": compress(aliceSharedKey)}

bobSharedKey = Kb * X   # punto v(uG)
output_bobSharedKey = {"x": compress(bobSharedKey)}

tamañoClave = len(compress(aliceSharedKey))

output_equalSharedKeys = {"equal_shared_keys": aliceSharedKey == bobSharedKey} # punto u(vG) = v(uG)

output = {
    "X": output_X,
    "Y": output_Y,
    "AliceSharedKey": output_aliceSharedKey,
    "BobSharedKey": output_bobSharedKey,
    "EqualSharedKeys": output_equalSharedKeys,
    "Curve": c,
    "Sizeclave": tamañoClave
}

json_output = json.dumps(output)

end_time = time.perf_counter()
execution_time = end_time - start_time

output_with_time = {
    "X": output_X,
    "Y": output_Y,
    "AliceSharedKey": output_aliceSharedKey,
    "BobSharedKey": output_bobSharedKey,
    "EqualSharedKeys": output_equalSharedKeys,
    "ExecutionTime": execution_time,
    "Curva": c,
    "Sizeclave": tamañoClave
}

json_output_with_time = json.dumps(output_with_time)

print()
print(json_output_with_time)