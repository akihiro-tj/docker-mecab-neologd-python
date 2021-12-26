# Docker + MeCab + mecab-ipadic-NEologd + Python

## Build

~~~bash
$ docker build . -t mecab-python
~~~


## Run

~~~bash
$ docker run -v $(pwd)/src:/opt/app --rm -it mecab-python /bin/bash
~~~

~~~
root@f196f1576c8d:/opt/app# python main.py
~~~
