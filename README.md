## 基于rho_attack的改良生日攻击

#### 小组成员

王彦森 201900150114

#### 代码概述

传统生日攻击的实现方式是每次计算一个哈希值，建立字典来比对每次计算的哈希值字典中是否已经有了。输出值长$l$比特的话就有$2^l$种可能性。因此为了实现这样的效果，需要花费较高的空间复杂度来维护一个字典。因此我尝试实现了一个改良版的生日攻击，将存储复杂度降低到了常数级别（只需要存一个对即可）。

#### 算法思路

我们可以确定一点：哈希值的计算一定满足下图的规律：

<img src="C:\Users\王彦森\AppData\Roaming\Typora\typora-user-images\image-20220730143957555.png" alt="image-20220730143957555" style="zoom:67%;" />

即不断进行哈希操作的话，一定可以找到一对碰撞，就如同上图中的$(H_4,H_{10})$就是一对满足要求的碰撞对。事实上，rho attack的碰撞攻击的方法就是如此。这种找碰撞对的方式比起传统生日攻击有两大优势：1.不同于生日攻击“大海捞针，rho算法目的性和方向性很强。2.生日攻击需要消耗很大的存储复杂度，但rho算法的空间复杂度降低到了常数级别。

算法分为两部分：第一部分类似于弗洛伊德判环法，通过两个哈希步数不同的变量判断环的大小。第二部分是再已经确定环的大小的情况下，寻找第一个不同的碰撞对。伪代码如下：

Input: A hash function $H:\{\overline{0}, 1\}^{*} \rightarrow\{\overline{0}, 1\}^{\varepsilon}$
Output: Distinct $x, x^{\prime}$ with $H(x)=H\left(x^{\prime}\right)$

$x_{0} \leftarrow\{0,1\}^{\ell+1}$
$x^{\prime}:=x:=x_{0}$
for $i=1,2, \ldots$ do:
$\quad x:=H(x)$
$\quad x^{\prime}:=H\left(H\left(x^{\prime}\right)\right)$
$\quad / /$ now $x=H^{(i)}\left(x_{0}\right)$ and $x^{\prime}=H^{(2 i)}\left(x_{0}\right)$
$\quad$ if $x=x^{\prime}$ break
$x^{\prime}:=x, x:=x_{0}$
for $j=1$ to $i:$
$\quad$ if $H(x)=H\left(x^{\prime}\right)$ return $x, x^{\prime}$ and halt
$\quad$ else $x:=H(x), x^{\prime}:=H\left(x^{\prime}\right)$
$\quad / /$ now $x=H^{(j)}\left(x_{0}\right)$ and $x^{\prime}=H^{(i+j)}\left(x_{0}\right)$

#### 代码实现

实现过程中主要面临以下问题：

python调用的gmssl库中sm3加密函数的操作对象是byte类型的数据，因此需要使用to_byte()函数将int类型的变量转成byte，以及使用bytes(str,encoding)函数将string类型的数据转成byte。这两个函数不能通用，所以缺一不可。

第一轮循环结束后赋值是有顺序的，不能赋反。

第一轮循环没有固定的停止时间，因此不能用for，得用while(1)循环等待。

python本身速度较慢，因此碰撞对的寻找需要较长时间，还需要一点运气。

代码使用jupyter notebook平台，完整代码如下：

![](C:\Users\王彦森\AppData\Roaming\Typora\typora-user-images\image-20220730152232004.png)

寻找过程如下：从运行结果来看很难找到

![image-20220730152317527](C:\Users\王彦森\AppData\Roaming\Typora\typora-user-images\image-20220730152317527.png)