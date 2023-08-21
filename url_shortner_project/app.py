from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)
app.config['BASE_URL']="https://jays_url_shortener.godaddysites.com/"  #Replace with your actual domain
app.config['URL_MAP']={}  # TO store url mapping

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = generate_short_url()
    app.config['URL_MAP'][short_url] = long_url
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = app.config['URL_MAP'].get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "Short URL not found", 404

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

if __name__ == '__main__':
    app.run(debug=True)