from dotenv import load_dotenv
from flask import Flask, request
from flask_restful import Api, Resource
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

load_dotenv()

application = Flask(__name__)
api = Api(application)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
player_table = dynamodb.Table('Players')
score_table = dynamodb.Table('Scores')

class Player(Resource):
    def get(self, player_id):
        try:
            response = player_table.get_item(Key={'player_id': player_id})
        except ClientError as e:
            return {'error': str(e)}, 500
        
        item = response.get('Item')
        if item:
            return {player_id: item['data']}, 200
        return {player_id: "Not found"}, 404

    def put(self, player_id):
        data = request.form['data']
        try:
            player_table.put_item(Item={'player_id': player_id, 'data': data})
        except ClientError as e:
            return {'error': str(e)}, 500
        return {player_id: data}, 201

class PlayerList(Resource):
    def get(self):
        try:
            response = player_table.scan()
        except ClientError as e:
            return {'error': str(e)}, 500
        
        return {item['player_id']: item['data'] for item in response['Items']}

    def post(self):
        data = request.form['data']
        try:
            response = player_table.scan(Select='COUNT')
            player_count = response['Count']
            new_player_id = str(player_count + 1)
            player_table.put_item(Item={'player_id': new_player_id, 'data': data})
        except ClientError as e:
            return {'error': str(e)}, 500
        return {new_player_id: data}, 201

class Score(Resource):
    def get(self, player_id):
        try:
            response = score_table.get_item(Key={'player_id': player_id})
        except ClientError as e:
            return {'error': str(e)}, 500
        
        item = response.get('Item')
        if item:
            return {player_id: item['score']}, 200
        return {player_id: "Not found"}, 404

    def put(self, player_id):
        score = request.form['score']
        try:
            score_table.put_item(Item={'player_id': player_id, 'score': score})
        except ClientError as e:
            return {'error': str(e)}, 500
        return {player_id: score}, 201

api.add_resource(PlayerList, '/players')
api.add_resource(Player, '/players/<player_id>')
api.add_resource(Score, '/scores/<player_id>')

if __name__ == '__main__':
    application.run(debug=True, port=5001)