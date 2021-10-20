from flask import Flask, request
from flask_restx import Api, Resource

from src.server.instance import server
from src.repositories.jokenpoRepository import JokenpoRepository

application, api = server.application, server.api


@api.route('/jokenpo')
class Jokenpo(Resource):
    @application.route('/health', methods=['GET'])
    def healthCheck() -> str:
        """
        Check application health, return True
        """
        return True, 200

    @application.route('/jokenpo', methods=['GET'])
    def get() -> dict:
        """
        Get game winners, return the response from 
        JokenpoRepository.get_current_game_result()
        """
        return JokenpoRepository.get_current_game_result()

    @application.route('/jokenpo/detail', methods=['GET'])
    def get_detail() -> dict:
        """
        Get game details for currently registered players, return the response from 
        JokenpoRepository.get_current_game_result_details()
        """
        return JokenpoRepository.get_current_game_result_detail()

    @application.route('/jokenpo/player/<int:id>', methods=['GET'])
    def get_player(id: int) -> dict:
        """
        Get player info with id received, return return the response from
        JokenpoRepository.get_player()

        id: player's id
        """
        return JokenpoRepository.get_player(id)
    
    @application.route('/jokenpo/player', methods=['POST'])
    def post() -> dict:
        """
        Insert player into db based on package received, return the response from
        JokenpoRepository.insert_player()
        """
        return JokenpoRepository.insert_player(api.payload)

    @application.route('/jokenpo/player/<int:id>', methods=['PUT'])
    def put(id) -> str:
        """
        Change a player info based on id and package received, return the response from
        JokenpoRepository.update_move()

        id: player id
        """
        return JokenpoRepository.update_move(id, api.payload)
    
    @application.route('/jokenpo/player/<int:id>', methods=['DELETE'])
    def delete(id: int) -> str:
        """
        Deletes the player with the received id, return the response from
        JokenpoRepository.delete_player()

        id: player id
        """
        return JokenpoRepository.delete_player(id)

    
    @application.route('/jokenpo/player/all', methods=['DELETE'])
    def delete_all() -> str:
        """
        Deletes all players, return the response from
        JokenpoRepository.delete_all_players()
        """
        return JokenpoRepository.delete_all_players()