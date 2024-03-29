# coding = utf-8
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required,DataRequired
# from flask.ext.script import Manager

class NameForm(Form):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
# manager = Manager(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    # FlaskWTFDeprecationWarning: "flask_wtf.Form" has been \
    # renamed to "FlaskForm" and will be removed in 1.0.
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html',form=form,name=name)

@app.route('/user/<name>')
def user(name):
    render_template('user.html',name=name)
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__ == '__main__':
    app.run()
    # manager.run()