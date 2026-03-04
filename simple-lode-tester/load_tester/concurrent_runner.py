from concurrent.futures import ThreadPoolExecutor, as_completed
from load_tester.requester import send_request


def run_concurrent_test(url, total_requests, max_workers):
    success_count = 0
    total_time = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(send_request, url) for _ in range(total_requests)]

        for future in as_completed(futures):
            result = future.result()
            if result["success"]:
                success_count += 1
            total_time += result["response_time"]

    avg_time = total_time / total_requests if total_requests > 0 else 0

    return {
        "total_requests": total_requests,
        "success_count": success_count,
        "fail_count": total_requests - success_count,
        "avg_response_time": avg_time,
        "concurrency": max_workers
    }