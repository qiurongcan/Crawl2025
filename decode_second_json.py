# 解析第二级 json data



import os
import pandas as pd
from box import Box
from tqdm import tqdm


folder_path = r'secondData'

file_paths = os.listdir(folder_path)

# 第三级网址的基础网址
base_url = r'https://xiaoyuan.zhaopin.com/'

for path in tqdm(file_paths):

    p = os.path.join(folder_path, path)
    # print(p)
    data = Box().from_json(filename=p)

    jobList = data.data.list

    for job in jobList:
        firstPublishTime = job.firstPublishTime
        jobSummary = job.jobSummary
        name = job.name
        number = job.number
        publishTime = job.publishTime
        salary60 = job.salary60
        workType = job.workType
        workCity = job.workCity
        workingExp = job.workingExp
        # print(name, "  ", number, "  ", workType, "  ", workingExp, "  ", workCity)
        third_url = base_url+number
        print(third_url)
    break


