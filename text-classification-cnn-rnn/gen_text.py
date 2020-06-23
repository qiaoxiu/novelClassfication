import os
TARGET_DIR = '/Users/admin/Downloads/111/'

files = [f for f in os.listdir(TARGET_DIR)]
i=1
for file in files:
    # os.rename(TARGET_DIR+file, '{}{}.txt'.format(TARGET_DIR, i))
    # i += 1
    try:
        with open(os.path.join(TARGET_DIR, file), "r", encoding="gb18030") as f:
            lines = f.readlines()
            print(lines)
    except Exception as  e:
        print(e)
        lines = []
        # print(file)

    if lines:
        lines = [line.replace("\n", "").strip() for line in lines]
        text = ''.join(lines)
        if text:
            with open("xiaoshuo.txt", "a+", encoding="utf-8") as ff:
                ff.write(text)


# with open("/Users/admin/Downloads/111/UuTxt丹药大亨.txt", 'r', encoding="gb2312") as f:
#     lines = f.readlines()
#     print(lines)