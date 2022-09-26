
import re
import json

with open(FILENAME, mode='r', encoding="utf8") as f:
    msgs = json.load(f)


texts = []
replies = []


for i in range(0,len(msgs) - 1):

    if msgs[i]['sender'] != msgs[i+1]['sender'] and 'text' in msgs[i] and 'text' in msgs[i+1]:

       if "\"" not in msgs[i]['text'] and "\"" not in msgs[i+1]['text'] and "'" not in msgs[i]['text'] and "'" not in msgs[i+1]['text'] and "\n" not in msgs[i]['text'] and "\n" not in msgs[i+1]['text']:
        texts.append(msgs[i+1]['text'])
        replies.append(msgs[i]['text'])

def print_no_newline(string):
    import sys
    sys.stdout.write(string)
    sys.stdout.flush()

for i in range(0, len(texts)):
    print_no_newline( "\"" + texts[i] + "\"" + ", ")
