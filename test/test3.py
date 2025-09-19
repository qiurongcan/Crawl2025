# 测试抓取一个详细网页
import requests
import re
import json
from box import Box

url = r'https://xiaoyuan.zhaopin.com/job/CC143133620J40383426913'

header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "cookie": "_uab_collina=173711689095461804156539; __tst_status=3328920973#; EO_Bot_Ssid=1717764096; x-zp-client-id=1732b3cd-7dda-49cf-b2b2-f3566750afe4; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; sts_deviceid=1946e5a764d1830-0073237d935f04-4c657b58-2073600-1946e5a764e2a16; LastCity=%E8%A5%BF%E5%AE%89; LastCity%5Fid=854; Hm_lvt_7fa4effa4233f03d11c7e2c710749600=1757040881,1758287635,1758295641; HMACCOUNT=09DF9E5DD31440E6; at=cbb670c1f7b148a598d95c424f4828a8; rt=f2f048dba29e4357b80f4712a33e5783; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221150604039%22%2C%22first_id%22%3A%221946e23d26841-0da0e77d15d7af8-4c657b58-2073600-1946e23d269265d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0NmUyM2QyNjg0MS0wZGEwZTc3ZDE1ZDdhZjgtNGM2NTdiNTgtMjA3MzYwMC0xOTQ2ZTIzZDI2OTI2NWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTUwNjA0MDM5In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221150604039%22%7D%2C%22%24device_id%22%3A%221946e23d26841-0da0e77d15d7af8-4c657b58-2073600-1946e23d269265d%22%7D; locationInfo_job={%22code%22:%22854%22%2C%22name%22:%22%E8%A5%BF%E5%AE%89%22}; _uab_collina=175829649671257217223886; selectCity_search=530; locationInfo_search={%22code%22:%22854%22%2C%22name%22:%22%E8%A5%BF%E5%AE%89%22}; ZL_REPORT_GLOBAL={%22company%22:{%22actionid%22:%22cef9ce99-feb2-4bb7-a71b-5ae09cd1f32f-company%22%2C%22funczone%22:%22hiring_jd%22}}; Hm_lpvt_7fa4effa4233f03d11c7e2c710749600=1758300242"
}


resp = requests.get(url=url, headers=header)
obj = re.compile(r'INITIAL_DATA__ = (.*?)</script', re.S)

data = obj.findall(resp.text)[0]
# print(data)
data = json.loads(data)
data = Box(data)
data.to_json("test7.json", indent=2)
resp.close()