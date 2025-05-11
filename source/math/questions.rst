那些課本不會告訴你的事
=======================

:nosearch:

交集問題
-----------

.. math::
    A = \{\frac{t}{2}\mid t \in \mathbb{N},1 \leq t \leq 50\}\\
    B = \{\frac{k}{3} \mid k \in \mathbb{N}, 1 \leq k \leq 50\}

試問 :math:`n(A \cup B) =\ ?`

首先我們先來找 :math:`n(A \cap B)` 是多少

他可以寫成像是這樣

.. math::
    A \cap B = \{ x \in \mathbb{Q} \mid x = \frac{a}{2} = \frac{b}{3}, a,b \in \mathbb{N}, 1 \leq a,b \leq 50 \}

:math:`\frac{a}{2}` 的最大範圍是 :math:`\frac{50}{2} = 25` ， 而 :math:`\frac{50}{3} = 16.\overline{6}`

也就是說，:math:`A \cap B` 的最大範圍就是16

所以 :math:`n(A \cap B) = 16` ， 在套用公式進行精密的計算過後

.. math::
    n(A \cup B) = n(A) + n(B) - n(A \cap B) = 50+50-16 = 84

.. note::
    他這16個分別是
    
    .. code-block:: text

        1 3 6 9 12 15
         2 4         16
        1.5 2.5 3.5 4.5 5.5 6.5 7.5

fin.

:math:`C^8_4` 之謎
------------------

請問下列哪些敘述的方法數與 :math:`C^8_4不同` ?

A. :math:`(x+1)^7` 展開後, :math:`x^3` 跟 :math:`x^4` 的係數和
B. 每個人單手只能出正面或反面，8個人恰好4正4反的方法數
C. 8人分兩組的方法數
D. 「歐拉歐拉歐拉歐拉」排成一列的方法數
E. 從11個大小相同的位置取4個恰不相鄰的位置的方法數

----

A. :math:`x^3` 係數為 :math:`C^7_3` :math:`x^4` 係數為 :math:`C^7_4` 而這兩個相加 :math:`C^7_3 + C^7_4 = C^8_4`
B. 就是將8個人分成兩種人，正面的人跟反面的人，每種人個站4個，也就是 :math:`\frac{8!}{4!4!}` ，這剛好也是 :math:`C^8_4` 的定義
C. 這個是用人選組(不是組選人，因為如果兩組選到同一個人的話是要把它對切嗎)，也就是 :math:`2^8` 種
D. 我不知道
E. 這個東東最少需要8個位置：前一(或後一)+中三+原本四個位置，然後我們要在這8個位置找4個不相鄰的空位督，也就是 :math:`C^8_4`

到底成績是多少
---------------

有一班有35個人，一次大考時，國文有及格25個，英文17個，數學14個，請問下列條件的人數

| 只有數學及格的
| 只有國文跟英文及格的
| 三個科目都及格的
| 都不及格的

----

定義

.. code-block:: text

    國文及格為A集合
    英文為B
    數學為C

所以可以描述成

.. math::
    n(A \cup B \cup C) = 25+17+14 - [n(A \cap B) + n(B \cap C) + n(A \cap C)] + n(A\cap B\cap C)

假設沒有人都不及格 :math:`\Rightarrow n(A \cup B \cup C) = 35`

(將 :math:`n(A \cap B) + n(B \cap C) + n(A \cap C)` 簡化為 x, :math:`n(A\cap B\cap C)` 簡化為y)

.. math::
    25+17+14-x+y = 35 \Rightarrow 56-x+y=35

.. math::
    x-y = 21