
import requests
import re
import json
from box import Box
import os
from time import time, sleep
from tqdm import tqdm

folder_path = r'secondData'
os.makedirs(folder_path, exist_ok=True)




cities = ["北京", "上海", "广州", "长春", "天津", "重庆", "西安", "杭州"]
cityCode = [530, 538, 763, 613, 531, 551, 854, 653]
codeToCity={
    "北京": 530,
    "上海": 538,
    "广州": 763, 
    "长春": 613, 
    "天津": 531,
    "重庆": 551, 
    "西安": 854, 
    "杭州":653
}

def crawl_second(major="会计", cityCode=530, page=1):
    """
    Args:
        major: 专业或者职位名称 [可以自定义]
        cityCode: 城市编码
        page: 抓取的页数 二级目录一页20个职位
    """

    url = r'https://cgate.zhaopin.com/positionbusiness/searchrecommend/searchPositions'

    json_data = {
        "identity":"1",
        "filterMinSalary":1,
        "version":"8.2.6",
        "pageIndex":page,
        "pageSize":20,
        "cvNumber":"F72C5E18A8ED6D5FE7BACABEFF6CD8BCC59D30A8BBDA1841D55E2064C331645118A767D2CDFC6BFE94144A9C2565F11E_A0001",
        "order":12,
        "at":"cbb670c1f7b148a598d95c424f4828a8",
        "rt":"f2f048dba29e4357b80f4712a33e5783",
        "S_SOU_FULL_INDEX":major,
        "S_SOU_WORK_CITY":cityCode,
        "d":"1732b3cd-7dda-49cf-b2b2-f3566750afe4",
        "channel":"xiaoyuan",
        "platform":"14"
        }

    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "cookie": "_uab_collina=173711688879760674241564; x-zp-client-id=1732b3cd-7dda-49cf-b2b2-f3566750afe4; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; sts_deviceid=1946e5a764d1830-0073237d935f04-4c657b58-2073600-1946e5a764e2a16; LastCity=%E8%A5%BF%E5%AE%89; LastCity%5Fid=854; Hm_lvt_7fa4effa4233f03d11c7e2c710749600=1757040881,1758287635,1758295641; HMACCOUNT=09DF9E5DD31440E6; at=cbb670c1f7b148a598d95c424f4828a8; rt=f2f048dba29e4357b80f4712a33e5783; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221150604039%22%2C%22first_id%22%3A%221946e23d26841-0da0e77d15d7af8-4c657b58-2073600-1946e23d269265d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk0NmUyM2QyNjg0MS0wZGEwZTc3ZDE1ZDdhZjgtNGM2NTdiNTgtMjA3MzYwMC0xOTQ2ZTIzZDI2OTI2NWQiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTUwNjA0MDM5In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221150604039%22%7D%2C%22%24device_id%22%3A%221946e23d26841-0da0e77d15d7af8-4c657b58-2073600-1946e23d269265d%22%7D; locationInfo_job={%22code%22:%22854%22%2C%22name%22:%22%E8%A5%BF%E5%AE%89%22}; _uab_collina=175829649671257217223886; Hm_lpvt_7fa4effa4233f03d11c7e2c710749600=1758296499; locationInfo_search={%22code%22:%22%22}; selectCity_search=530"
    }



    response = requests.post(url, json=json_data, headers=header)

    # 检查响应状态
    if response.status_code == 200:
        # 打印响应内容（JSON格式）
        # print(response.json())
        Box(response.json()).to_json(f"{folder_path}/{major}-{cityCode}-{page}.json", indent=2)
    else:
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)



if __name__ == "__main__":

    for city in tqdm(cityCode):
        
        crawl_second(cityCode=city)
        # 暂停 0.4s
        sleep(0.4)
        




