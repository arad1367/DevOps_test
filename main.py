from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('welcome'))
    return render_template('home.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        name = request.form.get('name')
        color = request.form['color']
        return render_template('welcome.html', name=name, color=color, form_send=True)
    return  render_template('welcome.html', form_send=False)

if __name__ == '__main__':
    app.run(debug=True)