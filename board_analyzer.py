#encoding=big5
import os
import jieba
from collections import defaultdict

all_word_map = defaultdict(int)

jieba.set_dictionary('dict.txt.big.txt')


exclude_table = [' ', '�A'.decode('big5'),'��'.decode('big5'),'[','�C'.decode('big5'),'=','�w'.decode('big5'),'.','/','�O'.decode('big5'),'�F'.decode('big5'),'��'.decode('big5'),'m','�b'.decode('big5'),'1','�]'.decode('big5'),'�N'.decode('big5'),'��'.decode('big5'),'�u','�v','�|'.decode('big5'),'��'.decode('big5'),'�L'.decode('big5'),'�H'.decode('big5'),'�n'.decode('big5'),'��'.decode('big5')]


for subdir, dirs, files in os.walk(os.path.join(os.getcwd(), "P_mike1026915")): # P_mike1026915 is board name

    for file in files:
        file_full_path = os.path.join(subdir, file)

        content = open(file_full_path, 'rb').read()

        try:
            data = content.split("\n")
            data = data[3:]
            handled_data = []
            for d in data:
                d.strip()
                if d.startswith(u'�@��'.encode('big5')) or d.startswith(u'�ɶ�'.encode('big5')) or  d.startswith(u'���D'.encode('big5')) \
                    or  d.startswith(u'��'.encode('big5')) or d.startswith(u'<'.encode('big5')):
                    continue
                if not d.endswith('--'):
                    if len(d) != 0 and d:
                        handled_data.append(d)
                else:
                    break
        except BaseException:
            #print content
            pass
        try:
            words = jieba.cut(''.join(handled_data).decode('big5'), cut_all=False)
        except BaseException as e:
            #print ''.join(handled_data)
            pass



        for word in words:
            if word.isdigit():
                continue
                
            if not word.isalpha():
                continue
                
            if word in exclude_table:
                continue 
               
            if len(word) == 1:
                continue
            
            all_word_map[word] += 1
            
    
all_pair = list(all_word_map.iteritems())
all_pair.sort(key=lambda x: x[1], reverse=True)
for i in range(1000):
    print i+1, all_pair[i][0], all_pair[i][1]
