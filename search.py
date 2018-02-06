#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:Zhai-Fan
# mail: zfneutrino@gmail.com

import requests
import re
import webbrowser
import datetime

url = 'https://www.baidu.com/s'
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9'}
PAGE_MAX = 30
# url_get = re.compile('<h3[\s\S]*?<a[^>]*?href[^>]*?"(.*?)"[^>]*?>.*?</a>')
content_get = re.compile('id="content_left"([\s\S]*?)id="page"')


def neg_judge(question):
    neg_list = ['没有', '不']
    for word in neg_list:
        if question.find(word)>0:
            return 1
    return 0


def baidu_search(question, options, browser_flag, more_search):
    params = {'wd': question, 'pn': 0, 'ie': 'utf-8', 'rn': 10}
    mark_raw = [0] * len(options)
    mark_unit = 1024
    # starttime = datetime.datetime.now()
    if browser_flag:
        webbrowser.open("https://www.baidu.com/s?wd=" + question)
    try:
        while params['pn'] < PAGE_MAX:
            resp = requests.get(url, params, headers=headers).content
            search_res = content_get.findall(resp.decode('utf'))
            # search_res = resp.decode('utf')
            for i, ans_i in enumerate(options):
                mark_raw[i] += len(re.compile(ans_i).findall(search_res[0])) * mark_unit
            # for i in url_get.findall(res):
            # request i[0] get calculate
            params['pn'] += 10
            mark_unit /= 2
    except Exception as e:
        print("Unexpected Error: {}".format(e))
    # endtime = datetime.datetime.now()
    # print(endtime - starttime)
    if more_search:
        for answer in options:
            mark_unit = 16
            params['pn'] = 0
            try:
                while params['pn'] < 10:
                    params['wd'] = question + ' ' + answer
                    resp = requests.get(url, params, headers=headers).content
                    search_res = content_get.findall(resp.decode('utf'))
                    for i, ans_i in enumerate(options):
                        mark_raw[i] += len(re.compile(ans_i).findall(search_res[0])) * mark_unit
                    # for i in url_get.findall(res):
                    # request i[0] get calculate
                    params['pn'] += 5
                    mark_unit /= 2
            except Exception as e:
                print("Unexpected Error: {}".format(e))
    mark_max = 0
    mark_min = 2000000
    for i, mark in enumerate(mark_raw):
        if mark > mark_max:
            ans_max = options[i]
            mark_max = mark
        if mark < mark_min:
            ans_min = options[i]
            mark_min = mark
        # print(options[i], ':', mark)
    # endtime = datetime.datetime.now()
    # print(endtime - starttime)
    if neg_judge(question):
        return ans_min
    else:
        return ans_max


# ans = ['美国', '英国', '法国']
# baidu_search('世界上第一家电视台出现在哪个国家', ans, 0, 1)

# ans = ['泸州市', '成都市', '达州市']
# baidu_search('古城“江阳”",以酿酒业驰名中外而有“酒城”美誉的是四川省哪座城市', ans, 0, 0)

# ans = ['狮身人面像', '卡纳克神庙', '卢浮宫']
# baidu_search('以下哪项不是埃及的著名景点', ans, 0, 1)
