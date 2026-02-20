# 1. SQL Injection (via string formatting)
user_input = request.args.get('user')
query = f"SELECT * FROM users WHERE name = '{user_input}'"
cursor.execute(query)

# 2. Weak Cryptography (MD5 is insecure)
import hashlib
hash = hashlib.md5(password.encode()).hexdigest()  # Snyk flags MD5

# 3. Hardcoded Secret (Snyk detects this)
API_KEY = "sk-1234567890abcdef"  # Simulate a secret

# 4. Command Injection (dangerous use of input)
import os
filename = request.args.get('file')
os.system(f"cat {filename}")  # User controls system command

# 5. Insecure Deserialization
import pickle
data = pickle.loads(user_input)  # Risk of arbitrary code execution   
