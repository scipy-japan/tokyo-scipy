**********************************
OpenOpt の線形計画で圧縮センシング
**********************************

担当： `神嶌 敏弘 <http://www.kamishima.net/>`_

最適化ライブラリ `OpenOpt <http://openopt.org/>`_ を使って，圧縮センシングを実装してみました．

実行方法
========

ちょこちょこっと ``openopt`` と ``FuncDesigner`` をインストール（もちろん numpy とかもね）してから::

  easy_install -U openopt
  easy_install -U FuncDesigner

* 直接線形計画を呼び出すバージョン： ``compressed_sensing.py``
* ``FuncDesigner`` を使って呼び出すバージョン： ``compressed_sensing2.py``

があるので，それぞれ実行してみてください．変換行列を乱数で作っているのでうまくデコードできるときも，そうでないときもあり，何回か実行すると元の入力の復元に失敗します．

メインルーチンの観測変数の数 ``n_outputs`` を 2〜5 の範囲で変えてみると，観測数が小さいほど失敗します．5 だともちろん線形方程式として解けるのでいつも正しいですが… (^_^)

``FuncDesigner`` を使うとときどき結果が ``NaN`` になるのは不思議ですね．

圧縮センシングの参考文献
========================

* `和田山 正“圧縮センシングの理論とその展開”第13回情報論的学習理論ワークショップ (2010) <http://ibisml.org/ibis2010/session/ibis2010wadayama.pdf>`_
* `田中 利幸“圧縮センシングの数理”IEICE Fundamentals Review, vol.4, no.1, pp.39-47 (2010) <http://www.ieice.org/ess/ESS/Fundam-Review.html>`_
