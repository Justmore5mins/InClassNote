三角函數
===========

角
-----

今天你看到一個角長這樣

.. image:: /_static/math/traingles/angles.png
    :width: 60%
    :align: center

一個角有兩個邊， ``始邊`` 與 ``終邊`` ，分別是一個角開始的邊與結束的邊

.. note::
    假設有兩個角他是同界角(共用始邊與終邊) :math:`\Longleftrightarrow \theta_1 - \theta_2 = 360^\circ k, k \in \mathbb{Z}`

.. tip::
    標準位置角：始邊是X軸正向，若終邊再第一象限 :math:`\rightarrow` 第一象限角, 第二象限 :math:`\rightarrow` 第二象限角 以此類推

.. image:: /_static/math/traingles/axis.png
    :width: 60%
    :align: center

那我們可以知道

.. math::
    \sin \theta = \frac{y}{r} (上下)
    \cos \theta = \frac{x}{r} (左右)
    \tan \theta = \frac{y}{x}

其中 :math:`\tan \theta = \frac{\sin\theta}{\cos\theta}`

如果背起來的話可以這樣記

.. image:: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNDHPL25vPAGPMGGx858oPlszdPPH6EwByMQ&s
    :width: 60%
    :align: center

.. note::
    我們也可以記成
        
    | 正弦 :math:`\sin \theta = \frac{對邊}{斜邊}`
    | 餘弦 :math:`\cos \theta = \frac{鄰邊}{對邊}`
    | 正切 :math:`\tan \theta = \frac{對邊}{鄰邊}` 

有趣的函數圖形
---------------

:math:`\sin \theta` 跟 :math:`\cos\theta` 的函數圖形長這樣

.. image:: /_static/math/traingles/functions.png
    :width: 60%
    :align: center

眼尖的你發現這個函數在每一個 :math:`2\pi` 會重複一次(這個牽涉到弧度的概念，可以簡單理解為 :math:`2\pi = 360^\circ` )

還有 :math:`\sin` 跟 :math:`\cos` 只有差 :math:`1.5\pi` (270度)


.. image:: /_static/math/traingles/tanx.png
    :width: 60%
    :align: center

這個是tan的函數圖形，可以看到他非常的抽象，就是在 :math:`90^\circ` 跟 :math:`270^\circ` 會發散掉

三角函數的範圍
+++++++++++++

.. image:: /_static/math/triangles/positive.png
    :width: 60%
    :align: center

.. attention:: 
    :math:`\tan 90^\circ` 跟 :math:`\tan 270^\circ` 未定義

----

假設今天a=5 b=12, c=13，那 :math:`\angle A` 的三角函數式多少

.. math::
    \sin A = \frac{5}{13}\\
    \cos A = \frac{12}{13}\\
    \tan A = \frac{5}{12}

然後聰明的你看了看發現 :math:`\angle B` 的三角函數會等於

.. math::
    \sin B = \cos A\\
    \cos B = \sin A\\

是不是非常神奇

.. image:: /_static/math/triangle.png
    :width: 60%
    :align: center

請問 :math:`\tan \theta = ?`

.. tip::
    下面兩條邊的比例(左比右)=上面兩條邊的比例(右比左)

那我們可以算出

.. math::
    \tan \theta = \frac{\frac{3}{2}}{3} = \frac{1}{2}

其中 :math:`\frac{3}{2} = 4\times \frac{3}{8}` ，4是下面那條邊的長度(3:4:5), :math:`\frac{3}{8}` 是裡面那個三角形佔的比例

小紀錄

.. image:: /_static/math/traingles/tricirc.png
    :width: 60%
    :align: center

.. note::
    公式們

    .. math::
        \tan\theta = \frac{\sin\theta}{\cos\theta} \\
        \sin^2 \theta+\cos^2\theta = 1 \\
        \sin \theta = \cos(90^\circ-\theta)\\
        \cos \theta = \sin(90^\circ-\theta)

.. todo:: Add the 30^\circ and 60^\circ table of sin cos and tan


當立方和公式遇到三角函數
-------------------------

小時候，我們學到

.. math::
    a^3+b^3 = (a+b)(a^3-ab+b^3) = (a+b)^3 - 3ab(a+b)\\
    a^3-b^3 = (a-b)(a^3+ab+b^3) = (a-b)^3 + 3ab(a-b)

讓我們來看看有哪些題目可以使用到這些公式

.. math::
    known \sin \theta - \cos\theta = \frac{1}{2}\\
    1. \sin\theta\cos\theta\\
    2. \sin\theta+\cos\theta\\
    3. \sin^3 \theta - \cos^3 \theta\\
   
1. 先一波計算
   
   :math:`(\sin \theta - \cos \theta)^2 = \sin^2 \theta + 2\sin\theta\cos\theta + \cos^2 \theta = \frac{1}{4}`
   
   再因為 :math:`\sin^2 \theta + \cos^2 \theta = 1` ,所以 :math:`\sin\theta\cos\theta=\frac{1}{4}\times\frac{1}{2} = \frac{1}{8}`

2. :math:`(\sin\theta+\cos\theta)^2 = ... = 1+2\times \frac{3}{8}, 所以 \sin\theta+\cos\theta = \frac{\sqrt{7}}{8}`

3. :math:`\sin^3 \theta - \cos^3 \theta = ... = \frac{1}{2} \times (1+\frac{3}{8}) = \frac{11}{16}`

.. tip::
    仰角上看俯角往下看



小練習
---------

試求下面圖剩餘線段的長度
++++++++++++++++++++++++++++

.. image:: /_static/math/traingles/q1.png
    :width: 60%
    :align: center

    

其中 :math:`\sin \theta = \frac{15}{17}, \cos \phi = \frac{3}{5}`

根據上面的條件，我們可以知道 :math:`\overline{BD} = 15, \overline{BC} = 15\times\frac{3}{5}=9` ，再推斷出 :math:`\overline{DC} = 4\times3=12`

非常的完美


公式換換樂
+++++++++++++++

.. math::
    1. \cos^2 34^\circ + \cos^2 56^\circ \\
    2. \tan^2 65^\circ-\frac{1}{\cos^2 65ª}

.. math::
    1. =\sin^2 56^\circ + \cos^2 56^\circ = 1 \\
    2. =\frac{\sin^2 65^\circ}{\cos^2 65^\circ} - \frac{1}{\cos^2 65^\circ} = \frac{\sin^2 65^\circ - (\cos^2 65^\circ+\sin^2 65^\circ)}{\cos^2 65^\circ} = -1
   