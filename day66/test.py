import requests

params = {
    "include": "data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,attachment,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,is_labeled,paid_info,paid_info_content,reaction_instruction,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_recognized;data[*].mark_infos[*].url;data[*].author.follower_count,vip_info,badge[*].topics;data[*].settings.table_of_content.enabled",
    "limit": "5", "offset": "10", "platform": "desktop", "sort_by": "default"}

url = 'https://www.zhihu.com/api/v4/questions/24744812/answers?'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    'cookie': '_zap=f95f6387-c978-4d68-a7e8-89fa5c7f94e9; d_c0="AKDfjPcGlBSPTs_xJ_CRtRZKJXZnAetkWvQ=|1646311321"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=%2Bt5p5EZMThFBEEQEEVc%2F%2FoZzjGdpUzUE; _xsrf=zmho8lW3dHbiVN8kVmm1TptXEzHnMhQ4; __snaker__id=goM9onN3Fowmkndx; gdxidpyhxdE=WD6VXQjfn6dlDg1eMzEhrRInM%2F8EZTbrf%2FBOCWesIdIIsByOb7%2FVAHywl%5Clzhieg%2F4Y7CTi4IQ%2BKXBuu5XhJ3Vsu%2BiZWBOc8XQULmkaMB4%2BC6adhnZnqWhUcQzvv%5CK02%2BfZqcOO2Ub0u0kchxz049o4%2FivArtXHAKfvUY5HbpHvwQYqB%3A1651160788849; YD00517437729195%3AWM_NI=3XFVrlTaFlBgjiGTGOgThZv7T1b1HPVnzzM8sYRSfodnTsR%2By%2FIDQPi0nASgNw70Mm8dIdRV3OKHvDf8fLen5tAmZ9%2FChwbipzYMLxM0hxtytRsMmjx1c6wTSdR%2BzmA9WkI%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed4d366b09a8195f75cad868bb2d44e969e8bb1c55e98ec8fd9e55be996a9b8e82af0fea7c3b92af1888ab7f16898bf8a8dc16daab789b5c645a58ca8bbf53d98efaed2cb5c96b2b69bd034b1879eb4e565a8b29c94d121bbf187a5d45cabf0a2a2d26d8ea9f9d1d067fcbc8785d15ef19185a9f550a6e8aaade866f7ac8f8ed933ed9da898e163b4a697aecf748ff0a899f773b88ebdaef062bcefadd7f66091bc9eccf96783e7998ccc37e2a3; z_c0=2|1:0|10:1651159902|4:z_c0|92:Mi4xYXhrUkFBQUFBQUFBb04tTTl3YVVGQ1lBQUFCZ0FsVk5YZ0ZZWXdEYnROSnlYQ3ZBcVg2ZktOR2pObU1vV1FNVnFB|e6babbf8e46218474d417a237c9ac27197bfc2cf1790ee9a98107eded7b43e43; q_c1=71f85b60e4494524838436e1a39d9d51|1651159902000|1651159902000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1655484073,1655514572,1655601534,1655737773; NOT_UNREGISTER_WAITING=1; SESSIONID=EiXGMzxGj1dy3BuQWe9x2K2z5BbKcujAVAQ6JEj1Ahy; JOID=W1kVCkokvFS_SJUMZCScze226al5adQF8A3ndSpGhTHPc99xNHAS5d1InARlLzXtBgYIHPNME_q2gI6gWWFdcJE=; osd=UVESA0sutFO2SZ8EYy2dx-Wx4KhzYdMM8QfvciNHjznIet57PHcb5NdAmw1kJT3qDwcCFPRFEvC-h4ehU2laeZA=; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1655746855; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1655746918|1655744088',
    'referer': 'https://www.zhihu.com/question/24744812',
}

resp = requests.get(url, headers=headers, params=params)
print(resp.json())
