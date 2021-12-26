# Docker + MeCab + mecab-ipadic-NEologd + Python

## Build

~~~
$ docker build . -t mecab-python
~~~


## Run Docker

### Mac

~~~
$ docker run -v $(pwd)/src:/opt/app --rm -it mecab-python /bin/bash
~~~


### Windows Command Prompt

~~~
C:\...\docker-mecab-neologd-python> docker run -v %cd%/src:/opt/app --rm -it mecab-python bash
~~~


### Windows PowerShell

~~~
PS C:\...\docker-mecab-neologd-python> docker run -v $pwd/src:/opt/app --rm -it mecab-python bash
~~~


## Run Python

~~~
root@f196f1576c8d:/opt/app# python main.py
~~~
