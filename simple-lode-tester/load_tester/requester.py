import requests
import time


def send_request(url):
    start_time = time.time()

    try:
        response = requests.get(url)
        success = response.status_code == 200
    except Exception:
        success = False

    end_time = time.time()

    return {
        "success": success,
        "response_time": end_time - start_time
    }