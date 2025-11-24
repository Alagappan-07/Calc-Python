import os
import json
import sqlite3

def handle_user_input(user_input):
    # Bad pattern (illustrative only): command building
    cmd = f"echo {user_input}"          # concept: command injection risk
    print("Would run:", cmd)            # but we do NOT execute it

    # Bad pattern (illustrative only): SQL building
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    print("Would query:", query)        # but we do NOT run SQL

    # Safe parsing instead of pickle
    data = json.loads('{"demo": "safe"}')
    return data

print(handle_user_input("example"))
