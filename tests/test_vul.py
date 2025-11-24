import json

def handle_user_input(user_input):
    clean_input = str(user_input).strip()

    # Safe simulated message
    message = f"Received: {clean_input}"

    # Safe JSON output
    data = {"status": "ok", "input": clean_input}
    json_output = json.dumps(data)

    return message, json_output   # ✅ returns two values
