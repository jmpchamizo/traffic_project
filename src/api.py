from flask import Flask, request, jsonify, flash, redirect, render_template
import detect_utils as du
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os, cv2
import numpy as np

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024




@app.route('/image/signs', methods=['POST'])
@cross_origin()
def get_signs_in_image():
    js = request.get_json()
    image = cv2.imread(f'{UPLOAD_FOLDER}/{js["filename"]}')
    if js['stop']:
        image = du.detect_sign(image)
    if js['circle']:
        image = du.detect_sign(image, "circular_cascade.xml", [1,2,3,4,5,6,8,9], (255,0,0), (255,0,0))
    if js['triangle']:
        image = du.detect_sign(image, "triangular_cascade.xml", [12,14,19,20,21,22,23,24,25,26,27,28,29,30,31,32], (0,255,0), (0,255,0))
    cv2.imwrite(f'./static/detect_{js["filename"]}',image)
    return f'../static/detect_{js["filename"]}'


@app.route('/video/signs', methods=['POST'])
@cross_origin()
def get_signs_in_video():
    js = request.get_json()
    return du.run_video_capture(stop=js['stop'], speed_limit=js['circle'], triangle_sign=js['triangle'])



def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_web():
	return render_template('index.html')


@app.route('/upload/image', methods=['POST'])
@cross_origin()
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('Files successfully uploaded')
		return render_template('detect_signs.html', value=filename)


app.run("0.0.0.0", 5000, debug=True)
#app.run("0.0.0.0", os.getenv("PORT"), debug=True)




