# 答题助手
## 程序功能
1、调用百度OCR接口识别题目
2、调用百度搜索搜索答案，题目与选项交叉搜索，按照搜索结果给出建议答案
###测试结果准确率大概只有70%~80%，可以做为参考，也可以用来调用浏览器搜索

## 程序用法
0、程序依赖在requirements.txt
1、使用前请安装一个手机模拟器，将答题直播显示到电脑上
2、高级搜索会调用交叉搜索，用时更长，一般网络条件下需要5秒左右
3、记录题目选中会记录题目到questions.txt文件中

## 不足与改进1
1、没有核心算法，欠缺NLP相关知识，水平有限
2、完成自动答题功能，不用手动操作，这样答错也不会浪费自己时间
3、并行答题

欢迎指教 zfneutrino@gmail.com
