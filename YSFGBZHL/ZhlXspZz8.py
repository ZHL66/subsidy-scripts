import json
import requests
import time
import threading
from datetime import datetime, time as dt_time

# 请求头信息
headers = {
    'Host': 'scene.cup.com.cn',
    'Cookie': 'route=be2997e80bebd668c45359ccc2f7cbec',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Sec-Fetch-Site': 'same-origin',
    'appNo': 'YJHXNP044125012',
    'channelNo': 'Q000101',
    'Sec-Fetch-Mode': 'cors',
    'token': 'bj_1b515bbd63681a3640d3b792ecaf64bb997504eef74b3f3c3f6683a97cd9063e_sh',
    'Origin': 'https://scene.cup.com.cn',
    'bankCode': '',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_6_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148  (com.unionpay.chsp) (cordova 4.5.4) (updebug 0) (version 1024) (UnionPay/1.0 CloudPay) (clientVersion 324) (language zh_CN) (languageFamily zh_CN) (upHtml) (walletMode 00)',
    'Referer': 'https://scene.cup.com.cn/gsp_front/2025/online?appNo=YJHXNP044125012&channelNo=Q000101',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br'
}

# 请求体
payload = {
    "areaCode": "350699",
    "longitude": "118.2660416666667",
    "latitude": "24.58871527777778",
    "acquireType": "1",
    "cateCode": "N02800",
    "activityId": "11",
    "engGrade": None,
    "coordType": "gcj02ll"
}

# 请求URL
url = 'https://scene.cup.com.cn/gfmnewoth/appback/couponAcquire'

# 请求间隔(秒)
REQUEST_INTERVAL = 0.1  # 更短的间隔以提高频率
# 线程数量
THREAD_COUNT = 10
# 锁用于控制输出
print_lock = threading.Lock()


def send_request(thread_id):
    """发送请求并在控制台输出结果"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]  # 精确到毫秒
    try:
        response = requests.post(url, headers=headers, json=payload)
        try:
            json_response = response.json()
            resp_msg = json_response.get("respMsg", "未知响应")
            with print_lock:
                print(f"[线程{thread_id}] {timestamp} - {resp_msg}")
        except ValueError:
            with print_lock:
                print(f"[线程{thread_id}] {timestamp} - 非JSON响应: {response.text}")
        return response

    except requests.exceptions.RequestException as e:
        with print_lock:
            print(f"[线程{thread_id}] {timestamp} - 请求异常: {str(e)}")
        return None
    except Exception as e:
        with print_lock:
            print(f"[线程{thread_id}] {timestamp} - 未知错误: {str(e)}")
        return None


def worker(thread_id):
    """工作线程函数"""
    while True:
        send_request(thread_id)
        time.sleep(REQUEST_INTERVAL)


def scheduled_sending():
    """定时发送请求"""
    print("等待到指定时间...")
    while True:
        now = datetime.now()
        # 检查是否到达8点
        if now.time() >= dt_time(7, 59, 58):
            print(f"开始发送请求 @ {now.strftime('%Y-%m-%d %H:%M:%S')}")
            break
        time.sleep(0.01)  # 每10ms检查一次时间

    # 创建并启动工作线程
    threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=worker, args=(i + 1,))
        t.daemon = True
        t.start()
        threads.append(t)

    # 等待所有线程完成（实际上会一直运行）
    for t in threads:
        t.join()


if __name__ == '__main__':
    # 启动定时发送线程
    scheduler_thread = threading.Thread(target=scheduled_sending)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    # 主线程保持运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序已停止")