import tensorflow.keras as kr
import tensorflow as tf
from types import MethodType, FunctionType
import re
import jieba
import fasttext.FastText as fasttext
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from cnn_model import TCNNConfig, TextCNN
save_dir = 'checkpoints/textcnn2'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径
model_path = "all.1_dim300_lr05_iter15.model"
classifier = fasttext.load_model(model_path)

def clean_txt(raw):
    fil = re.compile(r"[^0-9a-zA-Z\u4e00-\u9fa5]+")
    return fil.sub(' ', raw)

def seg(sentence, sw, apply=None):
    if isinstance(apply, FunctionType) or isinstance(apply, MethodType):
        sentence = apply(sentence)
    return ' '.join([i for i in jieba.cut(sentence) if i.strip() and i not in sw])


def stop_words():
    with open('stopwords.txt', 'r', encoding='utf-8') as swf:
        return [line.strip() for line in swf]

def open_file(filename, mode='r'):
    return open(filename, mode, encoding="utf-8")

def native_content(content):
    #return content.decode('gbk')
    return content

def read_vocab(vocab_dir="vocab.txt"):

    # words = open_file(vocab_dir).read().strip().split('\n')
    with open_file(vocab_dir) as fp:
        # 如果是py2 则每个值都转化为unicode
        words = [native_content(_.strip()) for _ in fp.readlines()]
        # for _ in fp.readlines():
        #     print(_)
        #     words.append(native_content(_.strip()))
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id


def process_content(contents, word_to_id, max_length=2000):

    data_id = []
    data_id.append([word_to_id[x] for x in contents if x in word_to_id])

    # 使用keras提供的pad_sequences来将文本pad为固定长度
    x_pad = kr.preprocessing.sequence.pad_sequences(data_id, max_length)
    return x_pad


config = TCNNConfig()
# words, word_to_id = read_vocab(vocab_dir)
# config.vocab_size = len(words)
model = TextCNN(config)

session = tf.Session()
session.run(tf.global_variables_initializer())
saver = tf.train.Saver()
saver.restore(sess=session, save_path=save_path)  # 读取保存的模型


def pridect(x_test):
    feed_dict = {
        model.input_x: x_test,
        model.keep_prob: 1.0
    }
    # model.y_pred_cls
    return session.run(model.y_pred_cls, feed_dict=feed_dict)

def fast_pridect(content):
    predict = classifier.predict([content], k=2)
    label = predict[0][0][0].replace("__label__", "")
    print('----label----', label)
    if label =='小说':
        return 0
    else:
        return 1
