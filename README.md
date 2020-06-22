# :leaves: Final-Project-DPS5-A
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/chilaact/Final-Project-DPS5-A/blob/master/LICENSE)
[![](https://img.shields.io/badge/python-3.8%2B-green.svg)](https://github.com/chilaact/Final-Project-DPS5-A)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)

<p align=center>
<img src="https://i.ibb.co/k0b0RWJ/ML-fore-2x.png" width=30% height=30%>
</p>

<p align=justify>&emsp;This repository contains a Plant Disease Classification application with a Neural Network Convolutional Using TensorFlow 2 which is intended to complete the Final Project Bangkit Academy 2020. We use CNN with Pre-trained MobileNetV2 who have previously been trained in building models, then we spread it through Herokuapp using a flask.</p>

## :computer: Usage
1. Pull this repository<br>
2. Enter this command<br>
```
pip install -r requirements.txt
```
3. Run on development server
```
python main.py
```
4. Open up <b>localhost:5000/</b> on your browser<br>

## :black_square_button: App Screenshot
<p align=center>
<img src="https://i.ibb.co/bXhBCyp/Screenshot-from-2020-06-20-08-10-14.png" width=80% height=80%><br>Image 1<br><br>
<img src="https://i.ibb.co/mBfdYx5/Screenshot-from-2020-06-22-12-27-19.png" width=80% height=80%><br>Image 2<br><br>
<img src="https://i.ibb.co/BKhY0rg/Screenshot-from-2020-06-22-12-28-28.png" width=80% height=80%><br>Image 3<br><br>
<img src="https://i.ibb.co/Prc3F5N/Screenshot-from-2020-06-22-12-28-45.png" width=80% height=80%><br>Image 4</p>
  
## :paperclip: Features
1. Can diagnose the disease of plant by giving the image of it's leaf
2. Free for everyone
3. Model can easily adjusted for main purpose (model on static/mobilenetv2.h5)

## :exclamation: Limitations
1. Can only classifying image which have 256x256 resolution (or the app will redirect you on warning page)
2. The best look of user interface our app is for laptop/computer not mobile 

## :pushpin: Live demo
<a href="https://plant-dps5a.herokuapp.com/">CLICK!</a><br>
Try using the dataset from https://www.kaggle.com/vipoooool/new-plant-diseases-dataset/
