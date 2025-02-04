from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

############################################################
# SETUP
############################################################

app = Flask(__name__)

# TODO Connect to MongoDB
MONGO_URI = ''
client = MongoClient(MONGO_URI, server_api=ServerApi('1'), tlsCAFule=ca)
app.config["Mongo_URI"] = MONGO_URI
mongo = PyMongo(app)
db = ''

# TODO Ensure You Succesfully Connected To MongoDB
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

############################################################
# ROUTES
############################################################
 
@app.route('/')
def index():
    # TODO Fetch all users from MongoDB

    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    # TODO Get The 'name' and 'email' From The Form Submission
    
    #TODO If Both 'name' and 'email' Are Provided, Insert Them Into The MongoDB Collectoin

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
