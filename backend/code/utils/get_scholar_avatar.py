import requests
import json
from tqdm import tqdm
import threading


def get_scholar_avatar(name, school):
    # 定义 URL 和 POST 数据
    url = 'https://searchtest.aminer.cn/aminer-search/search/person'
    data = {
        "query": "",
        "needDetails": True,
        "page": 0,
        "size": 20,
        "searchKeyWordList": [
            {"advanced": True, "keyword": name, "operate": "0", "wordType": 4, "segmentationWord": "true",
             "needTranslate": True},
            {"advanced": True, "keyword": school, "operate": "0", "wordType": 5, "segmentationWord": "true",
             "needTranslate": True}]
    }
    # 发送 POST 请求
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    response_json = response.json()
    # 从 JSON 数据中获取头像 URL
    hit_list = response_json['data'].get('hitList', [])

    # 检查 hit_list 是否有内容
    if len(hit_list) > 0:
        if hit_list[0].get('avatar', None):
            avatar_url = hit_list[0]['avatar']
        else:
            avatar_url = None
    else:
        avatar_url = None
    return avatar_url


THREAD_COUNT = 6

scholar_list = []
new_data = []


# 负责[left, right]闭区间的数据
def get_avatar(left, right):
    tmp_scholar_list = scholar_list[left: right + 1]
    for tmp_scholar in tqdm(tmp_scholar_list):
        try:
            avatar_url = get_scholar_avatar(tmp_scholar['display_name'], tmp_scholar['institution'])
            if avatar_url is not None:
                new_scholar = {
                    '_id': tmp_scholar['_id'],
                    'display_name': tmp_scholar['display_name'],
                    'institution': tmp_scholar['institution'],
                    'h_index': tmp_scholar['h_index'],
                    'avatar_url': avatar_url,
                }
                new_data.append(new_scholar)
        except:
            print('error: ', tmp_scholar['display_name'])
            continue


if __name__ == '__main__':

    with open('author_list.json', 'r', encoding='utf-8') as f:
        scholar_list = json.load(f)

    # 多线程爬取
    threads = []
    for i in range(THREAD_COUNT):
        each_cnt = len(scholar_list) // THREAD_COUNT
        print('each_cnt: ', each_cnt)
        if i == THREAD_COUNT - 1:
            threads.append(threading.Thread(target=get_avatar, args=(each_cnt * i, len(scholar_list) - 1)))
        else:
            threads.append(threading.Thread(target=get_avatar, args=(each_cnt * i, each_cnt * (i + 1) - 1)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('new_data: ', len(new_data))
    with open('avatar_list.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(new_data, ensure_ascii=False))
