from flask import Flask, jsonify, request, make_response
import random

app = Flask(__name__)    
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def random_value():
    return str(random.randint(1, 1000))

@app.route('/no-store')
def no_store():
    response = make_response(jsonify({ 
        "startegy": "no-store",
        "resource": random_value()
    }))
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/no-cache')  
def no_cache():
    response = make_response(jsonify({ 
        "startegy": "no-cache",
        "resource": random_value()
    }))
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/public')
def public():     
    response = make_response(jsonify({ 
        "startegy": "public",
        "resource": random_value()
    }))
    response.headers['Cache-Control'] = 'public'
    return response

@app.route('/private')
def private():
    response = make_response(jsonify({
        "strategy": "private",
        "resource": random_value()
    }))
    response.headers['Cache-Control'] = 'private'     
    return response

@app.route('/max-age')
def max_age():
    response = make_response(jsonify({
        "strategy": "max-age=3600",
        "resource": random_value()
    }))
    response.headers['Cache-Control'] = 'max-age=3600'
    return response

if __name__ == '__main__':
    app.run(debug=True)