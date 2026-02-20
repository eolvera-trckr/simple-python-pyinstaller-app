# 1. SQL Injection
user_input = request.args.get('user')
query = f"SELECT * FROM users WHERE name = '{user_input}'"
cursor.execute(query)

# 2. Hardcoded Non-Cryptographic Secret
API_KEY = "sk-1234567890abcdef"

# 3. Command Injection (dangerous use of input)
import os
filename = request.args.get('file')
os.system(f"cat {filename}")

# 4. Deserialization of Untrusted Data
import pickle
data = pickle.loads(user_input)   
