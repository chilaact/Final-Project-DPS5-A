# libraries
from numpy import array, argmax
from skimage import io, transform
from pyrebase import initialize_app

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, render_template, request, redirect, url_for

# flask routing
app = Flask(__name__)

# load the model
model = load_model('static/mobilenetv2.h5')

# firebase configuration
config = {"apiKey": "secret",
          "authDomain": "secret",
          "databaseURL": "secret",
          "projectId": "secret",
          "storageBucket": "secret",
          "messagingSenderId": "secret",
          "appId": "secret"}

# helper variable
spesies = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
           'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
           'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)',
           'Peach___Bacterial_spot', 'Peach___healthy','Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
           'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight',
           'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
           'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

# to help access the firebase storage
storage = initialize_app(config).storage()

# main page
@app.route('/')
def index():
  return render_template('index.html')

# base model .ipynb
@app.route('/base-model')
def base():
  return render_template('Model_base.html')

# improved model .ipynb
@app.route('/improved-model')
def improved():
  return render_template('Model_improved.html')

# main process
@app.route('/diagnose/<plant>', methods=['POST', 'GET'])
def diagnose(plant):
  global spesies # to access species variable because it is global variable
  
  # to determine the type of leaves
  if plant == 'others':
    species = ['Blueberry___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew']
  else:
    species = [sp for sp in spesies if plant.capitalize() in sp]

  # begin to classify
  if request.method == "POST":
    # normal scenario, if the resolution image given by user is 256x256
    try:
      # send it to firebase storage first and then do the classification
      storage.child('bangkit/temp.jpg').put(request.files['gambar'])
      url_img = storage.child('bangkit/temp.jpg').get_url(None)

      img = io.imread(url_img)
      img = array([transform.resize(img, (256, 256))])

      # get prediction results
      pred = model.predict(img)

      # to get indexes of each elements for spesies variable
      if plant == 'others':
        indeks = [4, 15, 23, 24, 25]
      else:
        indeks = [i for i, e in enumerate(spesies) if plant.capitalize() in e]

      # get final results
      hasil = [pred[0][i] for i in indeks]
      hasil = list(map(abs, hasil))
      hasil_akhir = [i/sum(hasil)*100 for i in hasil]
      
      # convert it into dictionaries
      result = dict(zip(species, hasil_akhir))

      return render_template('hasil.html', plant = plant, result = result, img = url_img)
    except:
      # error scenario, if the resolution image given by user isn't 256x256 
      return render_template('500.html', plant = plant, img = storage.child('bangkit/temp.jpg').get_url(None))

  # rendered if user didn't do the classification
  return render_template('diagnose.html', plant = plant, species = species)

# for unlisted route/url
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404