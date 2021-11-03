#転移学習を用いて芸能人の画像を学習し､パーソナルカラー診断をできるようにしました｡
##学習済みモデル：inception_v3を使用
##特徴量の抽出：dlibのランドマーク検出で顔だけを切り抜く

###主なモデル作成の手順
<li>自身のパーソナルカラーが判明している芸能人の画像を春､夏､秋､冬の各フォルダーに保存</li>
<li>dlibを使用して､パーソナルカラー診断として需要な顔だけを抽出する</li>
<li>抽出した画像を学習済みモデルincepton_v3を使用して転移学習を行う</li>
