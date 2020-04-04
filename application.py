from flask import Flask, Markup, request, render_template
app = Flask(__name__)

@app.route('/')
def precalc():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def aftercalc():
    a = request.form['username']
    b = request.form['password']
    if a=="admin":
        if b=="S)e<7zwK9Sxz]44F":
            return render_template('success.html')
        else:
            return render_template('error.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.debug = True
    app.run()