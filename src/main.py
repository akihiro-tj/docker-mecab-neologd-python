import MeCab

text = "あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。"

tagger = MeCab.Tagger(
    "-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd")
node = tagger.parseToNode(text)

while node:
    print(node.feature)
    node = node.next
