from gevent import monkey
monkey.patch_all()
import requests
from multiprocessing.dummy import Pool
from lxml import etree
import gevent

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
def get_url(url):
    response = requests.get(url=url,headers=headers).text
    tree = etree.HTML(response)
    li_list = tree.xpath('//*[@id="index_ajax_list"]/li')
    g_list=[]
    for li in li_list:
        href = li.xpath('./a/@href')[0]
        g = gevent.spawn(down_url,href)
        g_list.append(g)
    gevent.joinall(g_list)
def down_url(href):
    r = requests.get(href,headers).text
    e = etree.HTML(r)
    img_list = e.xpath('//*[@id="image_div"]/p/img')
    g2_list=[]
    for img in img_list:
        src_url =  img.xpath('./@src')[0]
        g2 = gevent.spawn(down_each_url,src_url)
        g2_list.append(g2)
    gevent.joinall(g2_list)
def down_each_url(src_url):
    print(src_url)
if __name__ == '__main__':

    url_list=[]
    for i in range(1,22):
        urls = f'http://www.mntuxiu.com/page/{i}/'
        url_list.append(urls)
    pool = Pool(5)
    pool.map(get_url,url_list)




