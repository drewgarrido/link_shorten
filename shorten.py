from flask import Flask, url_for, request, render_template
app = Flask(__name__)

dispatch = {'testing':"http://www.google.com"}
count = 1

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global count
    global dispatch
    if request.method == 'POST':
        shortened_url = str(count)
        count += 1

        dispatch[shortened_url] = request.form['url_text']
        return render_template('index.html',
                                shortened_url=shortened_url,
                                dest_url=dispatch[shortened_url])
    else:
        return render_template('index.html')

@app.route('/<shortened_url>')
def redirect(shortened_url):
    if (shortened_url in dispatch):
        return render_template('redirect.html', url_text=dispatch[shortened_url])
    else:
        return "Could not find " + shortened_url



if __name__ == '__main__':
    app.run()
    url_for('static', filename='style.css')
