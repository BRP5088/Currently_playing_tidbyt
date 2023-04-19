import json
import pickle
import os
from Person import *
from helper_functions import *

from flask import Flask, render_template, request
app = Flask(__name__)


peopleLst = []
# global peopleLst
# gameDisplayFileFolderPath = os.path.join('B:', os.path.sep+'Game Display Files')
# gameMapFilePath = os.path.join('B:', os.path.sep+'Game Display Files'+os.path.sep, 'gameMap.save')
gameDisplayFileFolderPath = os.path.join( '..' + os.path.sep+'..' +os.path.sep + 'mnt' + os.path.sep, 'BrettNAS' + os.path.sep, 'Game Display Files')
peopleLstFilePath = os.path.join('..' + os.path.sep+'..' +os.path.sep + 'mnt' + os.path.sep, 'BrettNAS' + os.path.sep, 'Game Display Files'+os.path.sep, 'peopleLst.save')
# ../../mnt/BrettNAS/Game Display Files

# {"Brett": ["Atomic heart"], "Taylere": ["Stray", "Pokemon Violet", "It Takes Two", "Zero Dawn Horizon"]}


def setup_peopleLst():
    global peopleLst
    if os.path.exists( peopleLstFilePath ):
        with open(peopleLstFilePath, 'rb') as file:
            peopleLst = pickle.load( file )
            file.close()
        print( 'Finished loading peopleLst' )
    else:
        print( 'There isn\'t a save file to read in. Creating List.' )
        peopleLst = []


@app.route("/savePeopleLst", methods = ['GET', 'POST' ] )
def save_peopleLst():
    if request.method == 'GET':
        with open(peopleLstFilePath, 'wb') as file:
            pickle.dump( peopleLst, file )
            file.close()
        print( 'successfully saved peopleLst!' )
        return "get - success"
    
    # elif request.method == 'POST':
        

@app.route("/editPerson/<name>", methods=[ 'POST' ])
def edit_person( name ):
    print( f'peopleLst === { peopleLst }' )

    data_json = request.json
    person = get_person( peopleLst, name )

    for key in data_json:

        if key == 'games':
            person.remove_game( data_json[key] )
        elif key == 'game_covers':
            pass
        elif key == 'name_text_color' or 'game_text_color':
            person.update_text_color(key, data_json[key] )

    print( f'peopleLst === { peopleLst }' )
    save_peopleLst()

    return "success"

@app.route("/addPerson", methods=[ 'POST' ] )
def add_person():
    print(f'request === {request}')

    person_json = request.json
    person_json = person_json if type( person_json ) == list else [ person_json ] # This makes it a list so I can iterate over it next no matter how many people are added

    for person_obj in person_json:
        p = Person( person_obj['name'] )

        for game in person_obj['games']:
            p.add_game( game )
            game_cover = person_obj.get('game_cover', False )
            p.add_game_cover(game, game_cover.get( game ) if game_cover else 'N/a' )

        peopleLst.append( p )

    with open(peopleLstFilePath, 'wb') as file:
        pickle.dump(peopleLst, file)
        file.close()
    print('successfully saved peopleLst!')
    return "post - success"


@app.route("/")
def index():
    return render_template( './index.html', peopleLst=peopleLst )


@app.route("/getPeopleLst", methods = [ 'GET' ] )
def getpeopleLst():
    if len( peopleLst ) == 0:
        setup_peopleLst()

    return json.dumps([obj.__dict__ for obj in peopleLst])






def setup_app(app):
    setup_peopleLst()

setup_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
    # app.run(host='127.0.0.1', port=30006, debug=True)

    # gameMap['Brett'] = ['Atomic heart']
    # gameMap['Taylere'] = [ 'Stray', 'Pokemon Violet', 'It Takes Two', 'Zero Dawn Horizon'  ]
