from flask import Flask
import time
import numpy as np
from re_utils import *
from utils import read_vocab, process_content, pridect, stop_words, seg, clean_txt, fast_pridect
import os
import json
from flask import Flask,request, Response, render_template
app = Flask(__name__)
app.config.from_object('settings.Development')
app.config['SECRET_KEY'] = os.urandom(24)
max_content_len = 2000

words, word_to_id = read_vocab()

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/api/class', endpoint="class_method", methods=["POST"])
def class_method():
    content = request.json.get("content", "")
    contents = content.lower().replace('\n', '')
    #contents = seg(content.lower().replace('\n', ''), stop_words(), apply=clean_txt)
    while contents:
        content = contents[0:max_content_len]
        print(len(content))
        test_vec = process_content(content, word_to_id)
        res = pridect(test_vec)
        print(res)
        if res[0] == 0:
            type_ = '小说'
        else:
            type_ = '非小说'
            break
        print(type_)
        contents = contents[max_content_len:]
    res = {"message": type_}
    return Response(json.dumps(res), content_type='application/json')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899)
