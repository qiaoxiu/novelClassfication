
import urllib.request
import pymysql
import os
import ssl
import asyncio
ssl._create_default_https_context = ssl._create_unverified_context

conn = pymysql.connect(
             host="10.60.0.221",
             port=3306,
                 user="root",password="123456",
                     database="abcd",
                         charset="utf8")

cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示


# sql = "SELECT pdf_url from entity_res_clip WHERE resource_format in ('DOC', 'DOCX', 'PPT', 'PPTX') and status=1 LIMIT 10"
# cursor.execute(sql)
# res = cursor.fetchall()
# FILE_DIR = "data/"
# cursor.close()
# conn.close()


def download_pdf(url):
    index = url.rindex("/")
    pdf_name = url[index + 1:]
    file_path = os.path.join(FILE_DIR, pdf_name)
    urllib.request.urlretrieve(url, file_path)


def main():
    for url in res:
        url = url[0]
        print(url)
        download_pdf(url)

from urllib.request import urlopen
def get_file(url):
    response = urlopen(url)
    chunk = 16 * 1024
    index = url.rindex("/")
    pdf_name = url[index + 1:]
    file_path = os.path.join(FILE_DIR, pdf_name)
    with open(file_path, 'wb') as f:
        while True:
            chunk = response.read(chunk)
            if not chunk:
                break
            f.write(chunk)
if __name__ == '__main__':
    get_file("https://pd.okjiaoyu.cn/pd_w_io1ptz6858.pdf")






