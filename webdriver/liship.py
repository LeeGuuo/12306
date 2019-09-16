import requests
import re, os, time
from urllib.request import urlretrieve

# 获取页面源代码 获取视频ID
# 拼接URL地址
# 获取完整的视频播放URL
# 下载视频


def download_video():
    '''
    获取视频
    '''
    # 获取页面源代码
    header = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64)'
    }
    page_url = 'https://www.pearvideo.com/category_1'
    res = requests.get(url=page_url, headers=header)
    res.encoding = 'utf-8'
    html = res.text
    reg = r'<a href="(.*?)" class="vervideo-lilink actplay">'
    viode_ids = re.findall(reg, html)
    # print(viode_ids)

    # 拼接URL
    viode_url = []
    start_url = 'https://www.pearvideo.com/'
    for viode_id in viode_ids:
        new_url = start_url + viode_id
        viode_url.append(new_url)

    # 此处可以处理下拉翻页功能

    # 获取完整URL地址
    for play_url in viode_url:
        play_html = requests.get(url=play_url, headers=header)
        play_html.encoding = 'utf-8'
        play_html = play_html.text
        reg = r'srcUrl="(.*?)",vdoUrl'
        url = re.findall(reg, play_html)
        reg = r'<h1 class="video-tt">(.*?)</h1>'
        name = re.findall(reg, play_html)
        print("正在下载>>> %s" % name[0])
        path = 'video'
        if path not in os.listdir():
            os.mkdir(path)

        # 下载视频
        time.sleep(1)
        filepath = path + '%s.mp4' % name[0]
        urlretrieve(url[0], filepath)
        print("下载地址>>> %s" % url[0])


if __name__ == "__main__":
    # 匹配新闻等相关视频
    download_video()


