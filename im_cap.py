#!/usr/bin/python
# coding:utf8
# author:Zhai-Fan
# mail: zfneutrino@gmail.com


import os
from PIL import Image
from PIL import ImageGrab
import sys
# import colorsys


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


def im_cap_adb(programme):
    if programme == 'QQ':
        location = (0.046154, 0.123, 0.8590, 0.584)  # to do
    elif programme == '163':
        location = (0.046154, 0.123, 0.8590, 0.584)  # to do
    elif programme == 'Toutiao':
        location = (0.046154, 0.137, 0.9490, 0.642)
    elif programme == 'Taobao':
        location = (0.046154, 0.166, 0.9230, 0.642)
    elif programme == 'Chongding':
        location = (0.046154, 0.137, 0.9436, 0.589)
    elif programme == 'Zhishi':
        location = (0.046154, 0.149, 0.9490, 0.599)
    else:
        location = (0.0769, 0.325, 0.869, 0.931)
    sys.path.append("C:\\adb")
    os.system("adb -s 82dbf96b shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system("adb -s 82dbf96b pull /sdcard/screenshot.png screenshot.png")
    im = Image.open("screenshot.png")
    im_c = im.crop((im.size[0]*location[0], im.size[1]*location[1], im.size[0]*location[2], im.size[1]*location[3]))
    im_c.save('0.png')


def im_cap_pc(programme):
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
        location = (30, 260, 335, 680)
    im = ImageGrab.grab(location)
    im.save('0.png')

# from adb import adb_commands
# from adb import sign_m2crypto
#
#
# # KitKat+ devices require authentication
# signer = sign_m2crypto.M2CryptoSigner(
#     op.expanduser('~/.android/adbkey'))
# # Connect to the device
# device = adb_commands.AdbCommands.ConnectDevice(
#     rsa_keys=[signer])
# # Now we can use Shell, Pull, Push, etc!
# for i in xrange(10):
#   print device.Shell('echo %d' % i)

# adb -s 82dbf96b shell /system/bin/screencap -p /360/screenshot.png
# adb -s 82dbf96b pull /sdcard/screenshot.png screenshot.png
#
# im_cap_adb('default')
# im_cap('default')
