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
        return Repo.getResult()

    @application.route('/jokenpo/player/<int:id>', methods=['GET'])
    def getPlayer(id):
        return Repo.getPlayer(id)
    
    @application.route('/jokenpo/player', methods=['POST'])
    def post():
        return Repo.insertPlayer(api.payload)

    @application.route('/jokenpo/player/<int:id>', methods=['PUT'])
    def put(id):
        return Repo.updateMove(id, api.payload)
    
    @application.route('/jokenpo/player/<int:id>', methods=['DELETE'])
    def delete(id):
        return Repo.deletePlayer(id)

    
    @application.route('/jokenpo/player/all', methods=['DELETE'])
    def delete_all():
        return Repo.delete_allPlayers()