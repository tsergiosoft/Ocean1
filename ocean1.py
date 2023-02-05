import datetime
import mycode
from flask import Flask, render_template, request, url_for, flash, redirect, Response

# ...

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]


@app.route('/')
@app.route('/index/')
def startpage():
    mycode.myvar = mycode.myvar + 1
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(), var1=mycode.myvar)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect('/index')
            #return redirect(url_for('startpage'))

    return render_template('create.html')

if __name__ == '__main__':
    app.run()
    app.debug = True