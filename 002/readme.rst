****************
Tokyo.Scipy #002
****************

第2回 Tokyo.Scipy で議論された code snippet などです．
サンプルコードは，オリジナルのものをコピーしただけなので，-inf に対応していなかったり，行列の大きさの変更に対応していなかったり，クラスの値の範囲が 1 からか 0 からかまちまちだったりするため，気がついたら書き直して下さい．

- Partake: http://partake.in/events/ef1d15c9-a9ba-46e4-b94e-e91e6fbd0aa3
- Announce: http://groups.google.com/group/tokyo_scipy/browse_frm/thread/3a9baba571c9d0bc

Program
=======

- NumPy/SciPy体験セクション続編 杜世橋さん （FreeBit、@lucidfrontier45） http://j.mp/ra3Esg
- 数式を numpy に落としこむコツ 〜機械学習を題材に〜 @shuyoさん http://d.hatena.ne.jp/n_shuyo/20111016/numpy
- 最適なコーディングディスカッション 全員 http://www.slideshare.net/shoheihido/111015-tokyo-scipy2
- Callable Array @tyatsutaさん http://www.slideshare.net/yatsuta/tokyo-scipy2

CODE 03
=======

``NaN`` や ``Inf`` を含む値の列 ``x = numpy.array([[1,0,nan,1,Inf,1,....]])`` が与えられたとき、 ``NaN`` や ``Inf`` 以外のxの要素の合計を計算する方法が直ぐに思い浮かびますか？

Check for discussion at scikits.learn https://github.com/scikit-learn/scikit-learn/issues/252

CODE 04
=======

``NaN`` を含む 4×2行列 ``m = numpy.array([[1,nan,-1,0],[0,0,nan,1]])`` が与えられたとき、 ``NaN`` を含む行を削除して 2×2行列にする方法が直ぐに思い浮かびますか？

CODE 05
=======

``numpy.array([[1,3,2]])`` を、1-of-K 表記法変換して ``numpy.array([[1,0,0],[0,0,1],[0,1,0]])`` にする処理方法が直ぐに思い浮かびますか？
