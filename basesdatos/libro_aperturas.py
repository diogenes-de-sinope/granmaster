import pickle
import random


aperturas = {

'top10': ['e2e4'] * 43 + ['d2d4'] * 38 + ['g1f3'] * 10 + ['c2c4'] * 8\
        + [random.choice(['b2b3', 'g2g3', 'f2f4', 'b1c3', 'e2e3'])],

'semi-abierto': ['e2e4'],
'defensa-alekhine': ['e2e4', 'g8f6'],
'caro-kann': ['e2e4', 'c7c6'],
'defensa-francesa': ['e2e4', 'e7e6'],
'defensa-siciliana': ['e2e4', 'c7c5'],
'defensa-pirca': ['e2e4', 'd7d6', 'd2d4', 'g8f6'],

'doble-peon-rey': ['e2e4', 'e7e5'],
'gambito-rey': ['e2e4', 'e7e5', 'f2f4'],
'giuoco-piano': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4', 'f8c5'],
'gambito-evans': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4', 'f8c5', 'b2b4'],
'defensa-dos-caballos': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4', 'g8f6'],
'ruy-lopez': ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5'],

'doble-peon-dama': ['d2d4', 'd7d5', 'c2c4'],
'gambito-dama-rechazado': ['d2d4', 'd7d5', 'c2c4', 'e7e6'],
'gambito-dama-aceptado': ['d2d4', 'd7d5', 'c2c4', 'd5c4'],
'defensa-tarrasch': ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c5'],
'defensa-slav': ['d2d4', 'd7d5', 'c2c4', 'c7c6'],
'defensa-chigorin': ['d2d4', 'd7d5', 'c2c4', 'b8c6'],

'apertura-india': ['d2d4', 'g8f6', 'c2c4'],
'apetura-catalana': ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g2g3'],
'defensa-nimzo-india': ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4'],
'defensa-reina-india': ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'b7b6'],
'defensa-bogo-india': ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'f8b4'],
'defensa-rey-indio': ['d2d4', 'g8f6', 'c2c4', 'g7g6'],
'defensa-vieja-india': ['d2d4', 'g8f6', 'c2c4', 'd7d6']

}



pickle.dump(aperturas, open('libroAperturas.gm', 'wb'))


