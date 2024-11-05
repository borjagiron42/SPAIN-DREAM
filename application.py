from flask import Flask, render_template
application = Flask(__name__)

@application.route('/')
@application.route('/home')
def home():
  return render_template('home.html')

@application.route('/business')
def business():
  return render_template('business.html', title='business')

@application.route('/light_talk_app')
def light_talk_app():
    return render_template('light_talk_app.html', title='light_talk_app')

if __name__=='__main__':
  application.run(debug=True)  
