from flask import Flask,render_template,request
from flask_mail import Mail, Message
# import os        -> if you use os.environment.get('PASSWORD')

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ujjwalbhandari144@gmail.com'
# app.config['MAIL_PASSWORD'] = os.environment.get('PASSWORD') # because of being confidential
# or ⬇️
app.config['MAIL_PASSWORD'] = 'you_password_here'  #it's on backend. so, not to worry about writing your password here 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app) # mail libary initalized

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['GET','POST'])
def send_message():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        message = Message(subject, sender='ujjwalbhandari144@gmail.com', recipients=['ujjwalbhandari14@gmail.com'])
        message.body = msg
        mail.send(message)  
        success = "message sent"
        return render_template('AfterSend.html', success = success)

if __name__ == "__main__":
    app.run(debug=True)


