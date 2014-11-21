# Sample API Mashup

A sample mashup combining Twitter and Github user profiles.

## Running the Code

1. Initialize a virtualenv with the dependencies:

    virtualenv demo
    source demo/bin/activate
    pip install flask flask-restful requests

2. Start the server

    ipython server.py

3. Browse to [http://localhost:5000/mashup/<username>](http://localhost:5000/mashup/<username>). [Example](http://localhost:5000/mashup/emallson)