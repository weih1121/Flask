### vitualenv

Mac os X或者linux安装:

```shell
sudo easy_install virtualenv
sudo pip install virtualenv
```

Ubuntu

```shell
sudo apt-get install python-virtualenv
```

Windows

```shell
pip install virtualenv
```

---

激活虚拟环境

OS X或者Linux

```shell
virtualenv venv
. venv/bin/activate
```

Widows

```shell
virtualenv venv			#在指定目录下创建虚拟环境
venv\scripts\activate	#激活虚拟环境
```

```shell
C:\Users\H\test>virtualenv venv
Using base prefix 'c:\\program files\\python36'
New python executable in C:\Users\H\test\venv\Scripts\python.exe
Installing setuptools, pip, wheel...done.

C:\Users\H\test>venv\scripts\activate

(venv) C:\Users\H\test>
```

虚拟环境中安装包

```shell
pip install pac_name
```

----

安装最新版本的Flask两种方法:

1.git check

```shell
$ git clone http://github.com/mitsuhiko/flask.git
Initialized empty Git repository in ~/dev/flask/.git/
$ cd flask
$ virtualenv venv --distribute
New python executable in venv/bin/python
Installing distribute............done.
$ . venv/bin/activate
$ python setup.py develop
...
Finished processing dependencies for Flask
```

2.使用pip直接下载最新版本的包