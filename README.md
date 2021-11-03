# Description
深層学習を用いて手軽にパーソナルカラー診断を行えることで今後の服選ぶや女性の方なら化粧品選びの参考になれば良いと思ったから作成に至った｡
 
# Features
パーソナルカラー診断を行いたい画像のパスを与えることで､その画像に対して春､夏､秋､冬の各タイプの可能性を提示する｡
また､最も近いタイプを表示する｡
 
# Requirement
 開発に使用したライブラリなど
 
* tensorflow 2.5.0
* opencv 4.5.2.52
* dlib 19.22.1
* imutils 0.5.4
 
# Installation
 
Requirementで列挙したライブラリなどのインストール方法
```bash
pip install tensorflow 
```
```bash
pip install opencv-python
```
```bash
brew install cmake
brew install boost-python
conda install -c menpo dlib=18.18
pip install dlib
```
```bash
pip install imutils
```
 
# Usage
 作成したモデルをHDF5で保存をしましたが､モデルの容量が大きすぎてgithub上に公開できないため､モデルの作成手順を記載しておきます｡
 
* 春､夏､秋､冬ごとにパーソナルカラーが判明している人の画像を保存を行う｡
* dlibのshape_predictor_68_face_landmarks.datを用いてその人物の顔もしくは特徴量となる目や口だけを保存する｡
* IncepitonV3を使用して転移学習を行い､モデルを作成する｡
 

 
# Author
* k.junya0727@gmail.com
* 具体的な詳細であったり､質問等ございましたらご気軽に連絡ください
