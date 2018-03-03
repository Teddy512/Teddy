# -*- coding: utf-8 -*-
#    authon:teddy

'2.装饰器'

'你是一家视频网站的后端开发工程师，你们网站有以下几个版块'


def home():
    print("---首页----")

def america():
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

def henan():
    print("----河南专区----")

'''视频刚上线初期，为了吸引用户，你们采取了免费政策，所有视频免费观看，
迅速吸引了一大批用户，免费一段时间后，每天巨大的带宽费用公司承受不了了，
所以准备对比较受欢迎的几个版块收费，其中包括“欧美” 和 “河南”专区，你拿到这个需求后，想了想，
想收费得先让其进行用户认证，认证通过后，再判定这个用户是否是VIP付费会员就可以了，是VIP就让看，
不是VIP就不让看就行了呗。 你觉得这个需求很是简单，因为要对多个版块进行认证，那应该把认证功能提取出来单独写个模块，
然后每个版块里调用 就可以了，与是你轻轻的就实现了下面的功能 。'''




'版本1'
user_status = False #用户登录了就把这个改成True

def login():
    _username = "alex" #假装这是DB里存的用户信息
    _password = "abc!23" #假装这是DB里存的用户信息
    global user_status

    if user_status == False:
        username = input("user:")
        password = input("pasword:")

        if username == _username and password == _password:
            print("welcome login....")
            user_status = True
        else:
            print("wrong username or password!")
    else:
        print("用户已登录，验证通过...")

def home():
    print("---首页----")

def america():
    login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

def henan():
    login() #执行前加上验证
    print("----河南专区----")



home()
america()
henan()


'''此时你信心满满的把这个代码提交给你的TEAM LEADER审核，没成想，没过5分钟，代码就被打回来了， TEAM LEADER给你反馈是，
我现在有很多模块需要加认证模块，你的代码虽然实现了功能，但是需要更改需要加认证的各个模块的代码，
这直接违反了软件开发中的一个原则“开放-封闭”原则，简单来说，它规定已经实现的功能代码不允许被修改，但可以被扩展，即：

    封闭：已实现的功能代码块不应该被修改
    开放：对现有功能的扩展开放

这个原则你还是第一次听说，我擦，再次感受了自己这个野生程序员与正规军的差距，
BUT ANYWAY,老大要求的这个怎么实现呢？如何在不改原有功能代码的情况下加上认证功能呢？你一时想不出思路，
只好带着这个问题回家继续憋，媳妇不在家，去隔壁老王家串门了，你正好落的清静，一不小心就想到了解决方案，不改源代码可以呀，

你师从沙河金角大王时，记得他教过你，高阶函数，就是把一个函数当做一个参数传给另外一个函数，当时大王说，
有一天，你会用到它的，没想到这时这个知识点突然从脑子 里蹦出来了，我只需要写个认证方法，每次调用 需要验证的功能 时
，直接 把这个功能 的函数名当做一个参数 传给 我的验证模块不就行了么，哈哈，机智如我，如是你啪啪啪改写了之前的代码'''


'版本2'
user_status = False #用户登录了就把这个改成True

def login(func): #把要执行的模块从这里传进来
    _username = "alex" #假装这是DB里存的用户信息
    _password = "abc!23" #假装这是DB里存的用户信息
    global user_status

    if user_status == False:
        username = input("user:")
        password = input("pasword:")

        if username == _username and password == _password:
            print("welcome login....")
            user_status = True
        else:
            print("wrong username or password!")

    if user_status == True:
        func() # 看这里看这里，只要验证通过了，就调用相应功能

def home():
    print("---首页----")

def america():
    #login() #执行前加上验证
    print("----欧美专区----")

def japan():
    print("----日韩专区----")

def henan():
    #login() #执行前加上验证
    print("----河南专区----")



home()
login(america) #需要验证就调用 login，把需要验证的功能 当做一个参数传给login
# home()
# america()
login(henan)







'版本3'
def login(func): #把要执行的模块从这里传进来

    def inner():#再定义一层函数
        _username = "alex" #假装这是DB里存的用户信息
        _password = "abc!23" #假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func() # 看这里看这里，只要验证通过了，就调用相应功能

    return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数



'版本4'
user_status = False #用户登录了就把这个改成True

def login(func): #把要执行的模块从这里传进来

    def inner(*args,**kwargs):#再定义一层函数
        _username = "alex" #假装这是DB里存的用户信息
        _password = "abc!23" #假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能

    return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数


def home():
    print("---首页----")

@login
def america():
    #login() #执行前加上验证
    print("----美专区----")

def japan():
    print("----韩专区----")

# @login
def henan(style):
    '''
    :param style: 喜欢看什么类型的，就传进来
    :return:
    '''
    #login() #执行前加上验证
    print("----河南专区----")

home()
# america = login(america) #你在这里相当于把america这个函数替换了
henan = login(henan)

# #那用户调用时依然写
america()

henan("39")







'版本4'
user_status = False #用户登录了就把这个改成True

def login(auth_type): #把要执行的模块从这里传进来
    def auth(func):
        def inner(*args,**kwargs):#再定义一层函数
            if auth_type == "qq":
                _username = "alex" #假装这是DB里存的用户信息
                _password = "abc!23" #假装这是DB里存的用户信息
                global user_status

                if user_status == False:
                    username = input("user:")
                    password = input("pasword:")

                    if username == _username and password == _password:
                        print("welcome login....")
                        user_status = True
                    else:
                        print("wrong username or password!")

                if user_status == True:
                    return func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
            else:
                print("only support qq ")
        return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

    return auth

def home():
    print("---首页----")

@login('qq')
def america():
    #login() #执行前加上验证
    print("----美专区----")

def japan():
    print("----韩专区----")

@login('weibo')
def henan(style):
    '''
    :param style: 喜欢看什么类型的，就传进来
    :return:
    '''
    #login() #执行前加上验证
    print("----河南专区----")

home()
# america = login(america) #你在这里相当于把america这个函数替换了
#henan = login(henan)

# #那用户调用时依然写
america()

# henan("3p")


'''4.软件目录结构规范
为什么要设计好目录结构?

"设计项目目录结构"，就和"代码编码风格"一样，属于个人风格问题。对于这种风格上的规范，一直都存在两种态度:

    一类同学认为，这种个人风格问题"无关紧要"。理由是能让程序work就好，风格问题根本不是问题。
    另一类同学认为，规范化能更好的控制程序结构，让程序具有更高的可读性。

我是比较偏向于后者的，因为我是前一类同学思想行为下的直接受害者。我曾经维护过一个非常不好读的项目，其实现的逻辑并不复杂，但是却耗费了我非常长的时间去理解它想表达的意思。从此我个人对于提高项目可读性、可维护性的要求就很高了。"项目目录结构"其实也是属于"可读性和可维护性"的范畴，我们设计一个层次清晰的目录结构，就是为了达到以下两点:

    可读性高: 不熟悉这个项目的代码的人，一眼就能看懂目录结构，知道程序启动脚本是哪个，测试目录在哪儿，配置文件在哪儿等等。从而非常快速的了解这个项目。
    可维护性高: 定义好组织规则后，维护者就能很明确地知道，新增的哪个文件和代码应该放在什么目录之下。这个好处是，随着时间的推移，代码/配置的规模增加，项目结构不会混乱，仍然能够组织良好。

所以，我认为，保持一个层次清晰的目录结构是有必要的。更何况组织一个良好的工程目录，其实是一件很简单的事儿。
目录组织方式

关于如何组织一个较好的Python工程目录结构，已经有一些得到了共识的目录结构。在Stackoverflow的这个问题上，能看到大家对Python目录结构的讨论。

这里面说的已经很好了，我也不打算重新造轮子列举各种不同的方式，这里面我说一下我的理解和体会。

假设你的项目名为foo, 我比较建议的最方便快捷目录结构这样就足够了:

Foo/
|-- bin/
|   |-- foo
|
|-- foo/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- docs/
|   |-- conf.py
|   |-- abc.rst
|
|-- setup.py
|-- requirements.txt
|-- README

简要解释一下:

    bin/: 存放项目的一些可执行文件，当然你可以起名script/之类的也行。
    foo/: 存放项目的所有源代码。(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。(2) 其子目录tests/存放单元测试代码； (3) 程序的入口最好命名为main.py。
    docs/: 存放一些文档。
    setup.py: 安装、部署、打包的脚本。
    requirements.txt: 存放软件依赖的外部Python包列表。
    README: 项目说明文件。

除此之外，有一些方案给出了更加多的内容。比如LICENSE.txt,ChangeLog.txt文件等，我没有列在这里，因为这些东西主要是项目开源的时候需要用到。如果你想写一个开源软件，目录该如何组织，可以参考这篇文章。

下面，再简单讲一下我对这些目录的理解和个人要求吧。
关于README的内容

这个我觉得是每个项目都应该有的一个文件，目的是能简要描述该项目的信息，让读者快速了解这个项目。

它需要说明以下几个事项:

    软件定位，软件的基本功能。
    运行代码的方法: 安装环境、启动命令等。
    简要的使用说明。
    代码目录结构说明，更详细点可以说明软件的基本原理。
    常见问题说明。

我觉得有以上几点是比较好的一个README。在软件开发初期，由于开发过程中以上内容可能不明确或者发生变化，并不是一定要在一开始就将所有信息都补全。但是在项目完结的时候，是需要撰写这样的一个文档的。

可以参考Redis源码中Readme的写法，这里面简洁但是清晰的描述了Redis功能和源码结构。
关于requirements.txt和setup.py
setup.py

一般来说，用setup.py来管理代码的打包、安装、部署问题。业界标准的写法是用Python流行的打包工具setuptools来管理这些事情。这种方式普遍应用于开源项目中。不过这里的核心思想不是用标准化的工具来解决这些问题，而是说，一个项目一定要有一个安装部署工具，能快速便捷的在一台新机器上将环境装好、代码部署好和将程序运行起来。

这个我是踩过坑的。

我刚开始接触Python写项目的时候，安装环境、部署代码、运行程序这个过程全是手动完成，遇到过以下问题:

    安装环境时经常忘了最近又添加了一个新的Python包，结果一到线上运行，程序就出错了。
    Python包的版本依赖问题，有时候我们程序中使用的是一个版本的Python包，但是官方的已经是最新的包了，通过手动安装就可能装错了。
    如果依赖的包很多的话，一个一个安装这些依赖是很费时的事情。
    新同学开始写项目的时候，将程序跑起来非常麻烦，因为可能经常忘了要怎么安装各种依赖。

setup.py可以将这些事情自动化起来，提高效率、减少出错的概率。"复杂的东西自动化，能自动化的东西一定要自动化。"是一个非常好的习惯。

setuptools的文档比较庞大，刚接触的话，可能不太好找到切入点。学习技术的方式就是看他人是怎么用的，可以参考一下Python的一个Web框架，flask是如何写的: setup.py

当然，简单点自己写个安装脚本（deploy.sh）替代setup.py也未尝不可。
requirements.txt

这个文件存在的目的是:

    方便开发者维护软件的包依赖。将开发过程中新增的包添加进这个列表中，避免在setup.py安装依赖时漏掉软件包。
    方便读者明确项目使用了哪些Python包。

这个文件的格式是每一行包含一个包依赖的说明，通常是flask>=0.10这种格式，要求是这个格式能被pip识别，这样就可以简单的通过 pip install -r requirements.txt来把所有Python包依赖都装好了。具体格式说明： 点这里。


关于配置文件的使用方法
注意，在上面的目录结构中，没有将conf.py放在源码目录下，而是放在docs/目录下。

很多项目对配置文件的使用做法是:

    配置文件写在一个或多个python文件中，比如此处的conf.py。
    项目中哪个模块用到这个配置文件就直接通过import conf这种形式来在代码中使用配置。

这种做法我不太赞同:

    这让单元测试变得困难（因为模块内部依赖了外部配置）
    另一方面配置文件作为用户控制程序的接口，应当可以由用户自由指定该文件的路径。
    程序组件可复用性太差，因为这种贯穿所有模块的代码硬编码方式，使得大部分模块都依赖conf.py这个文件。
'''
'''
所以，我认为配置的使用，更好的方式是，

    模块的配置都是可以灵活配置的，不受外部配置文件的影响。
    程序的配置也是可以灵活控制的。

能够佐证这个思想的是，用过nginx和mysql的同学都知道，nginx、mysql这些程序都可以自由的指定用户配置。

所以，不应当在代码中直接import conf来使用配置文件。上面目录结构中的conf.py，是给出的一个配置样例，不是在写死在程序中直接引用的配置文件。可以通过给main.py启动参数指定配置路径的方式来让程序读取配置内容。当然，这里的conf.py你可以换个类似的名字，比如settings.py。或者你也可以使用其他格式的内容来编写配置文件，比如settings.yaml之类的。
'''