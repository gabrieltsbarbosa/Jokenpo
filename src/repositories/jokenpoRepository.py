from .DB import *

COD_MOVE = {
    'Lagarto': 0,
    'Spock': 1,
    'Tesoura': 2,
    'Papel': 3,
    'Pedra': 4,
}

class JokenpoRepositoy():
    def get_current_game_result() -> dict:
        """
        Get game score for currently registered players, return dict with score and
        info of all players
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

            return result, 200

        return "Not Found", 404

    def get_player(id: int) -> dict:
        """
        Get player info with id received, return dict with all player info

        id: player's id
        """
        return {id : db('Jokenpo')[str(id)]}, 200

    
    def insert_player(package: dict) -> dict:
        """
        Insert player into db based on package received, return dict with player info
        package: {
            "name": player's name
            "move": player's move
        }
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
    

    def update_move(id: int, package: dict) -> dict:
        """
        Change a player info based on id and package received, return player info 
        to check changes\n
        id: player id
        package: {
            "item": put here the item you want to change.
            "content": put here the content ou want to insert.
        }
        """
        modify('Jokenpo', str(id), package['item'], package['content'])
        if package['item'] == 'move':
            modify('Jokenpo', str(id), 'cod_move', COD_MOVE[package['content']])
        return {id : db('Jokenpo')[str(id)]}, 202

    def delete_player(id: int) -> str:
        """
        Deletes the player with the received id, returns "True" in case of success

        id: player id
        """
        try:
            delete('Jokenpo', str(id))
            return True, 200

        except:
            return False, 404

    def delete_all_players() -> str:
        """
        Deletes all players, returns "True in case of success"
        """
        delete_all('Jokenpo')

        return 'Sucess', 200

    

    


