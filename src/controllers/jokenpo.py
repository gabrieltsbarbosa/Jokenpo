from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server
from src.repositories.jokenpoRepository import Repo

application, api = server.application, server.api


@api.route('/jokenpo')
class Jokenpo(Resource):
    @application.route('/health', methods=['GET'])
    def healthCheck():
        return 'healthCheck', 200

    @application.route('/jokenpo', methods=['GET'])
    def get():
        return Repo.get_result()

    @application.route('/jokenpo/player/<int:id>', methods=['GET'])
    def get_player(id):
        return Repo.get_player(id)
    
    @application.route('/jokenpo/player', methods=['POST'])
    def post():
        return Repo.insert_player(api.payload)

    @application.route('/jokenpo/player/<int:id>', methods=['PUT'])
    def put(id):
        return Repo.update_move(id, api.payload)
    
    @application.route('/jokenpo/player/<int:id>', methods=['DELETE'])
    def delete(id):
        return Repo.deletePlayer(id)

    
    @application.route('/jokenpo/player/all', methods=['DELETE'])
    def delete_all():
        return Repo.delete_all_players()