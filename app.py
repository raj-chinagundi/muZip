from flask import Flask, render_template, request, send_file
import youtube_zip
from youtube_zip import searchtube
import os
app = Flask(__name__)


@app.route('/')
@app.route("/index/")
def index():
    return render_template('index.html', success=False, error=False)


@app.route('/download')
# def download_file():
#     return send_file('audios.zip')


@app.route("/send_audio/", methods=['POST'])
def send_audio():
        if request.method == 'POST':
            artist = request.form['artist'] + ' official m/v'
            songNumber = int(request.form['songNumber'])
        if artist == '' or songNumber == '':
            return render_template('index.html', message='Please enter required fields')
        searchtube(artist, songNumber)
        return send_file('audios.zip')
    
    
    

if __name__ == "__main__":
   
    app.run(debug=True)
