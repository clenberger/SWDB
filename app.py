from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient()
db = client.StreetwearDB
clothing = db.clothing

app = Flask(__name__)

clothing.insert_many([
    {'name': 'Flowers T-Shirt', 'brand': 'Supreme'},
    {'name': 'ASSC Logo Hoodie', 'brand': 'ASSC'},
    {'name': 'BOGO Hoodie', 'brand': 'Supreme'}
])

@app.route('/')
def clothing_index():
    """Show clothing feed."""
    clothing_db = clothing.find()
    return render_template('clothing_index.html', clothing_db=clothing_db)

@app.route('/clothing/new')
def clothing_new():
    """Create a new clothing item"""
    return render_template('clothing_new.html')

@app.route('/clothing', methods=['POST'])
def clothing_submit():
    """Submit a new clothing piece."""
    item = {
        'name': request.form.get('name'),
        'brand': request.form.get('brand')
    }
    item_id = clothing.insert_one(item).inserted_id
    return redirect(url_for('item_show', item_id=item_id))

@app.route('/clothing/<item_id>')
def item_show(item_id):
    """Show a single piece of clothing."""
    item = clothing.find_one({'_id': ObjectId(item_id)})
    return render_template('item_show.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)