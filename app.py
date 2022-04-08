from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_sender_gmail'
app.config['MAIL_PASSWORD'] = 'your_password_here'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']
        message = Message(subject, sender='your_sender_gmail',
                          recipients=['your_gmail_where_form_data_will_be_forwarded'])
        message.body = msg
        mail.send(message)
        success = "message sent"
        return render_template('AfterSend.html', success=success)

if __name__ == "__main__":
    app.run(debug=True)
