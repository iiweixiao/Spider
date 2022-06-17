import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
import aiofiles
from Crypto.Cipher import AES
import os


def get_iframe_url(url):
    resp = requests.get(url)
    main_page = BeautifulSoup(resp.text, "html.parser")
    iframe = main_page.find("iframe")
    resp.close()
    return iframe.get("src")


def get_first_m3u8_url(iframe_url):
    iframe_resp = requests.get(iframe_url)
    obj = re.compile(r'var main = "(?P<first_m3u8>.*?)"', re.S)
    result = obj.search(iframe_resp.text)
    iframe_resp.close()
    return result.group('first_m3u8').strip()


def download_m3u8_file(url, name):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    with open(name, mode="w", encoding="utf-8") as f:
        f.write(resp.text)
    resp.close()


async def download_ts(session, url, name):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video3/{name}", mode="wb") as f:
            await f.write(await resp.content.read())
    print(f"{name}~OK!")


async def aio_download(up_url):
    tasks = []
    async with aiofiles.open("第⼆层_tmp_m3u8.txt", mode="r", encoding="utf-8") as f:
        async with aiohttp.ClientSession() as session:
            async for line in f:
                if line.startswith("#"):
                    continue

                line = line.strip()
                ts_url = up_url + "/" + line
                name = line
                # 将异步任务添加到列表
                tasks.append(download_ts(session, ts_url, name))
            # 开炮!!
            await asyncio.wait(tasks)


def get_key(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    key = resp.text
    resp.close()
    return key


async def dec_ts(name, key):
    aes = AES.new(key=key, IV=b"0000000000000000", mode=AES.MODE_CBC)
    async with aiofiles.open("video3" + "/" + name, mode="rb") as f1, aiofiles.open("video4" + "/" + "tmp_" + name,
                                                                                    mode="wb") as f2:
        bs = await f1.read()
        await f2.write(aes.decrypt(bs))
    print(f"{name}~解密OK~")


async def aio_dec(key):
    tasks = []
    async with aiofiles.open("第⼆层_tmp_m3u8.txt", mode="r", encoding="utf-8") as f:
        async for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            tasks.append(dec_ts(line, key))
        # 异步解密
        await asyncio.wait(tasks)


def merge_ts():
    s = []
    with open("第⼆层_tmp_m3u8.txt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            s.append("./video4/tmp_" + line)
    names = " ".join(s)
    os.system(f"cat {names} > movie.mp4")


# 主程序
def main(url):
    iframe_url = get_iframe_url(url)

    # 1. iframe的域名
    iframe_domain = iframe_url.split("/share/")[0]

    # 2. 拿到m3u8地址(顶级)
    first_m3u8_url = get_first_m3u8_url(iframe_url)

    # 3.1 下载first_m3u8
    first_m3u8_url = iframe_domain + first_m3u8_url
    download_m3u8_file(first_m3u8_url, "顶层_tmp_m3u8.txt")
    # 3.2 拿到m3u8的上层url, ⽬的是拼接第⼆层m3u8的url以及后⾯的key.key等等
    first_m3u8_url_up = first_m3u8_url.rsplit("/", 1)[0]
    # 3.3 下载第⼆层m3u8⽂件
    with open("顶层_tmp_m3u8.txt", mode="r", encoding='utf-8') as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                second_m3u8_url = first_m3u8_url_up + "/" + line.strip()
                download_m3u8_file(second_m3u8_url, "第⼆层_tmp_m3u8.txt")

    # 4. 读取第⼆层m3u8⽂件. 开始下载ts
    second_m3u8_url_up = second_m3u8_url.rsplit("/", 1)[0]
    # 异步下载
    asyncio.run(aio_download(second_m3u8_url_up))
    # 测试的时候慎重啊

    # 5. 解密与合并
    # 5.1. 拿到key
    key = get_key(second_m3u8_url_up + "/key.key")  # 这⾥就不去m3u8⾥找了.偷个懒
    # print(key)
    # key = "c5878c26baaaac8c"
    # 5.2. 解密
    asyncio.run(aio_dec(key))
    # 5.3. 合并
    merge_ts()


if __name__ == '__main__':
    url = "https://www.91kanju.com/vod-play/541-2-1.html"
    main(url)
