from load_tester.requester import send_request
from load_tester.runner import run_test
if __name__ == "__main__":
    result = send_request("https://www.baidu.com")
    print(result)
    report = run_test("https://www.baidu.com", 10)
    print(report)

