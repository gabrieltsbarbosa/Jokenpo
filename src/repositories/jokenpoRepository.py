from .DB import *

COD_MOVE = {
    'Lagarto': 0,
    'Spock': 1,
    'Tesoura': 2,
    'Papel': 3,
    'Pedra': 4,
}

class Repo():
    def get_result() -> dict:
        """
        call this to get game result
        """
        rule = ['Papel', 'Pedra', 'Lagarto', 'Spock', 
                'Tesoura', 'Papel', 'Pedra', 'Lagarto', 'Spock']
        db_jokenpo = db("Jokenpo")
        if db_jokenpo is not '':
            for id in db_jokenpo:
                score = 0
                move = db_jokenpo[id]['cod_move'] + 2
                for id_adv in db_jokenpo:
                    if id != id_adv:
                        adv = db_jokenpo[id_adv]['move']
                        if adv == rule[move + 1] or adv == rule[move - 2]:
                            score += 3

                        elif adv == rule[move]:
                            score += 1                            
                    

                modify('Jokenpo', id, 'score', score)
                
            result = db('Jokenpo')

            """delete_all('Jokenpo')"""

            return result, 200

        return "Not Found", 404

    def get_player(id: int) -> dict:
        """
        Use to get player name and move
        """
        return {id : db('Jokenpo')[str(id)]}, 200

    
    def insert_player(package: dict) -> dict:
        """
        Use to insert a player into db
        """
        jokenpo_db = db('Jokenpo')
        id = len(jokenpo_db) + 1
        player = {
            id:{
                'name': package['name'],
                'cod_move': COD_MOVE[package['move']],
                'move': package['move'],
                'score': 0
            }
        }
        insert('Jokenpo', player)
        jokenpo_db = db('Jokenpo')

        return {id : jokenpo_db[str(id)]}, 201
    

    def update_move(id: int, package: dict) -> str:
        """
        Use to change player move
        """
        modify('Jokenpo', str(id), package['item'], package['content'])
        if package['item'] == 'move':
            modify('Jokenpo', str(id), 'cod_move', COD_MOVE[package['content']])
        return {id : db('Jokenpo')[str(id)]}, 202

    def deletePlayer(id: int) -> str:
        """
        Use to delete a player
        """
        try:
            delete('Jokenpo', str(id))
            return "Sucess", 200

        except:
            return "Error", 404

    def delete_all_players() -> str:
        """
        Use to clear all players
        """
        delete_all('Jokenpo')

        return 'Sucess', 200

    

    


