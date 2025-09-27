import time
import requests
import brotli
from datetime import datetime
import threading
import json

# 创建会话对象
session = requests.Session()


def send_request():
    """发送API请求并返回响应时间"""
    start_time = time.time()  # 记录开始时间
    current_timestamp = int(time.time())

    # 请求URL
    url = "https://api5-normal-sinfonlineb.dcarapi.com/motor/goods/api/v1/sku_order/create_batch_gov_consume"

    # 查询参数
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
        "selected_city_name": "漳州",
        "am_time": current_timestamp,
        "content_sort_mode": "0",
        "gps_city_name": "厦门",
        "app_enter_from": "",
        "update_version_code": "87105",
        "device_platform": "iphone",
        "device_type": "iphone 14",
        "user_id": "1823439612291392",
        "city_name": "漳州",
        "aid": "36",
        "district_name": "翔安",
        "scale": "3",
        "resolution": "1170 * 2532",
        "gps_district_name": "翔安"
    }

    # Cookie信息
    cookies = {
        'passport_csrf_token': 'e08704ca15a2a2d6670ae788c283002e',
        'passport_csrf_token_default': 'e08704ca15a2a2d6670ae788c283002e',
        'MONITOR_WEB_ID': '87898f55-1008-40d1-a5de-340659085a66',
        'd_ticket': '0afbfd8e43280faa9c73d851d6c5145852471',
        'is_staff_user': 'false',
        'n_mh': 'RgbbQ52lJbGj9AXg4m7dfQCZpIUVCKRS9Lxgw-Wy4Ko',
        'passport_mfa_token': 'CjYEGupIZbjL6nNUkmNary%2BGXLkRFoZdD%2Fi4FxugyoWz75MULIwVFOWSVvhBS%2F2WgLLetmskg%2BIaSgo8AAAAAAAAAAAAAE9oO95pqEvabYjMhVYcp8KQ2bR2xuPLSWO26MDXNV5lIdoMkrEG7tzGwGeQVAoHrpRoEJHY%2Bg0Y9rHRbCACIgEDQMRwEA%3D%3D',
        'sessionid': 'dace8e4f9a81a2259c1a96c9910ae41e',
        'sessionid_ss': 'dace8e4f9a81a2259c1a96c9910ae41e',
        'sid_guard': 'dace8e4f9a81a2259c1a96c9910ae41e%7C1756395172%7C5184000%7CMon%2C+27-Oct-2025+15%3A32%3A52+GMT',
        'sid_tt': 'dace8e4f9a81a2259c1a96c9910ae41e',
        'uid_tt': 'dda58f6e5e3db834f577dbad0cb17417',
        'uid_tt_ss': 'dda58f6e5e3db834f577dbad0cb17417',
        'session_tlb_tag': 'sttt%7C3%7C2s6OT5qBoiWcGpbJkQrkHv________-kNYH358LzmEGwlRwcZfrNm_FhEp2YT2gTGqfwqU21taE%3D',
        'install_id': '986720338984344',
        'ttreq': '1$815d2676a4905d100962be278418abe04e120301',
        'odin_tt': 'ff6e507e0e1e451796e17b5a9824c59d599627fa0e2f6e15f1c65e7835f5f777e1b9be981a07ed42fc399d734bea627733ab491a07db6432f3f67e5009a21b47a256e23a1339a44195a1f895b242fd7d'
    }

    # 请求头
    headers = {
        'Host': 'api5-normal-sinfonlineb.dcarapi.com',
        'Connection': 'keep-alive',
        'Content-Length': '489',
        'X-SS-STUB': '4B93CA1B10F0C79B714F24391800DBE3',
        'x-vc-bdturing-sdk-version': '3.6.4',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-SS-Cookie': 'odin_tt=ff6e507e0e1e451796e17b5a9824c59d599627fa0e2f6e15f1c65e7835f5f777e1b9be981a07ed42fc399d734bea627733ab491a07db6432f3f67e5009a21b47a256e23a1339a44195a1f895b242fd7d; install_id=986720338984344; ttreq=1$815d2676a4905d100962be278418abe04e120301; session_tlb_tag=sttt%7C3%7C2s6OT5qBoiWcGpbJkQrkHv________-kNYH358LzmEGwlRwcZfrNm_FhEp2YT2gTGqfwqU21taE%3D; d_ticket=0afbfd8e43280faa9c73d851d6c5145852471; is_staff_user=false; n_mh=RgbbQ52lJbGj9AXg4m7dfQCZpIUVCKRS9Lxgw-Wy4Ko; passport_mfa_token=CjYEGupIZbjL6nNUkmNary%2BGXLkRFoZdD%2Fi4FxugyoWz75MULIwVFOWSVvhBS%2F2WgLLetmskg%2BIaSgo8AAAAAAAAAAAAAE9oO95pqEvabYjMhVYcp8KQ2bR2xuPLSWO26MDXNV5lIdoMkrEG7tzGwGeQVAoHrpRoEJHY%2Bg0Y9rHRbCACIgEDQMRwEA%3D%3D; sessionid=dace8e4f9a81a2259c1a96c9910ae41e; sessionid_ss=dace8e4f9a81a2259c1a96c9910ae41e; sid_guard=dace8e4f9a81a2259c1a96c9910ae41e%7C1756395172%7C5184000%7CMon%2C+27-Oct-2025+15%3A32%3A52+GMT; sid_tt=dace8e4f9a81a2259c1a96c9910ae41e; uid_tt=dda58f6e5e3db834f577dbad0cb17417; uid_tt_ss=dda58f6e5e3db834f577dbad0cb17417; MONITOR_WEB_ID=87898f55-1008-40d1-a5de-340659085a66; passport_csrf_token=e08704ca15a2a2d6670ae788c283002e; passport_csrf_token_default=e08704ca15a2a2d6670ae788c283002e',
        'tt-request-time': str(current_timestamp * 1000),
        'User-Agent': 'AutoMobile 8.7.1 rv:8.7.1.05 (iPhone; iOS 18.6; zh_CN) Cronet',
        'x-Tt-Token': '00dace8e4f9a81a2259c1a96c9910ae41e0136c7a61eb2f4e6f52c92e077e17d5de9f91fcf627bb003d03818e5d9dea853c4afe105dbe8c1a2be8d2707c0a48e14c20c7bf107746a456999470af2a1697530b30eb19d1494f0bbef2d570053d1b1da6--0a490a20c21c084312eb815679e44cf11f36663d22ad0d4eeb69df8cba2a39b00e8c712a1220af5ed274bc9fc64e30a7747ef1adaa73d986ee982be4b4d3958f3fc670c6b2ac18f6b4d309-3.0.1',
        'sdk-version': '2',
        'passport-sdk-version': '5.20.8-alpha.64-anniex',
        'x-bd-kmsv': '1',
        'X-SS-DP': '36',
        'x-tt-trace-id': f'00-f15e41940dc41699798323a533fd0024-f15e41940dc41699-01',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Argus': 'bnqwaA==',
        'X-Gorgon': '8404007900001dacba59aaba950a835ecc835e0a081d5330df69',
        'X-Helios': 'cxE1XHgQK6xVdhQxD4FGjSinefmnG5uiqUKSG6+0vvtgTlO3',
        'X-Khronos': str(current_timestamp),
        'X-Ladon': 'aLB6bg==',
        'X-Medusa': 'bXqwaJmS75K5rWxTuFB4GDm10XDgkQEDkj696+EB6lQBUQiYbb2byGXshqL5eoSOjOQjfI71Xu8P7wqQOvHeqA8K7jDbVU9ANSdheo0kNggAscDcdEdEdbyzBZBLOiaNtvzqpGRu4AwZe+dNyuydSBP2a3tVY5qtYA1PFntYo9ME+urN8SmKXnHovsqdzxKjKrNWFYJp7QFMuqsoE7CrzfbglomEBxrB4IHm7TBs6+MGuCU+p/audtD94RugXeO6N75NI0PxQISC8ndtqWsJEilZ3hNjtU06d3E2C8fVOFDa49IXq/IFrWqTs+GBQQN+g1ntO96llsBNQRRALeAbNDisv2ScnLGdNwr0wsbmEqDGbVhzlc2QbJDZ6zwvrQbPhGC0stacxjunP1okplibbgIAAhOIRe9eDDF2qM+4LS7FsNeIN1PKbETyE8ryYpuQ4gXqRGaQVDgIitOIAQwf1SBmWQNUI9IX7NetUR9PBlcim66xH0XpGJvinWFthz0vaB3keafeYpIPAOhXdkhdGa4nlBy6xBNv0JYnHV/Q8JSPBzwR3xwOZk7WlWbvPcBs7MgQwVCV19pMOjAJ3OthxJ7gsZq26XBottZ4jtlCd419dD7zbhwc+AOlOSh1l0tFKYsD1dxCOLCAGpVSQosJ51acZZDUyYpx0OO4U2f3qXsQH/XfxsVpf9TkZCCNHJz7AdQ6Uan5WOHUNMVFt2fMLPHUwDH/ZnpCObmHg9BvRJg9CO2IEKigoxc0IxQCFUhhSWdMEraZk+tygrziWscp0GYq3OWCOsK+0hGc1uOtBJuYLaGhNvWFxM2fVonpemtVtIxIP/8t/v//Lf7aW4=',
        'Cookie': '; '.join([f'{k}={v}' for k, v in cookies.items()])
    }

    # 表单数据
    form_data = {
        'customer': '张海龙',
        'link_source': 'dcd_page_category-category_top_tab_gov_coupon_govconsumecoupon',
        'mobile_token': '@KlWMJh2u7t8949YJvgQ6HFgULU6o8/bl37TCQKj8HqP8MFS+w8z10H/ufLebwboS',
        'mobile_token_type': '0',
        'order_title': '汽车消费补贴发放中',
        'sku_list': '[{"sku_version":"7541349903450099737","sku_id":"20522356"}]',
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


# 主程序
if __name__ == "__main__":
    print("开始发送请求...")
    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

    # 使用多线程并行发送请求
    threads = []
    durations = []

    # 创建并启动线程
    for i in range(3):
        thread = threading.Thread(target=send_request_thread, args=(i + 1,))
        thread.start()
        threads.append(thread)
        time.sleep(0.1)  # 启动间隔100毫秒

    # 等待所有线程完成并收集耗时数据
    for thread in threads:
        thread.join()
        # 无法直接获取返回值，需要修改线程函数返回值处理

    # 分析性能
    print("\n性能分析:")
    print(f"总线程数: {len(threads)}")

    # 重新组织代码以收集耗时数据
    durations = []
    for i in range(3):
        start_time = time.time()
        duration = send_request_thread(i + 1)
        durations.append(duration)
        if i < 2:
            # 计算需要等待的时间
            elapsed = (time.time() - start_time) * 1000
            wait_time = max(0, 100 - elapsed) / 1000
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