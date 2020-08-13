# -*- coding: utf-8 -*-
import os

desktop_path = r'C:/Users/muc/Desktop/'
'''
	Excel
'''
excel_url_head = "http://college.bjjryj.com/static/Video/ICDL/GJSSB/" #　1.mp4


'''
	WORD
'''
word_url_head = "http://college.bjjryj.com/static/Video/ICDL/GJWSCL/" #　1.1.mp4.mp4
word_dict = {
	'1.1': '1.1修改文字格式1.mp4',
	'1.2': '1.2修改文字格式2.mp4',
	'2'  : '2.使用分节符.mp4',
	'3.1': '3.1使用表格功能1.mp4',
	'3.2': '3.2使用表格功能2.mp4',
	'4'  : '4.使用批注和修订.mp4',
	'5'  : '5.使用表单和保护.mp4',
	'6'  : '6.创建主控文档.mp4',
	'7'  : '7.创建目录.mp4',
	'8'  : '8.创建索引.mp4',
	'9'  : '9.书签、题注和脚注.mp4',
	'10' : '10.使用邮件合并.mp4',
	'11' : '11.链接/嵌入对象.mp4',
	'12' : '12.使用宏.mp4',
	'13' : '13.综合练习一.mp4',
	'14' : '14.综合练习二.mp4',
}

'''
	PPT
'''
ppt_url_head = r"http://college.bjjryj.com/static/Video/ICDL/GJYSWG/"  #　1.mp4
ppt_dict = {
	1: "1.自定义演示文稿.mp4",
	2: "2.编辑幻灯片母板.mp4",
	3: "3.绘制对象.mp4",
	4: "4.图形（上）.mp4",
	5: "5.图像（下）.mp4",
	6: "6.使用SmartArt.mp4",
	7: "7.添加特殊效果.mp4",
	8: "8.设置幻灯片放映.mp4",
	9: "9.使用幻灯片放映视图.mp4",
	10:"10.展示幻灯片放映.mp4",
	11:"11.创建自定义图表.mp4",
	12:"12.编辑图表.mp4",
	13:"13.导出大纲和幻灯片.mp4",
	14:"14.设计注意事项.mp4",
	15:"15.综合练习（一）.mp4",
	16:"16.综合练习（二）.mp4",
	17:"17.综合练习（三）.mp4",
}


def IDMdownload(url_dict, url_head, DownPath):
	IDMPath = r"C:/Program1/IDM 6.35.17 绿色/App"
	os.chdir(IDMPath)
	IDM = "IDMan.exe"

	for k,v in url_dict.items():
		FileName = v
		DownUrl = f'{url_head}{k}.mp4'
		command = ' '.join([IDM, '/d', DownUrl, '/p', DownPath, '/f', FileName, '/s', '/n'])
		# print(command)
		os.system(command)

IDMdownload(word_dict, word_url_head, desktop_path)

# for inx in range(7, 14):
# 	video_url = f'http://college.bjjryj.com/static/Video/ICDL/GJSSB/{inx}.mp4'
# 	desktop_path = r'C:/Users/muc/Desktop/'
# 	IDMdownload(video_url, desktop_path, f'{inx}.mp4')