from .DB import *

COD_MOVE = {
    'Lagarto': 0,
    'Spock': 1,
    'Tesoura': 2,
    'Papel': 3,
    'Pedra': 4,
}

class Repo():
    def getResult():
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

    def getPlayer(id):
        return {id : db('Jokenpo')[str(id)]}, 200

    
    def insertPlayer(package):
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
    

    def updateMove(id, package):
        modify('Jokenpo', str(id), package['item'], package['content'])
        if package['item'] == 'move':
            modify('Jokenpo', str(id), 'cod_move', COD_MOVE[package['content']])
        return {id : db('Jokenpo')[str(id)]}, 202

    def deletePlayer(id):
        try:
            delete('Jokenpo', str(id))
            return "Sucess", 200

        except:
            return "Error", 404

    def delete_allPlayers():
        delete_all('Jokenpo')

        return 'Sucess', 200

    

    


