'''
将pdf转换成文本文件
'''
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import os
TARGET_DIR = 'data1'
SAVE_DIR = 'save'
def read_pdf(pdf):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 获取所有行
    lines = str(content).split("\n")
    lines = [line.strip() for line in lines]
    text = " ".join(lines)
    return text


def get_text():
    files = [f for f in os.listdir(TARGET_DIR)]
    for file in files:
        with open(os.path.join(TARGET_DIR, file), "rb") as my_pdf:
            try:
                text = read_pdf(my_pdf)
            except Exception:
                print('error file:', file)

        if text:
            print(file)
            file_path = '{}/{}'.format(SAVE_DIR, file.replace("pdf", "txt"))
            with open(file_path, "w") as ff:
                ff.write(text)

if __name__ == '__main__':
    get_text()
