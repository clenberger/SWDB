from flask import Flask, render_template, redirect, url_for

from pymongo import MongoClient

client = MongoClient()
db = client.StreetwearDB
clothing = db.clothing

app = Flask(__name__)

# clothing.insert_many([
#     {'name': 'Flowers T-Shirt', 'brand': 'Supreme'},
#     {'name': 'ASSC Logo Hoodie', 'brand': 'ASSC'},
#     {'name': 'BOGO Hoodie', 'brand': 'Supreme'}
# ])

@app.route('/')
def swdb_index():
    """Show clothing feed."""
    clothing_index = clothing.find()
    return render_template('clothing_index.html', clothing_index=clothing_index)

if __name__ == '__main__':
    app.run(debug=True)