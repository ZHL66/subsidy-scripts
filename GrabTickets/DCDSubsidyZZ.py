import time
import requests
import brotli
from datetime import datetime, timedelta
import threading
import json
import sys

# 创建会话对象
session = requests.Session()


def send_request():
    """发送API请求并返回响应时间"""
    start_time = time.time()  # 记录开始时间
    current_timestamp = int(time.time())

    # 请求URL
    url = "https://api5-normal-sinfonlineb.dcarapi.com/motor/goods/api/v1/sku_order/create_batch_gov_consume"

    # 查询参数 (使用新提供的参数)
    params = {
        "device_id": "3449621491233338",
        "os_version": "18.6",
        "iid": "986720338984344",
        "app_name": "automobile",
        "ac": "WIFI",
        "cpu_score": "12",
        "total_memory": "5990924288",
        "selected_district_name": "",
        "ssmix": "a",
        "version_code": "8.7.1",
        "channel": "App Store",
        "overall_score": "11.45259952545166",
        "selected_city_name": "",
        "am_time": current_timestamp,
        "content_sort_mode": "0",
        "gps_city_name": "漳州",
        "app_enter_from": "",
        "update_version_code": "87105",
        "device_platform": "iphone",
        "device_type": "iphone 14",
        "user_id": "1823439612291392",
        "city_name": "漳州",
        "aid": "36",
        "district_name": "平和",
        "scale": "3",
        "resolution": "1170 * 2532",
        "gps_district_name": "平和"
    }

    # Cookie信息 (使用新提供的值)
    cookies = {
        'passport_csrf_token': '8bba881a3420563534dd42bf03d50d12',
        'passport_csrf_token_default': '8bba881a3420563534dd42bf03d50d12',
        'd_ticket': '8e6bd0e60416fb7dd315b55c774d2c7852471',
        'is_staff_user': 'false',
        'n_mh': 'RgbbQ52lJbGj9AXg4m7dfQCZpIUVCKRS9Lxgw-Wy4Ko',
        'passport_mfa_token': 'CjYepgMUdWPpOXMtc52286LqkeKxy89L3ADi1Xq9ZeAhUySxAq%2BRgn%2BFHJ5iVMWB9x%2Blf9EEy8caSgo8AAAAAAAAAAAAAE9pZHzaNKKa8LcddNNKzGz%2F90AY3kCfnkODbaK98VZ2LD3kdUzNWmXjUwRbiIxGT4JGEKbk%2Bg0Y9rHRbCACIgEDYTLC6A%3D%3D',
        'sessionid': '2655c92e9183398872a8898c9daf615b',
        'sessionid_ss': '2655c92e9183398872a8898c9daf615b',
        'sid_guard': '2655c92e9183398872a8898c9daf615b%7C1756488779%7C5184000%7CTue%2C+28-Oct-2025+17%3A32%3A59+GMT',
        'sid_tt': '2655c92e9183398872a8898c9daf615b',
        'uid_tt': '1cfa1199786be1f0a30e3dc915a5642a',
        'uid_tt_ss': '1cfa1199786be1f0a30e3dc915a5642a',
        'session_tlb_tag': 'sttt%7C17%7CJlXJLpGDOYhyqImMna9hW__________8DTOgajLkA8ddVQfF3QC46yjf86AfMKXTHrP32-04wkk%3D',
        'install_id': '986720338984344',
        'ttreq': '1$815d2676a4905d100962be278418abe04e120301',
        'odin_tt': '1d6bba574128287378dc19d7b9becac12a8e423157a1164334457e985152e835a5647d86cd313de5b1f18dc9e5cc40e01394987339326f274fa64be28967ab635caa3dde5f5b4f28206f5878e268f0f4'
    }

    # 请求头 (使用新提供的值)
    headers = {
        'Host': 'api5-normal-sinfonlineb.dcarapi.com',
        'Connection': 'keep-alive',
        'Content-Length': '489',
        'X-SS-STUB': 'AB8EB1D1791EE3421120C7B267508502',
        'x-vc-bdturing-sdk-version': '3.6.4',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-SS-Cookie': 'odin_tt=1d6bba574128287378dc19d7b9becac12a8e423157a1164334457e985152e835a5647d86cd313de5b1f18dc9e5cc40e01394987339326f274fa64be28967ab635caa3dde5f5b4f28206f5878e268f0f4; install_id=986720338984344; ttreq=1$815d2676a4905d100962be278418abe04e120301; session_tlb_tag=sttt%7C17%7CJlXJLpGDOYhyqImMna9hW__________8DTOgajLkA8ddVQfF3QC46yjf86AfMKXTHrP32-04wkk%3D; d_ticket=8e6bd0e60416fb7dd315b55c774d2c7852471; is_staff_user=false; n_mh=RgbbQ52lJbGj9AXg4m7dfQCZpIUVCKRS9Lxgw-Wy4Ko; passport_mfa_token=CjYepgMUdWPpOXMtc52286LqkeKxy89L3ADi1Xq9ZeAhUySxAq%2BRgn%2BFHJ5iVMWB9x%2Blf9EEy8caSgo8AAAAAAAAAAAAAE9pZHzaNKKa8LcddNNKzGz%2F90AY3kCfnkODbaK98VZ2LD3kdUzNWmXjUwRbiIxGT4JGEKbk%2Bg0Y9rHRbCACIgEDYTLC6A%3D%3D; sessionid=2655c92e9183398872a8898c9daf615b; sessionid_ss=2655c92e9183398872a8898c9daf615b; sid_guard=2655c92e9183398872a8898c9daf615b%7C1756488779%7C5184000%7CTue%2C+28-Oct-2025+17%3A32%3A59+GMT; sid_tt=2655c92e9183398872a8898c9daf615b; uid_tt=1cfa1199786be1f0a30e3dc915a5642a; uid_tt_ss=1cfa1199786be1f0a30e3dc915a5642a; passport_csrf_token=8bba881a3420563534dd42bf03d50d12; passport_csrf_token_default=8bba881a3420563534dd42bf03d50d12',
        'tt-request-time': str(current_timestamp * 1000),
        'User-Agent': 'AutoMobile 8.7.1 rv:8.7.1.05 (iPhone; iOS 18.6; zh_CN) Cronet',
        'x-Tt-Token': '002655c92e9183398872a8898c9daf615b03c8e7630ab6bbb8113bc88ec6adfa56797ab64c30a132db255f58ad43ca996ebd71dba4d885d7af5a5f9ba1cffcc802cba7b0de9639dc648fbd5ac2cce400b28f700c0bc1c9fe7987c45995e1b9ecfa212--0a490a20155ba477b893a6eb6c4e39886e51099c5d93c3d73440badd5d14acfa22e577791220c17b5c99f5a2b79e34723fb7dd85c67cdb279a2c0fcb2981bfccc7e9e451205518f6b4d309-3.0.1',
        'sdk-version': '2',
        'passport-sdk-version': '5.20.8-alpha.64-anniex',
        'x-bd-kmsv': '1',
        'X-SS-DP': '36',
        'x-tt-trace-id': '00-f6ea3b920dc41699798323a1ac500024-f6ea3b920dc41699-01',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Argus': 'F7RiE2hoHL7fTGwZYhcLaFDzrzneCYXF0urPaRvrez2n/8VqYiKQNIbfWv4E+VzERyQo6wt5mCxdt6LZc7bdwFTkIfQU1kMZCFB+OqGaNfuZ6pCfDKXssFKL+P0x7hAmKwYOxqdGeCbAvjeHRBUYAV4O/uBnDhIbNjlb+sjuUUz7PNCNeJB4ECF92LlYb02jNrs4iI7O4gz4BBMHYPwzZ14uEdCtO2OfQnpOfiLAhxB4+y6In51qLVUyGVAuERuMZvxt6IW1U6DY1DYhCzpMmgogDPqX567j6LnOj0fnYvgyyhr2e1n4AqeBWRGTGmWnjSJm+fxBXvSy55AGgWCKtqE5',
        'X-Gorgon': '8404202600009efae9c8cdcb3b59fb4858dac272eca857f7d34f',
        'X-Helios': 'juqKGNM+4ElPxoPXykjKhokFCF3dCBOI0/M6SfyhTg83YTHI',
        'X-Khronos': str(current_timestamp),
        'X-Ladon': 'dHcBOGSX8gCA9sQiIQtiBhi41d6YlKdxX0nZZ+T3mjHKfK6G',
        'X-Medusa': '8eWxaAUN7pIlMm1TJM95GKUq0HBgpwEDnLI7a6WovwsAKhAY1YjQAlcluvT+rF/t7CQ8LBNVr4K0NFnZsSZh0Z4S8l6AJ6ZeXai6zYuJZwAaA42RoTplOVOBtKa5Acng8FMA3FNZg8ZOHu2GZpNyf0QtIHW1sQHkHamCFWyv/vFwds40sJsIniHukY0jYmoi3skOzPH4sC7DuFldzHGovXI95Mt6NJZuJxFBYonJ7Kano86QJNzlnoFtWfVEyisCf0ONVEur6aZKVzn6SuWYOml1AYoG59QmZftYjjBodTpFTWgqHP+kAYogXu8/e/MZO2MtvSwsC268McKhMun3hhYagHlbYXN9RqF3SvzF+QL1gYiI1ml0Kpy8hgnzEN76UakKxtieR7xsapk+xUC9G4E/KQkTn5DqhKicc058wC5fs+PYfeBWDwgqU4ZvrfTiOmpD3JGNNAePxFAQqRE81cxa5XrQx/2x0WWU7xQPkYvjOTtjJkHeBSc5VnQIn+209MPZ3vrSSjaonuVscYensCKLCjGRHgDtqC9OtdK0XNzBmEV+z9AGIsD0KRMZ9UxIuN4u0ockIQSJLc699MCRRhhcJWXDNnkQTlP9hDknbfTfZ+GkbnHmDeQIWJ3pv2fgK7VWB7ueImUTb0/xQdUXVgdVeKKal4QzT/xKUI73ohmWKkGOf6bimxExkShpmk0kjEB/cv/O7aQqPZaDapGWWv319d9aRZPZHAMBen9fuqUMObF3UVLFPRa9VX7t2pSBsqDJ3UztDHIh4cdSbS8YkJ5QfdSeAj6TG0GB6rHuEUGD0J9Y1vY5Abw+lrU7NkEs+sV/N0pTY3Q43qxgyk/1M9E9JxL/+ccO//nHDscw',
        'Cookie': '; '.join([f'{k}={v}' for k, v in cookies.items()])
    }

    # 表单数据 (使用新提供的值)
    form_data = {
        'customer': '张福清',
        'link_source': 'dcd_page_category-category_top_tab_gov_coupon_govconsumecoupon',
        'mobile_token': '@KlWLKx2o7Ngw5NULsAc+FlkRK06o8/bl37TCQKj8HqP67a8Y0hHEZ7BP3vXQn6/Z',
        'mobile_token_type': '0',
        'order_title': '汽车消费补贴发放中',
        'sku_list': '[{"sku_version":"7541350043056459801","sku_id":"20522307"}]',
        'vercode': '',
        'zt': 'dcd_ncec_page_gov_consume_coupon_landing-coupon_module_get_coupon'
    }

    def decode_response(response):
        """处理API响应，自动解压并解码内容"""
        try:
            content_encoding = response.headers.get('Content-Encoding', '').lower()

            if 'br' in content_encoding:
                decoded_content = brotli.decompress(response.content)
                return decoded_content.decode('utf-8')
            elif 'gzip' in content_encoding:
                return response.text
            else:
                return response.content.decode('utf-8')
        except Exception as e:
            print(f"解码响应时出错: {e}")
            try:
                return response.content.decode('utf-8')
            except:
                return response.text

    try:
        # 发送POST请求
        response = session.post(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            data=form_data,
            timeout=10  # 设置合理的超时时间
        )

        # 记录结束时间
        end_time = time.time()
        request_duration = (end_time - start_time) * 1000  # 毫秒

        # 输出响应信息
        print(f"状态码: {response.status_code}")
        print(f"请求耗时: {request_duration:.2f} 毫秒")

        # 解码响应内容
        decoded_content = decode_response(response)

        # 尝试解析JSON
        try:
            json_data = json.loads(decoded_content)
            # 精简输出
            print("响应摘要:")
            print(f"  err_no: {json_data.get('err_no')}")
            print(f"  err_tips: {json_data.get('err_tips', 'N/A')}")
            print(f"  prompts: {json_data.get('prompts', 'N/A')}")

            # 检查是否成功
            if json_data.get("err_no") == 0:
                print("✅ 请求成功！")
            else:
                print("❌ 请求失败")

        except json.JSONDecodeError:
            print("响应内容:")
            print(decoded_content[:500] + "..." if len(decoded_content) > 500 else decoded_content)

        return request_duration

    except requests.exceptions.Timeout:
        end_time = time.time()
        error_duration = (end_time - start_time) * 1000
        print(f"⚠️ 请求超时 (耗时: {error_duration:.2f} 毫秒)")
        return error_duration

    except requests.exceptions.TooManyRedirects:
        end_time = time.time()
        error_duration = (end_time - start_time) * 1000
        print(f"⚠️ 重定向过多 (耗时: {error_duration:.2f} 毫秒)")
        return error_duration

    except requests.exceptions.RequestException as e:
        end_time = time.time()
        error_duration = (end_time - start_time) * 1000
        print(f"⚠️ 请求失败: {e} (耗时: {error_duration:.2f} 毫秒)")
        return error_duration

    except Exception as e:
        end_time = time.time()
        error_duration = (end_time - start_time) * 1000
        print(f"⚠️ 其他错误: {e} (耗时: {error_duration:.2f} 毫秒)")
        return error_duration


def send_request_thread(thread_id):
    """线程函数，用于发送请求"""
    thread_name = f"线程-{thread_id}"
    print(f"\n=== {thread_name} 开始 ===")

    # 打印开始时间
    start_time = time.time()
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"开始时间: {formatted_time}")

    # 发送请求
    duration = send_request()

    # 打印结束时间
    end_time = time.time()
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(f"结束时间: {formatted_time}")
    print(f"总耗时: {(end_time - start_time) * 1000:.2f} 毫秒")

    print(f"=== {thread_name} 结束 ===")
    return duration


def wait_until(target_hour, target_minute, target_second, target_millisecond=900):
    """精确等待到北京时间的目标时间"""
    while True:
        # 获取当前北京时间
        now = datetime.utcnow() + timedelta(hours=8)
        target_time = now.replace(hour=target_hour, minute=target_minute,
                                  second=target_second, microsecond=target_millisecond * 1000)

        # 如果当前时间已过目标时间，设定为明天的目标时间
        if now >= target_time:
            print("\n\n🚀 时间到！开始抢券...")
            return

        # 计算需要等待的秒数
        wait_seconds = (target_time - now).total_seconds()

        if wait_seconds > 0:
            # 转换为小时、分钟、秒、毫秒
            hours, remainder = divmod(wait_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            milliseconds = (seconds - int(seconds)) * 1000
            seconds = int(seconds)

            # 清空行并显示倒计时
            sys.stdout.write("\r")
            sys.stdout.write(
                f"⏳ 距离抢券时间: {int(hours):02d}:{int(minutes):02d}:{seconds:02d}.{int(milliseconds):03d} ")
            sys.stdout.flush()

            # 每0.1秒更新一次时间显示
            time.sleep(0.1)
        else:
            print("\n\n🚀 时间到！开始抢券...")
            return


def animated_spinner(duration, message="准备中"):
    """显示动画加载指示器"""
    spinner = ['|', '/', '-', '\\']
    start_time = time.time()
    i = 0

    while time.time() - start_time < duration:
        # 更新动画
        sys.stdout.write(f"\r{message} {spinner[i % len(spinner)]}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)


# 主程序
if __name__ == "__main__":
    print("🎯 汽车消费券自动抢券程序")
    print("⏰ 计划时间: 每天 08:59:59.900 北京时间\n")

    # 设置抢券时间（北京时间早上8:59:59.900）
    GRAB_HOUR = 8
    GRAB_MINUTE = 59
    GRAB_SECOND = 59
    GRAB_MILLISECOND = 900  # 900毫秒

    # 等待到目标时间
    wait_until(GRAB_HOUR, GRAB_MINUTE, GRAB_SECOND, GRAB_MILLISECOND)

    # 准备动画
    animated_spinner(0.1, "即将开始抢券")  # 缩短动画时间为0.1秒

    print("\n开始发送请求...")
    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

    # 使用多线程并行发送请求
    threads = []
    durations = []

    # 创建并启动线程 - 4个线程，间隔50毫秒
    for i in range(6):
        thread = threading.Thread(target=send_request_thread, args=(i + 1,))
        thread.start()
        threads.append(thread)
        time.sleep(0.05)  # 50毫秒间隔

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 重新组织代码以收集耗时数据
    durations = []
    for i in range(6):
        start_time = time.time()
        duration = send_request_thread(i + 1)
        durations.append(duration)
        if i < 3:  # 最后一次不需要等待
            # 计算需要等待的时间
            elapsed = (time.time() - start_time) * 1000
            wait_time = max(0, 50 - elapsed) / 1000  # 50毫秒间隔
            if wait_time > 0:
                time.sleep(wait_time)

    # 打印性能统计
    if durations:
        avg_duration = sum(durations) / len(durations)
        max_duration = max(durations)
        min_duration = min(durations)
        print(f"\n请求耗时统计:")
        print(f"  平均耗时: {avg_duration:.2f} 毫秒")
        print(f"  最大耗时: {max_duration:.2f} 毫秒")
        print(f"  最小耗时: {min_duration:.2f} 毫秒")

    print("\n所有请求完成！")
    print(f"结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

    # 显示结果后暂停，防止窗口立即关闭
    print("\n按Enter键退出...")
    input()