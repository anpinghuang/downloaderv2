from flask import Flask, render_template, request, redirect, send_file, jsonify,url_for, abort
import streamlink

app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    return render_template('index.html', error_or_not="visible"), 500

@app.route('/',  methods=["POST", "GET"])
def home():
  if request.method=="POST":
    url = request.form["url"]
    format = request.form.get('opt')
    print("the format is: "+str(format))
    print("Someone just tried to download", url)
    streams = streamlink.streams(url)

    try:
      stream = streams[format]
      download_url = stream.url
      return redirect(download_url)
    except streamlink.exceptions.PluginError:
      abort(500)
    
  else:
    return render_template('index.html', error_or_not="hidden")


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/terms')
def terms():
    return render_template('terms-and-conditions.html')
    


if __name__ == '__main__':
  app.run(debug=False)
