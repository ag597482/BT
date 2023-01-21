import hashlib
import uuid;
print(uuid.uuid4())
test_str = "d9920a5a883eb5da5a84aaffe592b68d"
result = hashlib.shake_256(test_str.encode()).hexdigest(6)
print(len(result))
print(result) 
print(len('5ad5fc805e27188440729cc1f9c9af59'))
