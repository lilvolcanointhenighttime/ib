from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

# Generation private_key
def generate_private_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key

# Generation publick_key_pem
def generate_public_key_pem(private_key):
    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return public_key_pem

# Loading publick_key_pem to use
def load_public_key_pem(public_key_pem):    
    member_public_key = serialization.load_pem_public_key(
        public_key_pem,
        backend=default_backend()
    )
    return member_public_key

# Encrypting message
def encrypt_message(message, member_public_key):
    message_encrypted = member_public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return message_encrypted

# Decrypting message
def decrypt_message(message, private_key):
    message_decrypted = private_key.decrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
    )
    return message_decrypted