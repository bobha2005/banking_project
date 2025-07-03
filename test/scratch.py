import bcrypt

password = b"hello"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
assert bcrypt.checkpw(b"hello", hashed)