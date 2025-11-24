# src/vul.py
import json

def handle_user_input(user_input):
    clean_input = str(user_input).strip()

    # Safe message
    message = f"Received input: {clean_input}"

    # Safe JSON output
    output_json = json.dumps({"status": "ok", "input": clean_input})

    return message, output_json
