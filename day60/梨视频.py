import requests

# 梨视频旅行频道任意一个内容的地址
url = 'https://www.pearvideo.com/video_1759234'
contID = url.split('_')[1]  # 提取video_后的数字

real_api = f'https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.1487451470844272'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Referer': f'https://www.pearvideo.com/video_{contID}',
}

resp = requests.get(real_api, headers=headers)
print(resp.json()['videoInfo']['videos']['srcUrl'].replace(resp.json()['systemTime'], f'cont-{contID}'))
link = resp.json()['videoInfo']['videos']['srcUrl'].replace(resp.json()['systemTime'], f'cont-{contID}')

with open(f'{contID}.mp4', 'wb') as f:
    f.write(requests.get(link).content)

'''
参考：

# 防盗链
Referer: https://www.pearvideo.com/video_1765321

# 真实视频地址
https://video.pearvideo.com/mp4/third/20220614/cont-1765321-15498275-151733-hd.mp4
'''

