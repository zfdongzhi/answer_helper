#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:Zhai-Fan
# mail: zfneutrino@gmail.com
from aip import AipOcr
import datetime


# baidu ocr key
APP_ID = '10714141'
API_KEY = 'u6NYbZValbFRjLkngQDqgHIp'
SECRET_KEY = 'oXzvN8hivVpvr6P343qSLvA7KxdfazSx'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def baidu_ocr(debug):
    question = ''
    answer_options = []
    option = {}
    option["probability"] = "true"
    option["vertexes_location"] = "true"
    option["recognize_granularity"] = "big"
    result = client.basicGeneral(get_file_content('0.png'), option)
    words_result = result['words_result']
    line_num = result['words_result_num']
    last_line = 0
    for i in range(line_num):
        top = words_result[i]['min_finegrained_vertexes_location'][0]['y']
        bottom = words_result[i]['min_finegrained_vertexes_location'][2]['y']
        if last_line > 0 and (top - last_line) > 0.8 * (bottom - top):
            break
        last_line = bottom
        question += words_result[i]['words']
    for j in range(i, line_num):
        if words_result[j]['words'][0] != 'A' and words_result[j]['words'][0] != 'B' and \
           words_result[j]['words'][0] != 'C' and words_result[j]['words'][0] != 'D':
            answer_options.append(words_result[j]['words'])
    if len(answer_options) < 2:
        answer_options = answer_options[0]
    if debug:
        time = datetime.datetime.now().strftime("%m/%d %H:%M:%S")
        f = open('questions.txt', 'a')
        f.write(time + '\n')
        f.write(question + '\n')
        f.write(' '.join(answer_options))
        f.write('\n')
    return question, answer_options


# question, options = baidu_ocr(0, 0)
# print(question,options)
# print(new_question(Image.open('5.png')))
