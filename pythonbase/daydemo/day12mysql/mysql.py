''
'''本节内容



    数据库介绍
    mysql 数据库安装使用
    mysql管理
    mysql 数据类型
    常用mysql命令
        创建数据库
        外键
        增删改查表
        权限
    事务
    索引
    python 操作mysql
    ORM sqlachemy学习

1. 数据库介绍
什么是数据库？

数据库（Database）是按照数据结构来组织、存储和管理数据的仓库，
每个数据库都有一个或多个不同的API用于创建，访问，管理，搜索和复制所保存的数据。
我们也可以将数据存储在文件中，但是在文件中读写数据速度相对较慢。
所以，现在我们使用关系型数据库管理系统（RDBMS）来存储和管理的大数据量。所谓的关系型数据库，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。
RDBMS即关系数据库管理系统(Relational Database Management System)的特点：
1.数据以表格的形式出现
2.每行为各种记录名称
3.每列为记录名称所对应的数据域
4.许多的行和列组成一张表单
5.若干的表单组成database'''
'''RDBMS 术语

在我们开始学习MySQL 数据库前，让我们先了解下RDBMS的一些术语：

    数据库: 数据库是一些关联表的集合。.
    数据表: 表是数据的矩阵。在一个数据库中的表看起来像一个简单的电子表格。
    列: 一列(数据元素) 包含了相同的数据, 例如邮政编码的数据。
    行：一行（=元组，或记录）是一组相关的数据，例如一条用户订阅的数据。
    冗余：存储两倍数据，冗余可以使系统速度更快。(表的规范化程度越高，表与表之间的关系就越多；查询时可能经常需要在多个表之间进行连接查询；而进行连接操作会降低查询速度。例如，学生的信息存储在student表中，院系信息存储在department表中。通过student表中的dept_id字段与department表建立关联关系。如果要查询一个学生所在系的名称，必须从student表中查找学生所在院系的编号（dept_id），然后根据这个编号去department查找系的名称。如果经常需要进行这个操作时，连接查询会浪费很多的时间。因此可以在student表中增加一个冗余字段dept_name，该字段用来存储学生所在院系的名称。这样就不用每次都进行连接操作了。)
    主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
    外键：外键用于关联两个表。
    复合键：复合键（组合键）将多个列作为一个索引键，一般用于复合索引。
    索引：使用索引可快速访问数据库表中的特定信息。索引是对数据库表中一列或多列的值进行排序的一种结构。类似于书籍的目录。
    参照完整性: 参照的完整性要求关系中不允许引用不存在的实体。与实体完整性是关系模型必须满足的完整性约束条件，目的是保证数据的一致性。

Mysql数据库

Mysql是最流行的关系型数据库管理系统，在WEB应用方面MySQL是最好的RDBMS(Relational Database Management System：关系数据库管理系统)应用软件之一。由瑞典MySQL AB公司开发，目前属于Oracle公司。MySQL是一种关联数据库管理系统，关联数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

    Mysql是开源的，所以你不需要支付额外的费用。
    Mysql支持大型的数据库。可以处理拥有上千万条记录的大型数据库。
    MySQL使用标准的SQL数据语言形式。
    Mysql可以允许于多个系统上，并且支持多种语言。这些编程语言包括C、C++、Python、Java、Perl、PHP、Eiffel、Ruby和Tcl等。
    Mysql对PHP有很好的支持，PHP是目前最流行的Web开发语言。
    MySQL支持大型数据库，支持5000万条记录的数据仓库，32位系统表文件最大可支持4GB，64位系统支持最大的表文件为8TB。
    Mysql是可以定制的，采用了GPL协议，你可以修改源码来开发自己的Mysql系统。
'''

'''5. mysql 常用命令
MySQL 创建数据表

语法
1

CREATE TABLE table_name (column_name column_type);

创建一个student表

create table student(
   stu_id INT NOT NULL AUTO_INCREMENT,
   name CHAR(32) NOT NULL,
   age  INT NOT NULL,
   register_date DATE,
   PRIMARY KEY ( stu_id )
);

实例解析：

    如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
    AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
    PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。

MySQL 插入数据

语法

INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );

插入数据


mysql> insert into student (name,age,register_date) values ("alex li",22,"2016-03-4")
    -> ;
    insert into student (name,age,register_date) values("teddy",12,"2018-02-25")
Query OK, 1 row affected (0.00 sec)

mysql> select * from student;
+--------+---------+-----+---------------+
| stu_id | name    | age | register_date |
+--------+---------+-----+---------------+
|      1 | alex li |  22 | 2016-03-04    |
+--------+---------+-----+---------------+
1 row in set (0.00 sec)
MySQL 查询数据

语法

SELECT column_name,column_name
FROM table_name
[WHERE Clause]
[OFFSET M ][LIMIT N]

    查询语句中你可以使用一个或者多个表，表之间使用逗号(,)分割，并使用WHERE语句来设定查询条件。
    SELECT 命令可以读取一条或者多条记录。
    你可以使用星号（*）来代替其他字段，SELECT语句会返回表的所有字段数据
    你可以使用 WHERE 语句来包含任何条件。
    你可以通过OFFSET指定SELECT语句开始查询的数据偏移量。默认情况下偏移量为0。
    你可以使用 LIMIT 属性来设定返回的记录数。


mysql> select * from student limit 3 offset 2;
+--------+---------+-----+---------------+
| stu_id | name    | age | register_date |
+--------+---------+-----+---------------+
|      3 | alex li |  24 | 2016-03-04    |
|      4 | alex li |  24 | 2016-03-01    |
|      5 | alex li |  24 | 2016-03-02    |
+--------+---------+-----+---------------+
3 rows in set (0.00 sec)
比如这个SQL ，limit后面跟的是3条数据，offset后面是从第3条开始读取

mysql> select * from student limit 3 ,1;
+--------+---------+-----+---------------+
| stu_id | name    | age | register_date |
+--------+---------+-----+---------------+
|      4 | alex li |  24 | 2016-03-01    |
+--------+---------+-----+---------------+
1 row in set (0.00 sec)

而这个SQL，limit后面是从第3条开始读，读取1条信息。

　　
MySQL where 子句

语法
1
2

SELECT field1, field2,...fieldN FROM table_name1, table_name2...
[WHERE condition1 [AND [OR]] condition2.....

以下为操作符列表，可用于 WHERE 子句中。

下表中实例假定 A为10 B为20
操作符	描述	实例
= 	等号，检测两个值是否相等，如果相等返回true 	(A = B) 返回false。
<>, != 	不等于，检测两个值是否相等，如果不相等返回true 	(A != B) 返回 true。
> 	大于号，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true 	(A > B) 返回false。
< 	小于号，检测左边的值是否小于右边的值, 如果左边的值小于右边的值返回true 	(A < B) 返回 true。
>= 	大于等于号，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true 	(A >= B) 返回false。
<= 	小于等于号，检测左边的值是否小于于或等于右边的值, 如果左边的值小于或等于右边的值返回true 	(A <= B) 返回 true。

　　

使用主键来作为 WHERE 子句的条件查询是非常快速的。
1

select * from student where register_date > '2016-03-04';

　　
MySQL UPDATE 查询

语法
1
2

UPDATE table_name SET field1=new-value1, field2=new-value2
[WHERE Clause]
1

update student set age=22 ,name="Alex Li" where stu_id>3;
MySQL DELETE 语句

语法
1

DELETE FROM table_name [WHERE Clause]<br><br>delete from student where stu_id=5;
MySQL LIKE 子句

语法


SELECT field1, field2,...fieldN table_name1, table_name2...
WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'


select *from student where name binary like "%Li";
select *from student where name binary like  binary "%Li"; #只匹配大写
MySQL 排序


SELECT field1, field2,...fieldN table_name1, table_name2...
ORDER BY field1, [field2...] [ASC [DESC]]
使用 ASC 或 DESC 关键字来设置查询结果是按升序或降序排列。 默认情况下，它是按升序排列。
select *from student where name like binary "%Li" order by stu_id desc;
MySQL GROUP BY 语句　　


SELECT column_name, function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;

示例


mysql> SELECT * FROM employee_tbl;
+----+--------+---------------------+--------+
| id | name   | date                | singin |
+----+--------+---------------------+--------+
|  1 | 小明 | 2016-04-22 15:25:33 |      1 |
|  2 | 小王 | 2016-04-20 15:25:47 |      3 |
|  3 | 小丽 | 2016-04-19 15:26:02 |      2 |
|  4 | 小王 | 2016-04-07 15:26:14 |      4 |
|  5 | 小明 | 2016-04-11 15:26:40 |      4 |
|  6 | 小明 | 2016-04-04 15:26:54 |      2 |
+----+--------+---------------------+--------+

接下来我们使用 GROUP BY 语句 将数据表按名字进行分组，并统计每个人有多少条记录：
mysql> SELECT name, COUNT(*) FROM   employee_tbl GROUP BY name;
+--------+----------+
| name   | COUNT(*) |
+--------+----------+
| 小丽 |        1 |
| 小明 |        3 |
| 小王 |        2 |
+--------+----------+
3 rows in set (0.01 sec)

使用 WITH ROLLUP
mysql> SELECT name, SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------+--------------+
| name   | singin_count |
+--------+--------------+
| 小丽 |            2 |
| 小明 |            7 |
| 小王 |            7 |
| NULL   |           16 |
+--------+--------------+
4 rows in set (0.00 sec)
其中记录 NULL 表示所有人的登录次数。<br>
我们可以使用 coalesce 来设置一个可以取代 NUll 的名称，coalesce 语法：
mysql> SELECT coalesce(name, '总数'), SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
MySQL ALTER命令

我们需要修改数据表名或者修改数据表字段时，就需要使用到MySQL ALTER命令。

删除，添加或修改表字段
1

alter table student drop register_date; #从student表删除register_date   字段alter table student add phone int(11) not null; ＃添加phone字段

修改字段类型及名称

如果需要修改字段类型及名称, 你可以在ALTER命令中使用 MODIFY 或 CHANGE 子句 。

例如，把字段 c 的类型从 CHAR(1) 改为 CHAR(10)，可以执行以下命令:
1

mysql> ALTER TABLE testalter_tbl MODIFY c CHAR(10);

使用 CHANGE 子句, 语法有很大的不同。 在 CHANGE 关键字之后，紧跟着的是你要修改的字段名，然后指定新字段名及类型。尝试如下实例：
1
2
3

mysql> ALTER TABLE testalter_tbl CHANGE i j BIGINT;

mysql> ALTER TABLE testalter_tbl CHANGE j j INT;
ALTER TABLE 对 Null 值和默认值的影响

当你修改字段时，你可以指定是否包含只或者是否设置默认值。

以下实例，指定字段 j 为 NOT NULL 且默认值为100 。
1
2

mysql> ALTER TABLE testalter_tbl
    -> MODIFY j BIGINT NOT NULL DEFAULT 100;
修改表名
1

mysql> ALTER TABLE testalter_tbl RENAME TO alter_tbl;


关于主键

外键，一个特殊的索引，用于关键2个表，只能是指定内容　　


mysql> create table class(
    -> id  int not null primary key,
    -> name char(16));
Query OK, 0 rows affected (0.02 sec)


CREATE TABLE `student2` (
  `id` int(11) NOT NULL,
  `name` char(16) NOT NULL,
  `class_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_class_key` (`class_id`),
  CONSTRAINT `fk_class_key` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`)
)


此时如果class 表中不存在id 1,student表也插入不了，这就叫外键约束
mysql> insert into student2(id,name,class_id) values(1,'alex', 1);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`testdb`.`student2`, CONSTRAINT `fk_class_key` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`))



mysql> insert into class(id,name) values(1,"linux");
Query OK, 1 row affected (0.01 sec)

mysql> insert into student2(id,name,class_id) values(1,'alex', 1);
Query OK, 1 row affected (0.00 sec)


＃如果有student表中跟这个class表有关联的数据，你是不能删除class表中与其关联的纪录的
mysql> delete from class where id =1;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`testdb`.`student2`, CONSTRAINT `fk_class_key` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`))

　　

　　






MySQL NULL 值处理　　

我们已经知道MySQL使用 SQL SELECT 命令及 WHERE 子句来读取数据表中的数据,但是当提供的查询条件字段为 NULL 时，该命令可能就无法正常工作。
为了处理这种情况，MySQL提供了三大运算符:
IS NULL: 当列的值是NULL,此运算符返回true。
IS NOT NULL: 当列的值不为NULL, 运算符返回true。
<=>: 比较操作符（不同于=运算符），当比较的的两个值为NULL时返回true。
关于 NULL 的条件比较运算是比较特殊的。你不能使用 = NULL 或 != NULL 在列中查找 NULL 值 。
在MySQL中，NULL值与任何其它值的比较（即使是NULL）永远返回false，即 NULL = NULL 返回false 。
MySQL中处理NULL使用IS NULL和IS NOT NULL运算符。


Mysql 连接（left join, right join, inner join ,full join）

我们已经学会了如果在一张表中读取数据，这是相对简单的，但是在真正的应用中经常需要从多个数据表中读取数据。

本章节我们将向大家介绍如何使用 MySQL 的 JOIN 在两个或多个表中查询数据。

你可以在SELECT, UPDATE 和 DELETE 语句中使用 Mysql 的 JOIN 来联合多表查询。

JOIN 按照功能大致分为如下三类：

    INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
    LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
    RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。

Suppose you have two tables, with a single column each, and data as follows:　　


A    B
-    -
1    3
2    4
3    5
4    6

Inner join

An inner join using either of the equivalent queries gives the intersection of the two tables, i.e. the two rows they have in common.


select * from a INNER JOIN b on a.a = b.b;
select a.*,b.*  from a,b where a.a = b.b;

a | b
--+--
3 | 3
4 | 4

其实就是只显示2个表的交集

Left join

A left join will give all rows in A, plus any common rows in B.


select * from a LEFT JOIN b on a.a = b.b;

a |  b
--+-----
1 | null
2 | null
3 |    3
4 |    4

Right join

A right join will give all rows in B, plus any common rows in A.

select * from a RIGHT JOIN b on a.a = b.b;

a    |  b
-----+----
3    |  3
4    |  4
null |  5
null |  6

Full join

A full outer join will give you the union of A and B, i.e. all the rows in A and all the rows in B. If something in A doesn't have a corresponding datum in B, then the B portion is null, and vice versa


select * from a FULL JOIN b on a.a = b.b;

 a   |  b
-----+-----
   1 | null
   2 | null
   3 |    3
   4 |    4
null |    6
null |    5

　　

mysql 并不直接支持full join,but 总是难不到我们
+ View Code

　　
6. 事务

MySQL 事务主要用于处理操作量大，复杂度高的数据。比如说，在人员管理系统中，你删除一个人员，你即需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务！

    在MySQL中只有使用了Innodb数据库引擎的数据库或表才支持事务
    事务处理可以用来维护数据库的完整性，保证成批的SQL语句要么全部执行，要么全部不执行
    事务用来管理insert,update,delete语句

一般来说，事务是必须满足4个条件（ACID）： Atomicity（原子性）、Consistency（稳定性）、Isolation（隔离性）、Durability（可靠性）

    1、事务的原子性：一组事务，要么成功；要么撤回。
    2、稳定性 ： 有非法数据（外键约束之类），事务撤回。
    3、隔离性：事务独立运行。一个事务处理后的结果，影响了其他事务，那么其他事务会撤回。事务的100%隔离，需要牺牲速度。
    4、可靠性：软、硬件崩溃后，InnoDB数据表驱动会利用日志文件重构修改。可靠性和高速度不可兼得， innodb_flush_log_at_trx_commit选项 决定什么时候吧事务保存到日志里。

在Mysql控制台使用事务来操作

mysql> begin； ＃开始一个事务

mysql> insert into a (a) values(555);

mysql>rollback; 回滚 ， 这样数据是不会写入的

当然如果上面的数据没问题，就输入commit提交命令就行；


7.索引　　

MySQL索引的建立对于MySQL的高效运行是很重要的，索引可以大大提高MySQL的检索速度。

打个比方，如果合理的设计且使用索引的MySQL是一辆兰博基尼的话，那么没有设计和使用索引的MySQL就是一个人力三轮车。

索引分单列索引和组合索引。单列索引，即一个索引只包含单个列，一个表可以有多个单列索引，但这不是组合索引。组合索引，即一个索包含多个列。

创建索引时，你需要确保该索引是应用在 SQL 查询语句的条件(一般作为 WHERE 子句的条件)。

实际上，索引也是一张表，该表保存了主键与索引字段，并指向实体表的记录。

上面都在说使用索引的好处，但过多的使用索引将会造成滥用。因此索引也会有它的缺点：虽然索引大大提高了查询速度，同时却会降低更新表的速度，如对表进行INSERT、UPDATE和DELETE。因为更新表时，MySQL不仅要保存数据，还要保存一下索引文件。建立索引会占用磁盘空间的索引文件。
普通索引

创建索引

这是最基本的索引，它没有任何限制。它有以下几种创建方式：
1

CREATE INDEX indexName ON mytable(username(length));

如果是CHAR，VARCHAR类型，length可以小于字段实际长度；如果是BLOB和TEXT类型，必须指定 length。

 修改表结构
1

ALTER mytable ADD INDEX [indexName] ON (username(length))

创建表的时候直接指定

CREATE TABLE mytable(

ID INT NOT NULL,

username VARCHAR(16) NOT NULL,

INDEX [indexName] (username(length))

);



删除索引的语法
1

DROP INDEX [indexName] ON mytable;
唯一索引

它与前面的普通索引类似，不同的就是：索引列的值必须唯一，但允许有空值。如果是组合索引，则列值的组合必须唯一。它有以下几种创建方式：

创建索引
+ View Code
使用ALTER 命令添加和删除索引
+ View Code
使用 ALTER 命令添加和删除主键
+ View Code
显示索引信息
1

mysql> SHOW INDEX FROM table_name\G



mysql练习题 http://www.cnblogs.com/wupeiqi/articles/5729934.html 　　



更多mysql知识，请看http://www.cnblogs.com/wupeiqi/articles/5713323.html'''