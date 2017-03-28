# -*- coding:utf-8 -*-

import plotly.offline
from plotly.graph_objs import *
 
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline
from plotly.graph_objs import *
# Generate the figure
import plotly.plotly as py
import plotly.graph_objs as go
#32841
list_list_all_lable = [
#0
["中国","自己","今天","就是","没有","第一","时候","朋友","大家","不是"],
#1
["中国","游戏","大家","今天","2017","自己","公司","金融","已经","第一"],
#2
["段子","哈哈","搞笑","朋友","中国","哈哈哈","视频","不是","今天","就是"],
#3
["健康","医院","医生","身体","中医","疾病","很多","血压","可以","知道"],
#4
["女人","自己","男人","朋友","时候","个人","没有","婚姻","爱情","不是"],
#5
["电影","大家","就是","一部","今天","这部","明星","中国","娱乐","自己"],
#6
["设计","装修","空间","风格","生活","家居","可以","客厅","房子","大家"],
#7
["中国","北京","市场","地产","楼市","投资","金融","公司","房价","2017"],
#8
["汽车","SUV","车型","中国","品牌","市场","销量","大家","新车","很多"],
#9
["中国","手机","苹果","联网","互联","互联网","公司","iPhone","数据","产品"],
#10
["时尚","发型","就是","搭配","大家","时髦","自己","可以","今天","女人"],
#11
["孩子","妈妈","宝宝","教育","家长","父母","自己","爸爸","家庭","幼儿"],
#12
["自己","人生","生活","没有","知道","知识","因为","不是","个人","就是"],
#13
["摄影","照片","摄影师","拍摄","中国","世界","相机","旅游","作品","镜头"],
#14
["公司","创业","管理","员工","企业","工作","自己","职场","老板","中国"],
#15
["美食","好吃","做法","蛋糕","美味","可以","鸡蛋","时候","就是","回复"],
#16
["中国","历史","文化","世界","古代","日本","就是","国人","作者","研究"],
#17
["教育","大学","孩子","学生","学校","2017","留学","高考","考研","家长"],
#18
["星座","白羊","自己","白羊座","12","爱情","他们","十二","二星","喜欢"],
#19
["中国","比赛","健身","今天","赛季","韩国","时间","体育","自己","世界"]
]
list_list_all_value = [
[ 223 , 111 , 109 , 107 , 107 , 106 , 94 , 91 , 86 , 86 ]
#1
,
[ 197 , 135 , 102 , 101 , 100 , 91 , 89 , 89 , 88 , 87 ]
#2
,
[ 683 , 154 , 124 , 117 , 104 , 95 , 94 , 91 , 89 , 88 ]
#3
,
[ 229 , 147 , 147 , 140 , 138 , 137 , 137 , 132 , 130 , 125 ]
#4
,
[ 261 , 200 , 181 , 145 , 124 , 116 , 103 , 101 , 90 , 87 ]
#5
,
[ 457 , 163 , 160 , 155 , 151 , 125 , 123 , 122 , 117 , 115 ]
#6
,
[ 491 , 380 , 169 , 158 , 156 , 123 , 118 , 109 , 105 , 97 ]
#7
,
[ 310 , 247 , 244 , 208 , 186 , 181 , 180 , 165 , 164 , 162 ]
#8
,
[ 419 , 293 , 202 , 176 , 174 , 145 , 112 , 111 , 103 , 102 ]
#9
,
[ 296 , 233 , 202 , 179 , 177 , 172 , 165 , 158 , 150 , 142 ]
#10
,
[ 208 , 177 , 163 , 161 , 156 , 154 , 153 , 149 , 140 , 139 ]
#11
,
[ 1262 , 368 , 338 , 290 , 257 , 231 , 173 , 145 , 123 , 121 ]
#12
,
[ 221 , 151 , 134 , 119 , 117 , 113 , 101 , 96 , 94 , 91 ]
#13
,
[ 748 , 200 , 186 , 164 , 139 , 110 , 101 , 93 , 89 , 83 ]
#14
,
[ 195 , 178 , 130 , 121 , 115 , 112 , 108 , 106 , 101 , 96 ]
#15
,
[ 177 , 142 , 129 , 110 , 105 , 95 , 95 , 85 , 84 , 84 ]
#16
,
[ 348 , 212 , 91 , 75 , 72 , 71 , 69 , 63 , 62 , 60 ]
#17
,
[ 315 , 271 , 198 , 175 , 157 , 146 , 143 , 141 , 137 , 129 ]
#18
,
[ 548 , 190 , 134 , 120 , 110 , 110 , 104 , 104 , 101 , 88 ]
#19
,
[ 298 , 272 , 237 , 163 , 153 , 153 , 146 , 132 , 131 , 126 ]]

list_articalClssfy= ['热门', '推荐',  '段子手','养身堂','私房话',\
					'八卦精','爱生活','财经迷','汽车迷','科技咖',\
					'潮人帮','辣妈帮','点赞党','旅行家','职场人',\
					'美食家','古今通','学霸族','星座控','体育迷']

sum=0
for a in xrange(0,20):
	for b in xrange(0,10):
		print "-",a,b
		sum +=list_list_all_value[a][b]
		print sum, 


# 
#
#
viewnum = 0
while viewnum < 20 :
	list_values = list_list_all_value[viewnum]
	list_lables = list_list_all_lable[viewnum]
	strName = list_articalClssfy[viewnum]
	myfilename = "data_to_view_pie_%d"%(viewnum)
	#

	fig = {
	  "data": [
	    {
	      "values": list_values,
	      "labels": list_lables,
	      "domain": {"x": [0, 1]},
	      "name": strName,
	      "hoverinfo":"label+percent+name",
	      "hole": .4,
	      "type": "pie"
	    }],
	  "layout": {
	        "title":"'微信指数'-'%s'"%strName,
	        "annotations": [
	            {
	                "font": {
	                    "size": 30
	                },
	                "showarrow": False,
	                "text": strName,
	                "x": 0.50,
	                "y": 0.5
	            }
	        ]
	    }
	}



	plotly.offline.plot(fig, filename='view_html/%s.html'%myfilename)
	#py.iplot(fig, filename='grouped-bar')
	print 'No.%d Completed'%viewnum
	viewnum +=1