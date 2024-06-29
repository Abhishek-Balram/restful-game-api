from flask import Flask, request
from flask_restful import Api, Resource

application = Flask(__name__)
api = Api(application)

# In-memory storage (replace with database in production)
players = {}
scores = {}

class Player(Resource):
    def get(self, player_id):
        return {player_id: players.get(player_id, "Not found")}, 200 if player_id in players else 404

    def put(self, player_id):
        players[player_id] = request.form['data']
        return {player_id: players[player_id]}, 201

class PlayerList(Resource):
    def get(self):
        return players

    def post(self):
        # This line does the following:
        # 1. Combines the existing player IDs with '0' using the | operator
        # 2. Converts all IDs to integers
        # 3. Finds the maximum value and adds 1 to get the new player_id
        # 4. Converts the result back to a string
        player_id = str(max(map(int, players.keys() | {'0'})) + 1)
        
        players[player_id] = request.form['data']
        return {player_id: players[player_id]}, 201

class Score(Resource):
    def get(self, player_id):
        return {player_id: scores.get(player_id, "Not found")}, 200 if player_id in scores else 404

    def put(self, player_id):
        scores[player_id] = request.form['score']
        return {player_id: scores[player_id]}, 201

api.add_resource(PlayerList, '/players')
api.add_resource(Player, '/players/<player_id>')
api.add_resource(Score, '/scores/<player_id>')

if __name__ == '__main__':
    application.run(debug=True, port=5001)