import httpx
import json


async def resend_request():
    # 请求头
    headers = {
        'host': 'api.m.jd.com',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/plain, */*',
        'sec-fetch-site': 'same-site',
        'x-rp-client': 'h5_1.0.0',
        'priority': 'u=3, i',
        'accept-language': 'zh-CN,zh-Hans;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'sec-fetch-mode': 'cors',
        'origin': 'https://pro.m.jd.com',  # 这里需要替换为实际的origin值
        'content-length': '2983',
        'user-agent': 'jdapp;iPhone;15.2.30;;;M/5.0;appBuild/170045;jdSupportDarkMode/0;lang/zh_CN;site/CN;ccy/CNY;elder/0;ef/1;ep/{"ciphertype":5,"cipher":{"ud":"DwTrCzKmY2Y2DzZuZWY0YWOnDNYyDQVsEQG3YJvsYzCyEQTsCNrwEG==","sv":"CtYkCK==","iad":""},"ts":1759052315,"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","version":"1.0.3","appname":"com.360buy.jdmobile","ridx":-1};Mozilla/5.0 (iPhone; CPU iPhone OS 26_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;',
        'x-referer-page': 'https://pro.m.jd.com/mall/active/wUEbTVFKwN7pFrCgSCNHxh7PJEG/index.html',
        'referer': 'https://pro.m.jd.com/mall/active/wUEbTVFKwN7pFrCgSCNHxh7PJEG/index.html?stath=47&navh=44&babelChannel=ttt4&visitScene=618&tttparams=iDowD4O1EeyJyZnMiOiIwMDAwIiwicG9zTG5nIjoiMTE4LjMyMDgzMyIsImRsIjoxLCJ1ZW1wcyI6IjAtMi0wIiwiZ0xuZyI6IjExOC4zMjA4MzMiLCJnTGF0IjoiMjQuNjA0NzI3IiwibG5nIjoiMTE4LjI2NjA1NSIsIm9yaWVudCI6InAiLCJvcyI6IjI2LjAiLCJsYnNMYXQiOiIyNC41ODg1NjYiLCJkTG5nIjoiIiwiZExhdCI6IiIsImxic0xuZyI6IjExOC4yNjYxNDYiLCJwcnN0YXRlIjoiMCIsImdwc19hcmVhIjoiMTZfMTMxNV8zNDg5XzQ2ODE2Iiwic2NhbGUiOiIzIiwiYWRkcmVzc0lkIjoiMTE4OTU1MTc2NDIiLCJ1bl9hcmVhIjoiMTZfMTMxNV8zNDg5XzQ2ODE2Iiwid2lkdGgiOiIxMTcwIiwibGJzQXJlYSI6IjE2XzEzMTVfMzQ4OV80NjgxNiIsImxhdCI6IjI0LjU4ODc0MiIsIm1vZGVsIjoiaVBob25lMTQsNyIsInJMbmciOiIxMTguMzIwODMzIiwickxhdCI6IjI0LjYwNDcyNyIsInBvc0xhdCI6IjI0LjYwNDcyNyIsImFyZWFDb2RlIjoiMCIsImNvcm5lciI6MX90=',
        'sec-fetch-dest': 'empty',
        'cookie': 'sdtoken=AAbEsBpEIOVjqTAKCQtvQu17C4fUqrvujV4FCR2Vo7UqhFWpppvFOdFWAS5ok31GXWBTs79gpCN-8HoqtRS-5CTFWEQS-v5LSwX8oy-UbrdKtp5oif8uy03gqQ_AcrAc0wdNEi2dwg; shshshfpa=5c7e9cf7-d57a-ba46-68d4-9434143c8e07-1728510432; shshshfpb=BApXSr6m4jPxAiDLnJz1U8tod_UOv-j_dBmoQAx1o9xJ1PdZfQq3chRfovDzQPaNLRBYCAKnn; __jd_ref_cls=Babel_dev_other_government_subsidies_bind; pre_seq=22; mba_muid=17590523124231150909339.406.1759052314495; mba_sid=406.19; unpl=JF8EAIFnNSttW04GAU5RExYUQggGWw1bG0cBbDVRXV4NQ1NVGgYYGhR7XlVdWRRKHx9sZBRVVVNKUA4fAisiE0xeUllbCk8UMzw3XQEZEAk6BRsGHxMRSl9WV14JSCczbGc1VFxoe1U1HDIrIhNMWlxcXzhKJwJfJVEIWVtIVQYdTysTIEg|JF8EAMZnNSttDRhRVR0CGkZHHFxSWw9cHx9QPDRVUlRQH1JQHwFIRkV7XlVdWRRKHx9vYhRUXVNIXA4bCisiEEpcVF9ZC04fA19kAlddXUNRBSsEdRAZTV1WW1wMJRQCbgl4DBoMCRUZGwF1En5IWldeWABOF21fZAVkXGhLUgEdBB8VE0NZVlxcDkIVAGpiAV1faEpkDBoyGxMRS1hSXVoPSBYGX1cEZFxoSmROdQNWEhZPW1JaWgtDEwBtZgNdX1tOUQESACsTIEs; __jda=122270672.17590523124231150909339.1759052312.1759052312.1759052312.1; __jdb=122270672.4.17590523124231150909339|1.1759052312; __jdv=122270672|manu_nc|-|Negative_screen|AppShortcut-search|1758715607000; cid=8; shshshfpx=17513724-686a-3edd-fe96-593003b85f77-1682518597; 3AB9D23F7A4B3C9B=CH3MYTKFADKYHXLCM5AUEBESP64NKCR52G2L633SLDWSCUATUQBRT2PCGRCP2GOP65GXER75AZCGAJVWCMJNYRLWTM; 3AB9D23F7A4B3CSS=jdd03CH3MYTKFADKYHXLCM5AUEBESP64NKCR52G2L633SLDWSCUATUQBRT2PCGRCP2GOP65GXER75AZCGAJVWCMJNYRLWTMAAAAMZR6YDDVYAAAAACIU5IC4DD7GYKAX; __jdc=122270672; _gia_d=1; pre_session=6ba300cf676def4aa14624eb8d7a9bc328bb08f9|708; b_avif=1; b_dh=588; b_dpr=3; b_dw=390; b_webp=1; pt_key=app_openAAJo2QIYADBqt7khQnDheut8zyUNKEnL1tWrdbGQOr79EGkPIISdhm8b6MCyNI4OgqUHkSmkmw0; pt_pin=jd_KjwmcPwJnEXW; pwdt_id=jd_KjwmcPwJnEXW'
    }

    # 请求体数据
    data = {
        'appid': 'gov-subsidy-h5',
        'loginType': 'null',
        'loginWQBiz': '',
        'functionId': 'bindingQualification',
        'body': '{"cateId":"B01","cateName":"手机","subCateId":"B01","provinceId":16,"cityId":1315,"channelId":"2025_16_1315_8","cateType":null,"qualificationRegionLevel":2,"locProvinceId":16,"loCityId":1315,"locCountyId":3489,"locTownId":46816,"otherPos":"{\\"code\\":0,\\"message\\":\\"ok\\",\\"region\\":\\"中国\\",\\"regionid\\":\\"0\\",\\"province\\":\\"福建\\",\\"provinceid\\":\\"16\\",\\"city\\":\\"厦门市\\",\\"cityid\\":\\"1315\\",\\"district\\":\\"翔安区\\",\\"districtid\\":\\"3489\\",\\"town\\":\\"新店街道\\",\\"townid\\":\\"46816\\",\\"detailaddr\\":\\"\\",\\"fullAddress\\":\\"福建厦门市翔安区新店街道\\",\\"oversea\\":\\"0\\",\\"callType\\":\\"GisService\\",\\"srclng\\":118.265995,\\"srclat\\":24.588582,\\"updateTime\\":1759052345064,\\"encryptLng\\":\\"aYBTP1y5jLFlPp2BUxf-gA\\",\\"encryptLat\\":\\"883C4qRcwZMtuiXddjHmEQ\\",\\"gridId\\":0,\\"poi\\":\\"\\",\\"accuracy\\":15}","paymentType":null,"clientVersion":"15.2.30","sourceChannelId":3}',
        'channelId': '2025_16_1315_8',
        't': '1759052414474',
        'h5st': '20250928174016484;6wzmtmzmzhjwq3p8;1365e;tk03wa9121c6b18nMQZYpDxl0PjK_Ky6SnQMY-JitiJXYmF1hUbYmHBl264uBFzNkl78E2FsvViLXxMDmVYFoxipRyLB;04588eb5da138a8a9b6c73d2918cd058;5.2;1759052414484;gt6f-BeFudqE3A7D04KGts7DqI_ZB5_ZxI7ZBh-f1ReZnZ-G_U7ZBh-f1ZvJrZ7JAUbI9EOV-MLT7EeV7UeUr9uJ_UbVoZeUo9OJ7YfZnZfFbwrI-MrE-hfZXx-Z7QLVvJ_IAM_UvBOTxVOVxVLJsd_V-YLJxZeV8M7V-c7ZB5_Zuc7EzcrJ-hfZXx-ZxZfZnZfUsY7ZBh-f1ZfVzZ_WsJqK8wLH7kMU5YfZnZ-E-hfZXx-ZtRcFvBeLVQuG-h-T-trG9oLJvYfZB5hW-N7GyAbN4YfZnZ-IxYfZB5hWkgfZXZ-IbYfZnZvVwN6J-hfZBh-f1ZeZnZPVwN6J-hfZBh-f1ROVB5_ZxdOE-YfZBhfZXxfT0h-T-ZOVsY7ZBhfZB5hW-BcD0g8NQE8V8kLN2s7ZB5_Z0kbIzc7F-hfZBh-f1heZnZfTsY7ZBhfZB5hWxh-T-FOE-YfZBhfZXxfUuh-T-JOE-YfZBhfZXxfVB5_ZsN6J-hfZBh-f1heZnZfUsY7ZBhfZB5hWxJeZnZvVsY7ZBhfZB5hW-N_WwpfVCMbE4w7ZB5_ZwN6J-hfZBh-f1heZnZvHqYfZBhfZXxPUB5_Zuw7ZBhfZB5hWxh-T-x7ZBhfZB5hWxh-T-RrE-hfZBh-fmg-T-R7G8QaD8YfZB5hWkgfZXZvMJM9GXEaN_srE30tK947ZB5_Zwh6ZBhfZB5xDB5_Zxg6ZBh-f1ZfLBVsOBVLJUgPI28bGBhuKrZeZOkdZ8orG5gMHBNcNegvT8orG5gMH-h-T-dLEuYfZB5xD;6c63ae6d7376b79e3cca029e282b43d1;gRaW989Gy8bE_oLE7wPD9k7J1RLHxgKJ',
        'x-api-eid-token': 'jdd03CH3MYTKFADKYHXLCM5AUEBESP64NKCR52G2L633SLDWSCUATUQBRT2PCGRCP2GOP65GXER75AZCGAJVWCMJNYRLWTMAAAAMZR6YDDVYAAAAACIU5IC4DD7GYKAX'
    }

    # 发送POST请求
    async with httpx.AsyncClient(http2=True) as client:
        try:
            # 注意：需要将 "链接1" 替换为实际的URL
            response = await client.post(
                "https://api.m.jd.com/client.action",  # 这里需要替换为实际的URL
                headers=headers,
                data=data,
                timeout=30.0
            )

            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            return response

        except Exception as e:
            print(f"Error: {e}")
            return None


# 运行异步函数
import asyncio

asyncio.run(resend_request())