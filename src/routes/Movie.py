from flask import Blueprint, jsonify, request
import uuid 

# Entities
from models.entities.Movie import Movie

# Models
from models.MovieModel import MovideModel

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovideModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovideModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/add', methods=['POST'])
def add_movie():
    try:
        print(request.json)
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        id = str(uuid.uuid4())
        print (id)
        movie = Movie(id, title, duration, released)

        affected_rows = MovideModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on insert"}),500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        #print(request.json)
        #id = request.json['id']                
        movie = Movie(id)

        
        affected_rows = MovideModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on delete"}),500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        print(request.json)
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        
        print (id)
        movie = Movie(id, title, duration, released)

        affected_rows = MovideModel.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "Error on update"}),500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500