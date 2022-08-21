# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, Response, jsonify, request
  
# creating a Flask app
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "I am running"
        return jsonify({'message': data})
  
  
# function to handle /webhook 
# methods GET & POST
@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
    if(request.method == 'GET'):
        mode =  request.args.get('hub.mode')
        challenge =  request.args.get('hub.challenge')
        verify_token =  request.args.get('hub.verify_token')
        if mode == 'subscribe' and verify_token == 'ramkumar':
            return Response(challenge, status=200)
        else:
            return Response(status=403)
    elif (request.method == 'POST'):
        print(request.json)
        return Response(status=200)
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = False)