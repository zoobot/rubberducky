# RubberDucky
## Email subscriber with Flask, HTML, and AJAX
*   This project was my first attempt at using Flask. I also goofed around with css animations.

* * *

### http://rubberducky.zoobot.ai:8000/index.html


### To start RubberDucky App
*   pip install flask gunicorn

* * *

### Without gunicorn
### Open terminal
### Enter this command:
*   FLASK_APP=server2.py flask run

* * *

### Open Browser
### Enter this url for serving via FLASK:
*   http://localhost:5000/index.html

* * *

### With gunicorn
*   rm -Rf __pycache__/
*   kill -HUP `cat server2.pid`
*   kill `cat server2.pid`
*   gunicorn server2:app -p server2.pid -b 0.0.0.0:8000 -D
*   gunicorn server2:app -p server2.pid -b localhost:8000 -D

* * *

### Open Browser
### Enter this url:
*   http://ip:5000/index.html