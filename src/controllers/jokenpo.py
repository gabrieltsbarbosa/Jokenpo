from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server
from src.repositories.jokenpoRepository import Repo

application, api = server.application, server.api


@api.route('/jokenpo')
class Jokenpo(Resource):
    @application.route('/health', methods=['GET'])
    def healthCheck() -> str:
        """
        Use to check application health
        """
        return 'healthCheck', 200

    @application.route('/jokenpo', methods=['GET'])
    def get() -> dict:
        """
        call this to get game result
        """
        return Repo.get_result()

    @application.route('/jokenpo/player/<int:id>', methods=['GET'])
    def get_player(id: int) -> dict:
        """
        Use to get player name and move
        """
        return Repo.get_player(id)
    
    @application.route('/jokenpo/player', methods=['POST'])
    def post() -> dict:
        """
        Use to insert a player into db
        """
        return Repo.insert_player(api.payload)

    @application.route('/jokenpo/player/<int:id>', methods=['PUT'])
    def put(id) -> str:
        """
        Use to change player move
        """
        return Repo.update_move(id, api.payload)
    
    @application.route('/jokenpo/player/<int:id>', methods=['DELETE'])
    def delete(id: int) -> str:
        """
        Use to delete a player
        """
        return Repo.deletePlayer(id)

    
    @application.route('/jokenpo/player/all', methods=['DELETE'])
    def delete_all() -> str:
        """
        Use to clear all players
        """
        return Repo.delete_all_players()