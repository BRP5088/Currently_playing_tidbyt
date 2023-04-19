
RED = "#FF3333"
ORANGE = "#FF9933"
YELLOW = "#FFFF33"
LIGHT_GREEN = "#99FF33"
GREEN = "#33FF33"
LIGHT_BLUE = "#33FFFF"
BLUE = "#3399FF"
PURPLE = "#3333FF"
VIOLET = "#9933FF"
PINK = "#FF33FF"
DARK_PINK = "#FF3399"
LIGHT_GREY = "#C0C0C0"
MID_GREY = "#404040"
DARK_GREY = "#808080"
BLACK = "#000000"
WHITE = "#FFFFFF"


class Person:
    def __init__(self, name):
        self.name = name
        self.games = []
        self.game_covers = {}
        self.name_text_color = LIGHT_GREEN
        self.game_text_color = PURPLE

    # def __repr__(self) -> str:
    #     return f"{self.name} is currently playing { ', '.join( self.games ) if len( self.games) > 1 else self.games[0] }" 
    
    def add_game(self, game_name ):
        self.games.append( game_name )

    def remove_game(self, game_name ):
        self.games.remove( game_name)
        self.remove_game_cover( game_name )
    
    def add_game_cover( self, game_name, game_cover_url ):
        self.game_covers[ game_name ] = game_cover_url
    
    def remove_game_cover( self, game_name ):
        self.game_covers.pop( game_name )

    def update_game_cover( self, game_name, new_url ):
        self.game_covers[ game_name ] = new_url
    
    def update_text_color( self, key, new_color ):
        globals_map = globals()

        if key == 'game_text_color':
            # self.game_text_color = globals_map[ new_color ]
            self.game_text_color = new_color
        else:
            # self.name_text_color = globals_map[ new_color ]
            self.name_text_color = new_color
