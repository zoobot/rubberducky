from flask import Flask, request, send_from_directory
import smtplib

# I tried to make a Flask server because I have not used Flask before
# name the app 'app'
app = Flask(__name__)

# resolve to whatever route is in your url path
@app.route('/<path:path>', methods=['POST', 'GET'])
def serve_page(path):
  email_subscriber =  request.form.get('email')
  if request.method == 'POST':
    # who's going to get these subscribers of the ducky
    email_to = 'rommims@gmail.com'
    # send from email and password here
    email_from = 'rose@zoobot.ai'
    email_pwd = 'c0mpound!ng'
    email_subject = 'You have a new RubberDucky subscriber: ' + email_subscriber
    # smtp server and port # here
    smtpserver = smtplib.SMTP("mail.zoobot.ai",25)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    # login here to willing smtp server, gmail sent a crabby blocking email
    smtpserver.login(email_from, email_pwd)
    email_header = 'To:' + email_to + '\n' + 'From: ' + email_from + '\n' + 'Subject:' + email_subject + '\n'
    email_msg = email_header + email_subject
    smtpserver.sendmail(email_from, email_to, email_msg)

    smtpserver.close()
    user_agent = request.headers.get('User-Agent')
    # to check for Bug in this version Safari with jquery show hide
    if (user_agent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7'):
      return send_from_directory('static', path)
    else:
     # return subscribe success for the rest of the nice browsers
     return '{"hello": "' + email_subscriber + '"}'
  # return index for get
  return send_from_directory('static', path)

if __name__ == '__main__':
 app.run(debug=True)