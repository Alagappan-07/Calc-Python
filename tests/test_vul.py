import json
from src.vul import handle_user_input  # ✅ corrected module name

def test_handle_user_input_returns_tuple():
    message, output_json = handle_user_input("hello")
    assert isinstance(message, str)
    assert isinstance(output_json, str)

def test_json_structure():
    _, output_json = handle_user_input("world")
    parsed = json.loads(output_json)
    assert parsed["status"] == "ok"
    assert parsed["input"] == "world"

def test_input_sanitization():
    message, _ = handle_user_input("   spaced   ")
    assert "spaced" in message
