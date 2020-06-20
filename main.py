from numpy import array, argmax
from skimage import io, transform

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
model = load_model('notebooks/mobilenetv2.h5')

# ntar awakmu atur sendiri lah ini enak'e piye
spesies = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
           'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
           'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)',
           'Peach___Bacterial_spot', 'Peach___healthy','Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight',
           'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
           'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
           'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/modeling')
def modeling():
  return render_template('Modeling.html')

@app.route('/diagnose/<plant>')
def diagnose(plant):
  global spesies
  
  if plant == 'others':
    species = ['Blueberry___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew']
  else:
    species = [sp for sp in spesies if plant.capitalize() in sp]

  return render_template('diagnose.html', plant = plant, species = species)

@app.route('/prediksi/<plant>', methods=['POST'])
def prediksi(plant):
  if request.method == "POST":
    img = io.imread(request.files['gambar'])
    img = array([transform.resize(img, (224, 224))])
     
    pred = model.predict(img)
    
    if plant == 'others':
      species = ['Blueberry___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew']
      indeks = [4, 15, 23, 24, 25]
    else:
      species = [sp for sp in spesies if plant.capitalize() in sp]
      indeks = [i for i, e in enumerate(spesies) if plant.capitalize() in e]
    
    hasil = [pred[0][i] for i in indeks]
    hasil = list(map(abs, hasil))
    hasil_akhir = [i/sum(hasil)*100 for i in hasil]
   
    result = dict(zip(species, hasil_akhir))

    return jsonify(result = result)
  pass

app.run(debug=True)