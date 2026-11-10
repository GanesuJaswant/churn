# API development and testing scratchpad
import requests

def test_local_api():
    base_url = "http://127.0.0.1:8000"
    try:
        health_res = requests.get(f"{base_url}/health")
        print("Health status:", health_res.status_code, health_res.json())
        meta_res = requests.get(f"{base_url}/metadata")
        print("Metadata:", meta_res.status_code, meta_res.json())
    except Exception as e:
        print("API not running or connection error:", e)

if __name__ == "__main__":
    test_local_api()
