#for flask
from __future__ import division
from __future__ import print_function
import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

#for model
import sys
import argparse
import cv2
import editdistance
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess
import predict


UPLOAD_FOLDER = '/home/shivam/SimpleHTR/data'
ALLOWED_EXTENSIONS = set([ 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/home', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('start.html')

@app.route('/uploads', methods =['GET', 'POST'])
def upload1_file():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template('first.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    predict.FilePaths.fnInfer = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    result = predict.main()
    return render_template('second.html',text = result['Recognized'],prob = result['Probability'] , accu = result['Accuracy'])


    #return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
   app.run(debug = True)
