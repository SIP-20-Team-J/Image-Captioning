from flask import Flask, render_template, url_for, request, redirect
from caption_this import caption_image
import warnings 
import tensorflow as tf
from text_to_speech import sound_function
from hashtags import hashtag_generator
warnings.filterwarnings("ignore")



app = Flask(__name__)



@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		img = request.files['image']

		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)


		caption = caption_image("static/"+img.filename)

		hashtag1= hashtag_generator(caption)		
		sound_output= sound_function(caption)
        
		result_dic = {
			'image' : "static/" + img.filename,
			'description' : caption,
			'sound' : sound_output,
            'length' : len(hashtag1)
            
           
			
		}
	return render_template('index.html', results = result_dic, Hashtag = hashtag1)


    
       


@app.route('/music/<path:filename>')
def download_file(filename):
        return send_file('/home/name/Music/', filename)       

if __name__ == '__main__':
	app.run(debug = True,threaded=False,use_reloader=False)