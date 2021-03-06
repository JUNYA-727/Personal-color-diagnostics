# Description
深層学習を用いて手軽にパーソナルカラー診断を行えることで今後の服選ぶや女性の方なら化粧品選びの参考になれば良いと思ったから作成に至った｡
 
 
# Requirement
 開発に使用したライブラリなど
 
* tensorflow 2.5.0
* opencv 4.5.2.52
* dlib 19.22.1
* imutils 0.5.4

# Features
パーソナルカラー診断を行いたい画像のパスを与えることで､その画像に対して春､夏､秋､冬の各タイプの可能性を提示する｡
また､最も近いタイプを表示する｡

# Model Creation Procedure

* 春､夏､秋､冬ごとにパーソナルカラーが判明している人の画像を保存を行う｡
* dlibのshape_predictor_68_face_landmarks.datを用いて人物のランドマークを検出する｡
![face](https://user-images.githubusercontent.com/61785070/140064480-fac8e45b-5c3d-426b-a949-8ef1a59ef5e6.png)

* ランドマーク検出後に顔や目､口といった特徴量だけを保存する｡
* IncepitonV3を使用して転移学習を行い､モデルを作成する｡
<img width="705" alt="スクリーンショット 2021-11-04 19 11 49" src="https://user-images.githubusercontent.com/61785070/140297273-0f468541-9791-454c-a526-e96f74fa84aa.png">
* 作成したモデルをdetect.pyのモデルの読み込みにパスを記載して実行する
<img width="714" alt="スクリーンショット 2021-11-03 22 08 05" src="https://user-images.githubusercontent.com/61785070/140065688-318aa913-0ddc-445c-a37f-3821b7df30ff.png">

# How to use
detect.pyを使用する際には､学習済みの以下のモデルのダウンロードしてから使用してください｡
https://drive.google.com/file/d/1ESLm0Ri3QNrz5isLr1jwXVvSvYaBpNmi/view?usp=sharing

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
 
# Author
* k.junya0727@gmail.com
* 具体的な詳細であったり､質問等ございましたらご気軽に連絡ください
