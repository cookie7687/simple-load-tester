# from requester import send_request
from load_tester.requester import send_request



def run_test(url, times):
    success_count = 0
    total_time = 0

    for _ in range(times):
        result = send_request(url)
        if result["success"]:
            success_count += 1
        total_time += result["response_time"]

    avg_time = total_time / times if times > 0 else 0

    return {
        "total_requests": times,
        "success_count": success_count,
        "fail_count": times - success_count,
        "avg_response_time": avg_time
    }