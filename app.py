from flask import Flask, render_template, redirect, url_for, request
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

client = MongoClient()
db = client.StreetwearDB
clothing = db.clothing

app = Flask(__name__)

# clothing.insert_many([
#     {'name': 'Flowers T-Shirt', 'brand': 'Supreme', 'image': './static/images/BoxLogo.png'},
#     {'name': 'ASSC Logo Hoodie', 'brand': 'ASSC', 'image': 'Levis.png'},
#     {'name': 'BOGO Hoodie', 'brand': 'Supreme', 'image': './static/images/BOGOhoodie.png'}
# ])

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

@app.route('/clothing/<item_id>/edit')
def item_edit(item_id):
    """Show the edit form for an item."""
    item = clothing.find_one({'_id': ObjectId(item_id)})
    return render_template('item_edit.html', item=item)

@app.route('/clothing/<item_id>', methods=['POST'])
def playlists_update(item_id):
    """Submit an edited item posting."""
    updated_item = {
        'name': request.form.get('name'),
        'brand': request.form.get('brand'),
    }
    clothing.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': updated_item})
    return redirect(url_for('item_show', item_id=item_id))

if __name__ == '__main__':
    app.run(debug=True)