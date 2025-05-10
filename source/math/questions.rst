那些課本不會告訴你的事
=======================

----
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

fin.

.. note::
    他這16個分別是
    
    .. code-block:: text

        1 3 6 9 12 15
         2 4         16
        1.5 2.5 3.5 4.5 5.5 6.5 7.5
