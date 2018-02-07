#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:Zhai-Fan
# mail: zfneutrino@gmail.com

# from PIL import Image
from PIL import ImageGrab
from aip import AipOcr
import datetime
# import colorsys

# baidu ocr key
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# def new_question(image):
#     image = image.convert('RGBA')
#     max_score = 0
#     dominant_color = None
#     for score, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
#         if a == 0:
#             continue
#         saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
#         y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
#         y = (y - 16.0) / (235 - 16)
#         if score > max_score:
#             max_score = score
#             dominant_color = (r, g, b)
#         if dominant_color[0] + dominant_color[1] + dominant_color[2] > 760:
#             return 1
#         else:
#             return 0


def im_cap(programme):
    if programme == 'QQ':
        location = (18, 120, 335, 440)  # to do
    elif programme == '163':
        location = (18, 120, 335, 440)  # to do
    elif programme == 'Toutiao':
        location = (18, 130, 370, 480)
    elif programme == 'Taobao':
        location = (18, 150, 360, 480)
    elif programme == 'Chongding':
        location = (18, 130, 368, 443)
    elif programme == 'Zhishi':
        location = (18, 138, 370, 450)
    else:
        location = (18, 120, 335, 440)
    im = ImageGrab.grab(location)
    im.save('0.png')


def baidu_ocr(head, debug):
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
    question = question[head:-1]
    # question = question.encode('utf')
    # if words_result[i]['min_finegrained_vertexes_location'][0]['y'] - words_result[i+1]['min_finegrained_vertexes_location'][0]['y'] < 5\
    #         and words_result[i+1]['min_finegrained_vertexes_location'][0]['y'] - words_result[i]['min_finegrained_vertexes_location'][0]['y'] < 5:
    #     diff = 2
    # else:
    #     diff = 1
    for j in range(i, line_num):
        bottom = words_result[j]['min_finegrained_vertexes_location'][2]['y']
        if bottom - last_line > 5 or last_line - bottom > 5:
            answer_options.append(words_result[j]['words'])
        last_line = bottom
    if debug:
        time = datetime.datetime.now().strftime("%m/%d %H:%M:%S")
        f = open('questions.txt', 'a')
        f.write(time + '\n')
        f.write(question + '\n')
        f.write(' '.join(answer_options))
        f.write('\n')
    return question, answer_options


# im_cap('Taobao')
# question, options = baidu_ocr(2, 0)
# print(question,options)
# print(new_question(Image.open('5.png')))
