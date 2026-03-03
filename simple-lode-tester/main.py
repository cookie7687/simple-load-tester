from load_tester.requester import send_request

if __name__ == "__main__":
    result = send_request("https://www.baidu.com")
    print(result)