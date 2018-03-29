'2018-03-24'
'redis  介绍'

'''缓存数据库介绍



 NoSQL(NoSQL = Not Only SQL )，意即“不仅仅是SQL”，泛指非关系型的数据库,随着互联网web2.0网站的兴起，
 传统的关系数据库在应付web2.0网站，特别是超大规模和高并发的SNS类型的web2.0纯动态网站已经显得力不从心，暴露了很多难以克服的问题，
 而非关系型的数据库则由于其本身的特点得到了非常迅速的发展。NoSQL数据库的产生就是为了解决大规模数据集合多重数据种类带来的挑战，
 尤其是大数据应用难题。
NoSQL数据库的四大分类



键值(Key-Value)存储数据库
这一类数据库主要会使用到一个哈希表，这个表中有一个特定的键和一个指针指向特定的数据。Key/value模型对于IT系统来说的优势在于简单、
易部署。但是如果DBA只对部分值进行查询或更新的时候，Key/value就显得效率低下了。[3]  举例如：Tokyo Cabinet/Tyrant, Redis,
Voldemort, Oracle BDB.



列存储数据库。
这部分数据库通常是用来应对分布式存储的海量数据。键仍然存在，但是它们的特点是指向了多个列。这些列是由列家族来安排的。
如：Cassandra, HBase, Riak.




文档型数据库
文档型数据库的灵感是来自于Lotus Notes办公软件的，而且它同第一种键值存储相类似。该类型的数据模型是版本化的文档，
半结构化的文档以特定的格式存储，比如JSON。文档型数据库可 以看作是键值数据库的升级版，允许之间嵌套键值。
而且文档型数据库比键值数据库的查询效率更高。如：CouchDB, MongoDb. 国内也有文档型数据库SequoiaDB，已经开源。




图形(Graph)数据库
图形结构的数据库同其他行列以及刚性结构的SQL数据库不同，它是使用灵活的图形模型，并且能够扩展到多个服务器上。
NoSQL数据库没有标准的查询语言(SQL)，因此进行数据库查询需要制定数据模型。许多NoSQL数据库都有REST式的数据接口或者查询API。[2]
  如：Neo4J, InfoGrid, Infinite Graph.
因此，我们总结NoSQL数据库在以下的这几种情况下比较适用：1、数据模型比较简单；2、需要灵活性更强的IT系统；
3、对数据库性能要求较高；4、不需要高度的数据一致性；5、对于给定key，比较容易映射复杂值的环境。'''



'''redis
介绍

redis是业界主流的key-value nosql 数据库之一。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，redis支持各种不同方式的排序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。
Redis优点

    异常快速 : Redis是非常快的，每秒可以执行大约110000设置操作，81000个/每秒的读取操作。

    支持丰富的数据类型 : Redis支持最大多数开发人员已经知道如列表，集合，可排序集合，哈希等数据类型。
    这使得在应用中很容易解决的各种问题，因为我们知道哪些问题处理使用哪种数据类型更好解决。

    操作都是原子的 : 所有 Redis 的操作都是原子，从而确保当两个客户同时访问 Redis 服务器得到的是更新后的值（最新值）。
    MultiUtility工具：Redis是一个多功能实用工具，可以在很多如：缓存，消息传递队列中使用（Redis原生支持发布/订阅），在应用程序中，如：Web应用程序会话，网站页面点击数等任何短暂的数据；

安装Redis环境
要在 Ubuntu 上安装 Redis，打开终端，然后输入以下命令：

$sudo apt-get update
$sudo apt-get install redis-server

这将在您的计算机上安装Redis

启动 Redis

$redis-server

查看 redis 是否还在运行

$redis-cli

这将打开一个 Redis 提示符，如下图所示：

redis 127.0.0.1:6379>

在上面的提示信息中：127.0.0.1 是本机的IP地址，6379是 Redis 服务器运行的端口。现在输入 PING 命令，如下图所示：

redis 127.0.0.1:6379> ping
PONG

这说明现在你已经成功地在计算机上安装了 Redis。

Python操作Redis


sudo pip install redis
or
sudo easy_install redis
or
源码安装

详见：https://github.com/WoLpH/redis-py

　　
在Ubuntu上安装Redis桌面管理器

要在Ubuntu 上安装 Redis桌面管理，可以从 http://redisdesktop.com/download 下载包并安装它。
Redis 桌面管理器会给你用户界面来管理 Redis 键和数据。


Redis API使用

redis-py 的API的使用可以分类为：

    连接方式
    连接池
    操作
        String 操作
        Hash 操作
        List 操作
        Set 操作
        Sort Set 操作
    管道
    发布订阅
'''
'''
Redis 简介

Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

Redis 与其他 key - value 缓存产品有以下三个特点：

    Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
    Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
    Redis支持数据的备份，即master-slave模式的数据备份。

Redis 优势

    性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
    丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
    原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
    丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

Redis与其他key-value存储有什么不同？

    Redis有着更为复杂的数据结构并且提供对他们的原子性操作，这是一个不同于其他数据库的进化路径。Redis的数据类型都是基于基本数据结构的同时对程序员透明，无需进行额外的抽象。

    Redis运行在内存中但是可以持久化到磁盘，所以在对不同数据集进行高速读写时需要权衡内存，因为数据量不能大于硬件内存。在内存数据库方面的另一个优点是，相比在磁盘上相同的复杂的数据结构，在内存中操作起来非常简单，这样Redis可以做很多内部复杂性很强的事情。同时，在磁盘格式方面他们是紧凑的以追加的方式产生的，因为他们并不需要进行随机访问。

Redis 教程
Redis 安装
2 篇笔记


      参考地址
    什么是BSD协议？

    BSD开源协议是一个给于使用者很大自由的协议。可以自由的使用，修改源代码，也可以将修改后的代码作为开源或者专有软件再发布。当你发布使用了BSD协议的代码，或者以BSD协议代码为基础做二次开发自己的产品时，需要满足三个条件：
        如果再发布的产品中包含源代码，则在源代码中必须带有原来代码中的BSD协议。
        如果再发布的只是二进制类库/软件，则需要在类库/软件的文档和版权声明中包含原来代码中的BSD协议。
        不可以用开源代码的作者/机构名字和原来产品的名字做市场推广。

    BSD代码鼓励代码共享，但需要尊重代码作者的著作权。BSD由于允许使用者修改和重新发布代码，也允许使用或在BSD代码上开发商业软件发布和销 售，因此是对商业集成很友好的协议。

    很多的公司企业在选用开源产品的时候都首选BSD协议，因为可以完全控制这些第三方的代码，在必要的时候可以修改或者 二次开发。'''

'''什么是原子性,什么是原子性操作？

举个例子：

A想要从自己的帐户中转1000块钱到B的帐户里。那个从A开始转帐，到转帐结束的这一个过程，称之为一个事务。在这个事务里，要做如下操作：

    1. 从A的帐户中减去1000块钱。如果A的帐户原来有3000块钱，现在就变成2000块钱了。
    2. 在B的帐户里加1000块钱。如果B的帐户如果原来有2000块钱，现在则变成3000块钱了。

如果在A的帐户已经减去了1000块钱的时候，忽然发生了意外，比如停电什么的，导致转帐事务意外终止了，而此时B的帐户里还没有增加1000块钱。那么，我们称这个操作失败了，要进行回滚。回滚就是回到事务开始之前的状态，也就是回到A的帐户还没减1000块的状态，B的帐户的原来的状态。此时A的帐户仍然有3000块，B的帐户仍然有2000块。

我们把这种要么一起成功（A帐户成功减少1000，同时B帐户成功增加1000），要么一起失败（A帐户回到原来状态，B帐户也回到原来状态）的操作叫原子性操作。

如果把一个事务可看作是一个程序,它要么完整的被执行,要么完全不执行。这种特性就叫原子性。'''


'''Ubuntu 下安装

在 Ubuntu 系统安装 Redis 可以使用以下命令:

$sudo apt-get update
$sudo apt-get install redis-server

启动 Redis

$ redis-server

查看 redis 是否启动？

$ redis-cli

以上命令将打开以下终端：

redis 127.0.0.1:6379>

127.0.0.1 是本机 IP ，6379 是 redis 服务端口。现在我们输入 PING 命令。

redis 127.0.0.1:6379> ping
PONG

以上说明我们已经成功安装了redis。'''


'''Mac 下安装

 1. 官网http://redis.io/ 下载最新的稳定版本,这里是3.2.0

 2. sudo mv 到 /usr/local/

 3. sudo tar -zxf redis-3.2.0.tar 解压文件

 4. 进入解压后的目录 cd redis-3.2.0

 5. sudo make test 测试编译

 6. sudo make install

chenming

   chenming

  203***5172@qq.com

  参考地址

   mengjun

  813***532@qq.com

mac 下安装也可以使用 homebrew，homebrew 是 mac 的包管理器。

1、执行 brew install redis

2、启动 redis，可以使用后台服务启动 brew services start redis。或者直接启动：redis-server /usr/local/etc/redis.conf
mengjun

   mengjun

  813***532@qq.com
9个月前 (07-03)'''



'''什么是守护进程？

守护进程（Daemon Process），也就是通常说的 Daemon 进程（精灵进程），是 Linux 中的后台服务进程。它是一个生存期较长的进程，
通常独立于控制终端并且周期性地执行某种任务或等待处理某些发生的事件。

守护进程是个特殊的孤儿进程，这种进程脱离终端，为什么要脱离终端呢？之所以脱离于终端是为了避免进程被任何终端所产生的信息所打断
，其在执行过程中的信息也不在任何终端上显示。由于在 linux 中，每一个系统与用户进行交流的界面称为终端，
每一个从此终端开始运行的进程都会依附于这个终端
，这个终端就称为这些进程的控制终端，当控制终端被关闭时，相应的进程都会自动关闭。'''

'''
Redis 数据类型

Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。
String（字符串）

string是redis最基本的类型，你可以理解成与Memcached一模一样的类型，一个key对应一个value。

string类型是二进制安全的。意思是redis的string可以包含任何数据。比如jpg图片或者序列化的对象 。

string类型是Redis最基本的数据类型，一个键最大能存储512MB。
实例

redis 127.0.0.1:6379> SET name "runoob"
OK
redis 127.0.0.1:6379> GET name
"runoob"

在以上实例中我们使用了 Redis 的 SET 和 GET 命令。键为 name，对应的值为 runoob。

注意：一个键最大能存储512MB。
Hash（哈希）

Redis hash 是一个键值(key=>value)对集合。

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。
实例

redis> HMSET myhash field1 "Hello" field2 "World"
"OK"
redis> HGET myhash field1
"Hello"
redis> HGET myhash field2
"World"

以上实例中 hash 数据类型存储了包含用户脚本信息的用户对象。 实例中我们使用了 Redis HMSET, HGETALL 命令，user:1 为键值。
每个 hash 可以存储 232 -1 键值对（40多亿）。

List（列表）

Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）。
实例

redis 127.0.0.1:6379> lpush runoob redis
(integer) 1
redis 127.0.0.1:6379> lpush runoob mongodb
(integer) 2
redis 127.0.0.1:6379> lpush runoob rabitmq
(integer) 3
redis 127.0.0.1:6379> lrange runoob 0 10
1) "rabitmq"
2) "mongodb"
3) "redis"
redis 127.0.0.1:6379>

列表最多可存储 232 - 1 元素 (4294967295, 每个列表可存储40多亿)。
Set（集合）

Redis的Set是string类型的无序集合。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。
sadd 命令

添加一个string元素到,key对应的set集合中，成功返回1,如果元素已经在集合中返回0,key对应的set不存在返回错误。

sadd key member

实例

redis 127.0.0.1:6379> sadd runoob redis
(integer) 1
redis 127.0.0.1:6379> sadd runoob mongodb
(integer) 1
redis 127.0.0.1:6379> sadd runoob rabitmq
(integer) 1
redis 127.0.0.1:6379> sadd runoob rabitmq
(integer) 0
redis 127.0.0.1:6379> smembers runoob

1) "rabitmq"
2) "mongodb"
3) "redis"

注意：以上实例中 rabitmq 添加了两次，但根据集合内元素的唯一性，第二次插入的元素将被忽略。

集合中最大的成员数为 232 - 1(4294967295, 每个集合可存储40多亿个成员)。
zset(sorted set：有序集合)
Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

zset的成员是唯一的,但分数(score)却可以重复。
zadd 命令

添加元素到集合，元素在集合中存在则更新对应score

zadd key score member

实例

redis 127.0.0.1:6379> zadd runoob 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabitmq
(integer) 0
redis 127.0.0.1:6379> > ZRANGEBYSCORE runoob 0 1000
1) "mongodb"
2) "rabitmq"
3) "redis"

'''


'''
Redis 命令

Redis 命令用于在 redis 服务上执行操作。

要在 redis 服务上执行命令需要一个 redis 客户端。Redis 客户端在我们之前下载的的 redis 的安装包中。
语法

Redis 客户端的基本语法为：

$ redis-cli

实例

以下实例讲解了如何启动 redis 客户端：

启动 redis 客户端，打开终端并输入命令 redis-cli。该命令会连接本地的 redis 服务。

$redis-cli
redis 127.0.0.1:6379>
redis 127.0.0.1:6379> PING

PONG

在以上实例中我们连接到本地的 redis 服务并执行 PING 命令，该命令用于检测 redis 服务是否启动。
在远程服务上执行命令

如果需要在远程 redis 服务上执行命令，同样我们使用的也是 redis-cli 命令。
语法

$ redis-cli -h host -p port -a password

实例

以下实例演示了如何连接到主机为 127.0.0.1，端口为 6379 ，密码为 mypass 的 redis 服务上。

$redis-cli -h 127.0.0.1 -p 6379 -a "mypass"
redis 127.0.0.1:6379>
redis 127.0.0.1:6379> PING

PONG

'''


'''
Redis 键(key)

Redis 键命令用于管理 redis 的键。
语法

Redis 键命令的基本语法如下：

redis 127.0.0.1:6379> COMMAND KEY_NAME

实例

redis 127.0.0.1:6379> SET runoobkey redis
OK
redis 127.0.0.1:6379> DEL runoobkey
(integer) 1

在以上实例中 DEL 是一个命令， runoobkey 是一个键。 如果键被删除成功，命令执行后输出 (integer) 1，否则将输出 (integer) 0
Redis keys 命令

下表给出了与 Redis 键相关的基本命令：
序号	命令及描述
1	DEL key
该命令用于在 key 存在时删除 key。
2	DUMP key
序列化给定 key ，并返回被序列化的值。
3	EXISTS key
检查给定 key 是否存在。
4	EXPIRE key seconds
为给定 key 设置过期时间。
5	EXPIREAT key timestamp
EXPIREAT 的作用和 EXPIRE 类似，都用于为 key 设置过期时间。 不同在于 EXPIREAT 命令接受的时间参数是 UNIX 时间戳(unix timestamp)。
6	PEXPIRE key milliseconds
设置 key 的过期时间以毫秒计。
7	PEXPIREAT key milliseconds-timestamp
设置 key 过期时间的时间戳(unix timestamp) 以毫秒计
8	KEYS pattern
查找所有符合给定模式( pattern)的 key 。
9	MOVE key db
将当前数据库的 key 移动到给定的数据库 db 当中。
10	PERSIST key
移除 key 的过期时间，key 将持久保持。
11	PTTL key
以毫秒为单位返回 key 的剩余的过期时间。
12	TTL key
以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。
13	RANDOMKEY
从当前数据库中随机返回一个 key 。
14	RENAME key newkey
修改 key 的名称
15	RENAMENX key newkey
仅当 newkey 不存在时，将 key 改名为 newkey 。
16	TYPE key
返回 key 所储存的值的类型。

更多命令请参考：https://redis.io/commands
'''

'''Redis 字符串(String)

Redis 字符串数据类型的相关命令用于管理 redis 字符串值，基本语法如下：
语法

redis 127.0.0.1:6379> COMMAND KEY_NAME

实例

redis 127.0.0.1:6379> SET runoobkey redis
OK
redis 127.0.0.1:6379> GET runoobkey
"redis"

在以上实例中我们使用了 SET 和 GET 命令，键为 runoobkey。
Redis 字符串命令

下表列出了常用的 redis 字符串命令：
序号	命令及描述
1	SET key value
设置指定 key 的值
2	GET key
获取指定 key 的值。
3	GETRANGE key start end
返回 key 中字符串值的子字符
4	GETSET key value
将给定 key 的值设为 value ，并返回 key 的旧值(old value)。
5	GETBIT key offset
对 key 所储存的字符串值，获取指定偏移量上的位(bit)。
6	MGET key1 [key2..]
获取所有(一个或多个)给定 key 的值。
7	SETBIT key offset value
对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)。
8	SETEX key seconds value
将值 value 关联到 key ，并将 key 的过期时间设为 seconds (以秒为单位)。
9	SETNX key value
只有在 key 不存在时设置 key 的值。
10	SETRANGE key offset value
用 value 参数覆写给定 key 所储存的字符串值，从偏移量 offset 开始。
11	STRLEN key
返回 key 所储存的字符串值的长度。
12	MSET key value [key value ...]
同时设置一个或多个 key-value 对。
13	MSETNX key value [key value ...]
同时设置一个或多个 key-value 对，当且仅当所有给定 key 都不存在。
14	PSETEX key milliseconds value
这个命令和 SETEX 命令相似，但它以毫秒为单位设置 key 的生存时间，而不是像 SETEX 命令那样，以秒为单位。
15	INCR key
将 key 中储存的数字值增一。
16	INCRBY key increment
将 key 所储存的值加上给定的增量值（increment） 。
17	INCRBYFLOAT key increment
将 key 所储存的值加上给定的浮点增量值（increment） 。
18	DECR key
将 key 中储存的数字值减一。
19	DECRBY key decrement
key 所储存的值减去给定的减量值（decrement） 。
20	APPEND key value
如果 key 已经存在并且是一个字符串， APPEND 命令将 指定value 追加到改 key 原来的值（value）的末尾。 '''



'''Redis 哈希(Hash)

Redis hash 是一个string类型的field和value的映射表，hash特别适合用于存储对象。

Redis 中每个 hash 可以存储 232 - 1 键值对（40多亿）。
实例

127.0.0.1:6379>  HMSET runoobkey name "redis tutorial" description "redis basic commands for caching" likes 20 visitors 23000
OK
127.0.0.1:6379>  HGETALL runoobkey
1) "name"
2) "redis tutorial"
3) "description"
4) "redis basic commands for caching"
5) "likes"
6) "20"
7) "visitors"
8) "23000"

在以上实例中，我们设置了 redis 的一些描述信息(name, description, likes, visitors) 到哈希表的 runoobkey 中。'''


'''Redis 列表(List)

Redis列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

一个列表最多可以包含 232 - 1 个元素 (4294967295, 每个列表超过40亿个元素)。
实例

redis 127.0.0.1:6379> LPUSH runoobkey redis
(integer) 1
redis 127.0.0.1:6379> LPUSH runoobkey mongodb
(integer) 2
redis 127.0.0.1:6379> LPUSH runoobkey mysql
(integer) 3
redis 127.0.0.1:6379> LRANGE runoobkey 0 10

1) "mysql"
2) "mongodb"
3) "redis"

在以上实例中我们使用了 LPUSH 将三个值插入了名为 runoobkey 的列表当中。'''


'''Redis 集合(Set)

Redis 的 Set 是 String 类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

Redis 中集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是 O(1)。

集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。
实例

redis 127.0.0.1:6379> SADD runoobkey redis
(integer) 1
redis 127.0.0.1:6379> SADD runoobkey mongodb
(integer) 1
redis 127.0.0.1:6379> SADD runoobkey mysql
(integer) 1
redis 127.0.0.1:6379> SADD runoobkey mysql
(integer) 0
redis 127.0.0.1:6379> SMEMBERS runoobkey

1) "mysql"
2) "mongodb"
3) "redis"

在以上实例中我们通过 SADD 命令向名为 runoobkey 的集合插入的三个元素。'''


'''Redis 有序集合(sorted set)

Redis 有序集合和集合一样也是string类型元素的集合,且不允许重复的成员。

不同的是每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。

有序集合的成员是唯一的,但分数(score)却可以重复。

集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1)。 集合中最大的成员数为 232 - 1 (4294967295, 每个集合可存储40多亿个成员)。
实例

redis 127.0.0.1:6379> ZADD runoobkey 1 redis
(integer) 1
redis 127.0.0.1:6379> ZADD runoobkey 2 mongodb
(integer) 1
redis 127.0.0.1:6379> ZADD runoobkey 3 mysql
(integer) 1
redis 127.0.0.1:6379> ZADD runoobkey 3 mysql
(integer) 0
redis 127.0.0.1:6379> ZADD runoobkey 4 mysql
(integer) 0
redis 127.0.0.1:6379> ZRANGE runoobkey 0 10 WITHSCORES

1) "redis"
2) "1"
3) "mongodb"
4) "2"
5) "mysql"
6) "4"

在以上实例中我们通过命令 ZADD 向 redis 的有序集合中添加了三个值并关联上分数。'''



'''Redis HyperLogLog

Redis 在 2.8.9 版本添加了 HyperLogLog 结构。

Redis HyperLogLog 是用来做基数统计的算法，HyperLogLog 的优点是，在输入元素的数量或者体积非常非常大时，计算基数所需的空间总是固定 的、并且是很小的。

在 Redis 里面，每个 HyperLogLog 键只需要花费 12 KB 内存，就可以计算接近 2^64 个不同元素的基 数。这和计算基数时，元素越多耗费内存就越多的集合形成鲜明对比。

但是，因为 HyperLogLog 只会根据输入元素来计算基数，而不会储存输入元素本身，所以 HyperLogLog 不能像集合那样，返回输入的各个元素。
什么是基数?

比如数据集 {1, 3, 5, 7, 5, 7, 8}， 那么这个数据集的基数集为 {1, 3, 5 ,7, 8}, 基数(不重复元素)为5。 基数估计就是在误差可接受的范围内，快速计算基数。
实例

以下实例演示了 HyperLogLog 的工作过程：

redis 127.0.0.1:6379> PFADD runoobkey "redis"

1) (integer) 1

redis 127.0.0.1:6379> PFADD runoobkey "mongodb"

1) (integer) 1

redis 127.0.0.1:6379> PFADD runoobkey "mysql"

1) (integer) 1

redis 127.0.0.1:6379> PFCOUNT runoobkey

(integer) 3'''


'''Redis 发布订阅

Redis 发布订阅(pub/sub)是一种消息通信模式：发送者(pub)发送消息，订阅者(sub)接收消息。

Redis 客户端可以订阅任意数量的频道。

下图展示了频道 channel1 ， 以及订阅这个频道的三个客户端 —— client2 、 client5 和 client1 之间的关系：
pubsub1

当有新消息通过 PUBLISH 命令发送给频道 channel1 时， 这个消息就会被发送给订阅它的三个客户端：
pubsub2
实例

以下实例演示了发布订阅是如何工作的。在我们实例中我们创建了订阅频道名为 redisChat:

redis 127.0.0.1:6379> SUBSCRIBE redisChat

Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "redisChat"
3) (integer) 1

现在，我们先重新开启个 redis 客户端，然后在同一个频道 redisChat 发布两次消息，订阅者就能接收到消息。

redis 127.0.0.1:6379> PUBLISH redisChat "Redis is a great caching technique"

(integer) 1

redis 127.0.0.1:6379> PUBLISH redisChat "Learn redis by runoob.com"

(integer) 1

# 订阅者的客户端会显示如下消息
1) "message"
2) "redisChat"
3) "Redis is a great caching technique"
1) "message"
2) "redisChat"
3) "Learn redis by runoob.com"

Redis 发布订阅命令

''''''

下表列出了 redis 发布订阅常用命令：
序号	命令及描述
1	PSUBSCRIBE pattern [pattern ...]
订阅一个或多个符合给定模式的频道。
2	PUBSUB subcommand [argument [argument ...]]
查看订阅与发布系统状态。
3	PUBLISH channel message
将信息发送到指定的频道。
4	PUNSUBSCRIBE [pattern [pattern ...]]
退订所有给定模式的频道。
5	SUBSCRIBE channel [channel ...]
订阅给定的一个或多个频道的信息。
6	UNSUBSCRIBE [channel [channel ...]]
指退订给定的频道。'''

'''Redis 事务

Redis 事务可以一次执行多个命令， 并且带有以下两个重要的保证：

    批量操作在发送 EXEC 命令前被放入队列缓存。
    收到 EXEC 命令后进入事务执行，事务中任意命令执行失败，其余的命令依然被执行。
    在事务执行过程，其他客户端提交的命令请求不会插入到事务执行命令序列中。

一个事务从开始到执行会经历以下三个阶段：

    开始事务。
    命令入队。
    执行事务。

实例

以下是一个事务的例子， 它先以 MULTI 开始一个事务， 然后将多个命令入队到事务中， 最后由 EXEC 命令触发事务， 一并执行事务中的所有命令：

redis 127.0.0.1:6379> MULTI
OK

redis 127.0.0.1:6379> SET book-name "Mastering C++ in 21 days"
QUEUED

redis 127.0.0.1:6379> GET book-name
QUEUED

redis 127.0.0.1:6379> SADD tag "C++" "Programming" "Mastering Series"
QUEUED

redis 127.0.0.1:6379> SMEMBERS tag
QUEUED

redis 127.0.0.1:6379> EXEC
1) OK
2) "Mastering C++ in 21 days"
3) (integer) 3
4) 1) "Mastering Series"
   2) "C++"
   3) "Programming"

单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务的执行并不是原子性的。

事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。

    这是官网上的说明 From redis docs on transactions:

    It's important to note that even when a command fails, all the other commands in the queue are processed – Redis will not stop the processing of commands.

比如：

redis 127.0.0.1:7000> multi
OK
redis 127.0.0.1:7000> set a aaa
QUEUED
redis 127.0.0.1:7000> set b bbb
QUEUED
redis 127.0.0.1:7000> set c ccc
QUEUED
redis 127.0.0.1:7000> exec
1) OK
2) OK
3) OK

如果在 set b bbb 处失败，set a 已成功不会回滚，set c 还会继续执行。
Redis 事务命令

下表列出了 redis 事务的相关命令：
序号	命令及描述
1	DISCARD
取消事务，放弃执行事务块内的所有命令。
2	EXEC
执行所有事务块内的命令。
3	MULTI
标记一个事务块的开始。
4	UNWATCH
取消 WATCH 命令对所有 key 的监视。
5	WATCH key [key ...]
监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。v'''


'''
Redis 脚本

Redis 脚本使用 Lua 解释器来执行脚本。 Reids 2.6 版本通过内嵌支持 Lua 环境。执行脚本的常用命令为 EVAL。
语法

Eval 命令的基本语法如下：

redis 127.0.0.1:6379> EVAL script numkeys key [key ...] arg [arg ...]

实例

以下实例演示了 redis 脚本工作过程：

redis 127.0.0.1:6379> EVAL "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}" 2 key1 key2 first second

1) "key1"
2) "key2"
3) "first"
4) "second"

Redis 脚本命令

下表列出了 redis 脚本常用命令：
序号	命令及描述
1	EVAL script numkeys key [key ...] arg [arg ...]
执行 Lua 脚本。
2	EVALSHA sha1 numkeys key [key ...] arg [arg ...]
执行 Lua 脚本。
3	SCRIPT EXISTS script [script ...]
查看指定的脚本是否已经被保存在缓存当中。
4	SCRIPT FLUSH
从脚本缓存中移除所有脚本。
5	SCRIPT KILL
杀死当前正在运行的 Lua 脚本。
6	SCRIPT LOAD script
将脚本 script 添加到脚本缓存中，但并不立即执行这个脚本。
'''

'''Redis 连接

Redis 连接命令主要是用于连接 redis 服务。
实例

以下实例演示了客户端如何通过密码验证连接到 redis 服务，并检测服务是否在运行：

redis 127.0.0.1:6379> AUTH "password"
OK
redis 127.0.0.1:6379> PING
PONG

Redis 连接命令

下表列出了 redis 连接的基本命令：
序号	命令及描述
1	AUTH password
验证密码是否正确
2	ECHO message
打印字符串
3	PING
查看服务是否运行
4	QUIT
关闭当前连接
5	SELECT index
切换到指定的数据库'''

'''
Redis 数据备份与恢复

Redis SAVE 命令用于创建当前数据库的备份。
语法

redis Save 命令基本语法如下：

redis 127.0.0.1:6379> SAVE

实例

redis 127.0.0.1:6379> SAVE
OK

该命令将在 redis 安装目录中创建dump.rdb文件。
恢复数据
如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可。获取 redis 目录可以使用 CONFIG 命令，如下所示：


redis 127.0.0.1:6379> CONFIG GET dir
1) "dir"
2) "/usr/local/redis/bin"

以上命令 CONFIG GET dir 输出的 redis 安装目录为 /usr/local/redis/bin。
Bgsave

创建 redis 备份文件也可以使用命令 BGSAVE，该命令在后台执行。
实例

127.0.0.1:6379> BGSAVE

Background saving started

'''

'''
Redis 安全

我们可以通过 redis 的配置文件设置密码参数，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的 redis 服务更安全。
实例

我们可以通过以下命令查看是否设置了密码验证：

127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) ""

默认情况下 requirepass 参数是空的，这就意味着你无需通过密码验证就可以连接到 redis 服务。

你可以通过以下命令来修改该参数：

127.0.0.1:6379> CONFIG set requirepass "runoob"
OK
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) "runoob"

设置密码后，客户端连接 redis 服务就需要密码验证，否则无法执行命令。
语法

AUTH 命令基本语法格式如下：

127.0.0.1:6379> AUTH password

实例

127.0.0.1:6379> AUTH "runoob"
OK
127.0.0.1:6379> SET mykey "Test value"
OK
127.0.0.1:6379> GET mykey
"Test value"

'''


'''Redis 客户端连接

Redis 通过监听一个 TCP 端口或者 Unix socket 的方式来接收来自客户端的连接，当一个连接建立后，Redis 内部会进行以下一些操作：

    首先，客户端 socket 会被设置为非阻塞模式，因为 Redis 在网络事件处理上采用的是非阻塞多路复用模型。
    然后为这个 socket 设置 TCP_NODELAY 属性，禁用 Nagle 算法
    然后创建一个可读的文件事件用于监听这个客户端 socket 的数据发送

最大连接数

在 Redis2.4 中，最大连接数是被直接硬编码在代码里面的，而在2.6版本中这个值变成可配置的。

maxclients 的默认值是 10000，你也可以在 redis.conf 中对这个值进行修改。

config get maxclients

1) "maxclients"
2) "10000"

实例

以下实例我们在服务启动时设置最大连接数为 100000：

redis-server --maxclients 100000

客户端命令
S.N.	命令	描述
1 	CLIENT LIST 	返回连接到 redis 服务的客户端列表
2 	CLIENT SETNAME 	设置当前连接的名称
3 	CLIENT GETNAME 	获取通过 CLIENT SETNAME 命令设置的服务名称
4 	CLIENT PAUSE 	挂起客户端连接，指定挂起的时间以毫秒计
5 	CLIENT KILL 	关闭客户端连接'''


'''
Java 使用 Redis
安装

开始在 Java 中使用 Redis 前， 我们需要确保已经安装了 redis 服务及 Java redis 驱动，且你的机器上能正常使用 Java。 Java的安装配置可以参考我们的 Java开发环境配置 接下来让我们安装 Java redis 驱动：

    首先你需要下载驱动包 下载 jedis.jar，确保下载最新驱动包。
    在你的 classpath 中包含该驱动包。

    本站提供了 2.9.0 jar 版本下载： jedis-2.9.0.jar

连接到 redis 服务
实例
import redis.clients.jedis.Jedis;

public class RedisJava {
    public static void main(String[] args) {
        //连接本地的 Redis 服务
        Jedis jedis = new Jedis("localhost");
        System.out.println("连接成功");
        //查看服务是否运行
        System.out.println("服务正在运行: "+jedis.ping());
    }
}

编译以上 Java 程序，确保驱动包的路径是正确的。

连接成功
服务正在运行: PONG

Redis Java String(字符串) 实例
实例
import redis.clients.jedis.Jedis;

public class RedisStringJava {
    public static void main(String[] args) {
        //连接本地的 Redis 服务
        Jedis jedis = new Jedis("localhost");
        System.out.println("连接成功");
        //设置 redis 字符串数据
        jedis.set("runoobkey", "www.runoob.com");
        // 获取存储的数据并输出
        System.out.println("redis 存储的字符串为: "+ jedis.get("runoobkey"));
    }
}

编译以上程序。

连接成功
redis 存储的字符串为: www.runoob.com

Redis Java List(列表) 实例
实例
import java.util.List;
import redis.clients.jedis.Jedis;

public class RedisListJava {
    public static void main(String[] args) {
        //连接本地的 Redis 服务
        Jedis jedis = new Jedis("localhost");
        System.out.println("连接成功");
        //存储数据到列表中
        jedis.lpush("site-list", "Runoob");
        jedis.lpush("site-list", "Google");
        jedis.lpush("site-list", "Taobao");
        // 获取存储的数据并输出
        List<String> list = jedis.lrange("site-list", 0 ,2);
        for(int i=0; i<list.size(); i++) {
            System.out.println("列表项为: "+list.get(i));
        }
    }
}

编译以上程序。

连接成功
列表项为: Taobao
列表项为: Google
列表项为: Runoob

Redis Java Keys 实例
实例
import java.util.Iterator;
import java.util.Set;
import redis.clients.jedis.Jedis;

public class RedisKeyJava {
    public static void main(String[] args) {
        //连接本地的 Redis 服务
        Jedis jedis = new Jedis("localhost");
        System.out.println("连接成功");

        // 获取数据并输出
        Set<String> keys = jedis.keys("*");
        Iterator<String> it=keys.iterator() ;
        while(it.hasNext()){
            String key = it.next();
            System.out.println(key);
        }
    }
}

编译以上程序。

连接成功
runoobkey
site-list

'''