''
'''
JavaScript是一门编程语言，浏览器内置了JavaScript语言的解释器，所以在浏览器上按照JavaScript语言的规则编写相应代码之，浏览器可以解释并做出相应的处理。
一、如何编写



1、JavaScript代码存在形式

<!-- 方式一 -->
<script type"text/javascript" src="JS文件"></script>

<!-- 方式二 -->
<script type"text/javascript">
    Js代码内容
</script>





2、JavaScript代码存放位置

    HTML的head中
    HTML的body代码块底部(推荐)

由于Html代码是从上到下执行，如果Head中的js代码耗时严重，就会导致用户长时间无法看到页面，
如果放置在body代码块底部，那么即使js代码耗时严重，也不会影响用户看到页面效果，只是js实现特效慢而已。

<script src="https://www.gstatic.com/og/_/js/k=og.og2.en_US.iF4jnkQuaf0.O/rt=j/t=zcms/m=def/exm=in,fot/d=1/ed=1/rs=AA2YrTv5-POC4Ks9GtGRdY2ywUWisqz7-Q"></script>
<script>
    alert('123');
</script>               '''




'''二、变量
JavaScript中变量的声明是一个非常容易出错的点，
局部变量必须一个 var 开头，
如果未使用var，则默认表示声明的是全局变量。

<script type="text/javascript">

    // 全局变量
    name = 'seven';

    function func(){
        // 局部变量
        var age = 18;

        // 全局变量
        gender = "男"
    }
</script>
JavaScript中代码注释：

    单行 //
    多行 /*  */

注意：此注释仅在Script块中生效。
三、数据类型

JavaScript 中的数据类型分为原始类型和对象类型：

    原始类型
        数字
        字符串
        布尔值
    对象类型
        数组
        “字典”
        ...

特别的，数字、布尔值、null、undefined、字符串是不可变。'''

'''

// null、undefined
null是JavaScript语言的关键字，它表示一个特殊值，常用来描述“空值”。
undefined是一个特殊值，表示变量未定义。'''

'''1、数字（Number）

JavaScript中不区分整数值和浮点数值，JavaScript中所有数字均用浮点数值表示。

转换：

    parseInt(..)    将某值转换成数字，不成功则NaN
    parseFloat(..) 将某值转换成浮点数，不成功则NaN

特殊值：

     NaN，非数字。可使用 isNaN(num) 来判断。
    Infinity，无穷大。可使用 isFinite(num) 来判断。
'''

'''常量

Math.E
常量e，自然对数的底数。

Math.LN10
10的自然对数。

Math.LN2
2的自然对数。

Math.LOG10E
以10为底的e的对数。

Math.LOG2E
以2为底的e的对数。

Math.PI
常量figs/U03C0.gif。

Math.SQRT1_2
2的平方根除以1。

Math.SQRT2
2的平方根。

静态函数

Math.abs( )
计算绝对值。

Math.acos( )
计算反余弦值。

Math.asin( )
计算反正弦值。

Math.atan( )
计算反正切值。

Math.atan2( )
计算从X轴到一个点的角度。

Math.ceil( )
对一个数上舍入。

Math.cos( )
计算余弦值。

Math.exp( )
计算e的指数。

Math.floor( )
对一个数下舍人。

Math.log( )
计算自然对数。

Math.max( )
返回两个数中较大的一个。

Math.min( )
返回两个数中较小的一个。

Math.pow( )
计算xy。

Math.random( )
计算一个随机数。

Math.round( )
舍入为最接近的整数。

Math.sin( )
计算正弦值。

Math.sqrt( )
计算平方根。

Math.tan( )
计算正切值。

Math'''


'''2、字符串（String）

字符串是由字符组成的数组，但在JavaScript中字符串是不可变的：可以访问字符串任意位置的文本，但是JavaScript并未提供修改已知字符串内容的方法。

常见功能：

obj.length                           长度

obj.trim()                           移除空白
obj.trimLeft()
obj.trimRight)
obj.charAt(n)                        返回字符串中的第n个字符
obj.concat(value, ...)               拼接
obj.indexOf(substring,start)         子序列位置
obj.lastIndexOf(substring,start)     子序列位置
obj.substring(from, to)              根据索引获取子序列
obj.slice(start, end)                切片
obj.toLowerCase()                    大写
obj.toUpperCase()                    小写
obj.split(delimiter, limit)          分割
obj.search(regexp)                   从头开始匹配，返回匹配成功的第一个位置(g无效)
obj.match(regexp)                    全局搜索，如果正则中有g表示找到全部，否则只找到第一个。
obj.replace(regexp, replacement)     替换，正则中有g则替换所有，否则只替换第一个匹配项，
                                     $数字：匹配的第n个组内容；
                                     $&：当前匹配的内容；
                                     $`：位于匹配子串左侧的文本；
                                     $'：位于匹配子串右侧的文本
                                     $$：直接量$符号
写。
3、布尔类型（Boolean）

布尔类型仅包含真假，与Python不同的是其首字母小写。

    ==      比较值相等
    !=       不等于
    ===   比较值和类型相等
    !===  不等于
    ||        或
    &&      且



4、数组

JavaScript中的数组类似于Python中的列表

常见功能：

obj.length          数组的大小

obj.push(ele)       尾部追加元素
obj.pop()           尾部获取一个元素
obj.unshift(ele)    头部插入元素
obj.shift()         头部移除元素
obj.splice(start, deleteCount, value, ...)  插入、删除或替换数组的元素
                    obj.splice(n,0,val) 指定位置插入元素
                    obj.splice(n,1,val) 指定位置替换元素
                    obj.splice(n,1)     指定位置删除元素
obj.slice( )        切片
obj.reverse( )      反转
obj.join(sep)       将数组元素连接起来以构建一个字符串
obj.concat(val,..)  连接数组
obj.sort( )         对数组元素进行排序
四、其他

1、序列化

    JSON.stringify(obj)   序列化
    JSON.parse(str)        反序列化

2、转义

    decodeURI( )                   URl中未转义的字符
    decodeURIComponent( )   URI组件中的未转义字符
    encodeURI( )                   URI中的转义字符
    encodeURIComponent( )   转义URI组件中的字符

    escape( )                         对字符串转义
    unescape( )                     给转义字符串解码
    URIError                         由URl的编码和解码方法抛出

3、eval

JavaScript中的eval是Python中eval和exec的合集，既可以编译代码也可以获取返回值。

    eval()
    EvalError   执行字符串中的JavaScript代码

4、正则表达式

1、定义正则表达式

    /.../  用于定义正则表达式
    /.../g 表示全局匹配
    /.../i 表示不区分大小写
    /.../m 表示多行匹配
    JS正则匹配时本身就是支持多行，此处多行匹配只是影响正则表达式^和$，m模式也会使用^$来匹配换行的内容)

     var pattern = /^Java\w*/gm;
    var text = "JavaScript is more fun than \nJavaEE or JavaBeans!";
    result = pattern.exec(text)
    result = pattern.exec(text)
    result = pattern.exec(text)

注：定义正则表达式也可以  reg= new RegExp()

2、匹配

JavaScript中支持正则表达式，其主要提供了两个功能：

    test(string)     检查字符串中是否和正则匹配


    n = 'uui99sdf'
    reg = /\d+/
    reg.test(n)  ---> true

    # 只要正则在字符串中存在就匹配，如果想要开头和结尾匹配的话，就需要在正则前后加 ^和$
    exec(string)    获取正则表达式匹配的内容，如果未匹配，值为null，否则，获取匹配成功的数组。


    获取正则表达式匹配的内容，如果未匹配，值为null，否则，获取匹配成功的数组。

    非全局模式
        获取匹配结果数组，注意：第一个元素是第一个匹配的结果，后面元素是正则子匹配（正则内容分组匹配）
        var pattern = /\bJava\w*\b/;
        var text = "JavaScript is more fun than Java or JavaBeans!";
        result = pattern.exec(text)

        var pattern = /\b(Java)\w*\b/;
        var text = "JavaScript is more fun than Java or JavaBeans!";
        result = pattern.exec(text)

    全局模式
        需要反复调用exec方法，来一个一个获取结果，直到匹配获取结果为null表示获取完毕
        var pattern = /\bJava\w*\b/g;
        var text = "JavaScript is more fun than Java or JavaBeans!";
        result = pattern.exec(text)

        var pattern = /\b(Java)\w*\b/g;
        var text = "JavaScript is more fun than Java or JavaBeans!";
        result = pattern.exec(text)

3、字符串中相关方法

obj.search(regexp)                   获取索引位置，搜索整个字符串，返回匹配成功的第一个位置(g模式无效)
obj.match(regexp)                    获取匹配内容，搜索整个字符串，获取找到第一个匹配内容，如果正则是g模式找到全部
obj.replace(regexp, replacement)     替换匹配替换，正则中有g则替换所有，否则只替换第一个匹配项，
                                        $数字：匹配的第n个组内容；
                                          $&：当前匹配的内容；
                                          $`：位于匹配子串左侧的文本；
                                          $'：位于匹配子串右侧的文本
                                          $$：直接量$符号

　　

5、时间处理

JavaScript中提供了时间相关的操作，时间操作中分为两种时间：

    时间统一时间
    本地时间（东8区）

'''

'''五、语句和异常

1、条件语句

JavaScript中支持两个中条件语句，分别是：if 和 switch
复制代码

    if(条件){

    }else if(条件){

    }else{

    }

复制代码
复制代码

    switch(name){
        case '1':
            age = 123;
            break;
        case '2':
            age = 456;
            break;
        default :
            age = 777;
    }'''

'''2、循环语句

JavaScript中支持三种循环语句，分别是：
复制代码

var names = ["alex", "tony", "rain"];

for(var i=0;i<names.length;i++){
    console.log(i);
    console.log(names[i]);
}


2:

var names = ["alex", "tony", "rain"];

变量names的索引;for循环
for(var index in names){
    console.log(index);
    console.log(names[index]);
}


3:
复制代码

while(条件){
    // break;
    // continue;
}



3、异常处理

try {
    //这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行
}
catch (e) {
    // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。
    //e是一个局部变量，用来指向Error对象或者其他抛出的对象
}
finally {
     //无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。
}

注：主动跑出异常 throw Error('xxxx')'''


'''六、函数

1、基本函数

JavaScript中函数基本上可以分为一下三类：

// 普通函数
    function func(arg){
        return true;
    }

// 匿名函数
    var func = function(arg){
        return "tony";
    }

// 自执行函数
    (function(arg){
        console.log(arg);
    })('123')

注意：对于JavaScript中函数参数，实际参数的个数可能小于形式参数的个数，函数内的特殊值arguments中封装了所有实际参数。

2、作用域

JavaScript中每个函数都有自己的作用域，当出现函数嵌套时，就出现了作用域链。当内层函数使用变量时，会根据作用域链从内到外一层层的循环，如果不存在，则异常。

切记：所有的作用域在创建函数且未执行时候就已经存在。

function f2(){
    var arg= 111;
    function f3(){
        console.log(arg);
    }

    return f3;
}

ret = f2();
ret();
复制代码

        function f2(){
            var arg= [11,22];
            function f3(){
                console.log(arg);
            }
            arg = [44,55];
            return f3;
        }

        ret = f2();
        ret();

复制代码

注：声明提前，在JavaScript引擎“预编译”时进行。'''


'''3、闭包

闭包是指可以包含自由（未绑定到特定对象）变量的代码块。

「闭包」，是指拥有多个变量和绑定了这些变量的环境的表达式（通常是一个函数），因而这些变量也是该表达式的一部分。

闭包是个函数，而它「记住了周围发生了什么」。表现为由「一个函数」体中定义了「另个函数」

由于作用域链只能从内向外找，默认外部无法获取函数内部变量。闭包，在外部获取函数内部的变量。


function f2(){
    var arg= [11,22];
    function f3(){
        return arg;
    }
    return f3;
}

ret = f2();
ret();

4、面向对象


function Foo (name,age) {
    this.Name = name;
    this.Age = age;
    this.Func = function(arg){
        return this.Name + arg;
    }
}

var obj = new Foo('alex', 18);
var ret = obj.Func("sb");
console.log(ret);

对于上述代码需要注意：

    Foo充当的构造函数
    this代指对象
    创建对象时需要使用 new

上述代码中每个对象中均保存了一个相同的Func函数，从而浪费内存。使用原型和可以解决该问题：


function Foo (name,age) {
    this.Name = name;
    this.Age = age;
}
Foo.prototype = {
    GetInfo: function(){
        return this.Name + this.Age
    },
    Func : function(arg){
        return this.Name + arg;
    }
}'''



'''JavaScript的作用域一直以来是前端开发中比较难以理解的知识点，对于JavaScript的作用域主要记住几句话，走遍天下都不怕...
一、“JavaScript中无块级作用域”

在Java或C#中存在块级作用域，即：大括号也是一个作用域。
复制代码

public static void main ()
{
    if(1==1){
        String name = "seven";
    }
    System.out.println(name);
}
// 报错

复制代码
C#

在JavaScript语言中无块级作用域
1
2
3
4
5
6
7

function Main(){
    if(1==1){
        var name = 'seven';
    }
    console.log(name);
}
// 输出： seven

补充：标题之所以添加双引号是因为JavaScript6中新引入了 let 关键字，用于指定变量属于块级作用域。
二、JavaScript采用函数作用域

在JavaScript中每个函数作为一个作用域，在外部无法访问内部作用域中的变量。
1
2
3
4
5
6
7
8
9

function Main(){
    var innerValue = 'seven';
}

Main();

console.log(innerValue);

// 报错：Uncaught ReferenceError: innerValue is not defined
三、JavaScript的作用域链

由于JavaScript中的每个函数作为一个作用域，如果出现函数嵌套函数，则就会出现作用域链。

xo = 'alex';

function Func(){
    var xo = "seven";
    function inner(){
        var xo = 'alvin';
        console.log(xo);
    }
    inner();
}
Func();

如上述代码则出现三个作用域组成的作用域链，如果出现作用域链后，那么寻找变量时候就会出现顺序，对于上述实例：

当执行console.log(xo)时，其寻找顺序为根据作用域链从内到外的优先级寻找，如果内层没有就逐步向上找，直到没找到抛出异常。

四、JavaScript的作用域链执行前已创建

JavaScript的作用域在被执行之前已经创建，日后再去执行时只需要按照作用域链去寻找即可。

示例一：

xo = 'alex';

function Func(){
    var xo = "seven";
    function inner(){

        console.log(xo);
    }
    return inner;
}

var ret = Func();
ret();
// 输出结果： seven

上述代码，在函数被调用之前作用域链已经存在：

    全局作用域 -> Func函数作用域 -> inner函数作用域

当执行【ret();】时，由于其代指的是inner函数，此函数的作用域链在执行之前已经被定义为：全局作用域 -> Func函数作用域 -> inner函数作用域，所以，在执行【ret();】时，会根据已经存在的作用域链去寻找变量。

示例二：

15

xo = 'alex';

function Func(){
    var xo = "eirc";
    function inner(){

        console.log(xo);
    }
    xo = 'seven';
    return inner;
}

var ret = Func();
ret();
// 输出结果： seven

上述代码和示例一的目的相同，也是强调在函数被调用之前作用域链已经存在：

    全局作用域 -> Func函数作用域 -> inner函数作用域

不同的时，在执行【var ret = Func();】时，Func作用域中的xo变量的值已经由 “eric” 被重置为 “seven”，所以之后再执行【ret();】时，就只能找到“seven”。

示例三：
用console.log代替alert和document.write，工作会变得轻松。
用console.log在控制台展开对象查看具体信息，可以直接看到对象信息，而不会显示[object Object]令我们一头雾水。

xo = 'alex';<br>
function Bar(){
    console.log(xo);
}

function Func(){
    var xo = "seven";

    return Bar;
}

var ret = Func();
ret();
// 输出结果： alex

上述代码，在函数被执行之前已经创建了两条作用域链：

    全局作用域 -> Bar函数作用域
    全局作用域 -> Func函数作用域

当执行【ret();】时，ret代指的Bar函数，而Bar函数的作用域链已经存在：全局作用域 -> Bar函数作用域，所以，执行时会根据已经存在的作用域链去寻找。
五、声明提前

在JavaScript中如果不创建变量，直接去使用，则报错：
1
2

console.log(xxoo);
// 报错：Uncaught ReferenceError: xxoo is not defined

JavaScript中如果创建值而不赋值，则该值为 undefined，如：

var xxoo;
console.log(xxoo);
// 输出：undefined

在函数内如果这么写：

function Foo(){
    console.log(xo);
    var xo = 'seven';
}

Foo();
// 输出：undefined

上述代码，不报错而是输出 undefined，
其原因是：JavaScript的函数在被执行之前，会将其中的变量全部声明，而不赋值。
所以，相当于上述实例中，函数在“预编译”时，已经执行了var xo；所以上述代码中输出的是undefined。'''
