import json
import requests
import time
import threading
from datetime import datetime, time as dt_time

# 从配置文件读取
with open("config/zzxbxfz95.json", "r", encoding="utf-8") as f:
    config = json.load(f)

url = config["url"]
headers = config["headers"]
payload = config["payload"]

# 定时时间
schedule_cfg = config.get("schedule", {"hour": 7, "minute": 59, "second": 58})
TARGET_TIME = dt_time(
    schedule_cfg["hour"], schedule_cfg["minute"], schedule_cfg["second"]
)

# 请求间隔(秒)
REQUEST_INTERVAL = 0.1
# 线程数量
THREAD_COUNT = 10
# 锁用于控制输出
print_lock = threading.Lock()


def send_request(thread_id):
    """发送请求并在控制台输出结果"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
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
    print(f"等待到指定时间 {TARGET_TIME} ...")
    while True:
        now = datetime.now()
        if now.time() >= TARGET_TIME:
            print(f"开始发送请求 @ {now.strftime('%Y-%m-%d %H:%M:%S')}")
            break
        time.sleep(0.01)

    threads = []
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=worker, args=(i + 1,))
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=scheduled_sending)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序已停止")