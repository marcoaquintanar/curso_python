class Sport:
    ''' Clase para representar un deporte '''

    def __init__(self, name:str, players:int, league:str):
        ''' Constructor de Sport '''
        self.name = name
        if isinstance(players, int): # verificamos que players sea un entero
            self.players = int(players)
        else:
            self.players = players
        self.league = league

    def __str__(self)->str:
        ''' Representacion de sport'''
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)->str:
        ''' Representacion en string de Sport '''
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        ''' Convertir Sport a JSON '''
        return {"name":self.name, "players":self.players, "league":self.league}
    
if __name__ == "__main__":
        nfl = Sport("Football", 11, "NFL")
        print(nfl)
        print(repr(nfl))
        print(nfl.to_json())