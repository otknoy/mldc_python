#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import MeCab


def mecab(filename):
    words = []
    f = open(filename, 'r')
    m = MeCab.Tagger('-Ochasen')
    for line in f:
        node = m.parseToNode(line)
        while node:
            w = {'surface': node.surface,
                 'feature': node.feature,
                 'posid': node.posid}
            words.append(w)
            node = node.next
    f.close()
    return words

def extract_noun(words):
    posids = [38] + range(41, 47) # noun id
    nouns = [w for w in words if w['posid'] in posids]
    return nouns

def term_frequency(words):
    tf = {}
    for n in words:
        term = n['surface']
        if not tf.has_key(term):
            tf[term] = 0
        tf[term] += 1
    return tf

def to_tag_cloud(tf):
    contents = ["<font size=" + str(int(math.sqrt(f))) + ">" + t + "</font>" for t, f in tf.items()]
    return """
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <title>Tag Cloud</title>
  </head>
  <body>
%s
  </body>
</html>""" % '\n'.join(contents)


if __name__ == '__main__':
    filename = sys.argv[1]

    words = mecab(filename)
    nouns = extract_noun(words)

    tf = term_frequency(nouns)

    f = open('tag_cloud.html', 'w')
    f.write(to_tag_cloud(tf))
    f.close()
