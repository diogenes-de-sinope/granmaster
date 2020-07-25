import time
import pickle
import random
from stockfish import Stockfish

stockfish = Stockfish("/usr/games/stockfish", parameters={'Contempt': 0})
stockfish.set_depth(30)
#print(stockfish.get_parameters())


class Juego:
    ''' Llama a stockfish y efectua e imprime la jugada.

[Historial]

[Pendiente]
-> Auditar la evaluacion de la jugada. Intentar actualizarla cada ej 3 s 

copyleft: diogenes | cyberpunklabs@protonmail.com

'''
    header = dict(
        evento = 'Partida CyberPunkChess',
        lugar = 'Laboratorios CyberPunk',
        fecha = '20 abril 2020',
        ronda = 1,
        jugador_blancas = 'Perfil 1',
        jugador_negras = 'Stockfish Level {} Depth {}'.format(10, 30),
        resultado = '*/*')
    
    juego = []
    n_movimiento = 0
    n_jugada = 1
    jugada_correcta = True
    salir = False


    def __init__(self):

        line1 = '#' * 20
        line2 = '##   Bienvenido   ##'
        line3 = '##     v.0.1      ##'
        line4 = '#' * 20

        self.imprimirGenerico(line1, line2, line3, line4)
        time.sleep(0.5)


        self.configuracion()           
        self.color = 'n'

        
    def jugada(self):
        if self.color == 'b':
            pass
        
        ######################
        ### Para las negras
        ######################
        else:
            aperturas = ['e2e4'] * 43 + ['d2d4'] * 38 + ['g1f3'] * 10 + ['c2c4'] * 8\
                + [random.choice(['b2b3', 'g2g3', 'f2f4', 'b1c3', 'e2e3'])]

            if Juego.jugada_correcta:
                self.imprimirGenerico('Replicante v{}.{}'.format(10,5), 'está pensando...')

                if Juego.n_jugada == 1:
                    blancas = random.choice(aperturas)

                else:
                    blancas = stockfish.get_best_move_time(Juego.dificultad)
                    
                Juego.juego.append(blancas)
                Juego.n_movimiento += 1
                
                stockfish.set_position(Juego.juego)

                evaluacion = stockfish.get_evaluation()
                Juego.evaluacion = evaluacion['value'] / 100


            self.imprimirNegras()
            

            negras = input().lower()

            if (len(negras) > 1) & (stockfish.is_move_correct(negras)):
                Juego.juego.append(negras)

                stockfish.set_position(Juego.juego)

                Juego.n_movimiento += 1
                Juego.n_jugada += 1

                Juego.jugada_correcta = True
                self.guardarJuego('respaldo')
                self.imprimirNegras()

            elif negras == 's':
                self.guardarJuego('juego1')
                Juego.jugada_correcta = False
                
            elif negras == 'a':
                self.deshacer()
                Juego.jugada_correcta = False

            elif negras == 'o':
                self.imprimirOpciones()
                Juego.jugada_correcta = False

            elif negras == 'b':
                Juego.jugada_correcta = False
                print(stockfish.get_board_visual())

            else:
                self.imprimirGenerico('{} incorrecta!'.format(negras))
                Juego.jugada_correcta = False

                time.sleep(0.5)


    ### Fin del loop principal 
    ###########################################################


    #################
    ### PANTALLAS ###
    #################

    ### Imprimir pantalla para negras            
    def imprimirNegras(self):
        self.formatearJuego()

                #-------------------         
        line1 = '{}  [ A | S | O ]'.format(Juego.evaluacion)
        line2 = '...{} {}.{}'.format(Juego.ultimas[0],   Juego.n_jugada - 1, Juego.ultimas[1])
        line3 = '...{} {}.{} *'.format(Juego.ultimas[2], Juego.n_jugada - 0, Juego.ultimas[3])
        line4 = 'Ingresa jugada...'


        print("{}\n{}\n{}\n{}\n".format(line1, line2, line3, line4))


    ### Imprimir opciones            
    def imprimirOpciones(self):

                #-------------------
        line1 = 'Opciones     [ 0 ]'  
        line2 = '(1)Ver (2)Analizar'
        line3 = '(3)PGN (4)Salir'
        line4 = '(5)¡Únete!'

        print("{}\n{}\n{}\n{}\n".format(line1, line2, line3, line4))

        opcion = input()

        if opcion == '0':
            pass
        
        elif opcion == '4':
            self.imprimirGenerico('Juego guardado en', "'juegos/respaldo.cpc'")
            time.sleep(0.5)
            
            Juego.salir = True
            
        else:
            self.imprimirGenerico('Por implementar...')
            time.sleep(0.5)
            


    def imprimirGenerico(self, line1='', line2='', line3='', line4=''):
        print("{}\n{}\n{}\n{}\n".format(line1, line2, line3, line4))
        time.sleep(0.5)
            

        
    ### Deshacer jugada
    def deshacer(self):

        if len(Juego.juego) > 1:
            del Juego.juego[-2:]

            stockfish.set_position(Juego.juego)

            Juego.n_jugada     -= 1
            Juego.n_movimiento -= 2
               
        else:
            self.imprimirGenerico('Inicio del juego !!')
            time.sleep(0.5)


    ### Guardar juego
    def guardarJuego(self, tipo):

        diccionario = dict(header=Juego.header, juego=Juego.juego, pgn=[])

        if tipo == 'respaldo':
            pickle.dump(diccionario, open('juegos/{}.cpc'.format(tipo), 'wb'))

        else:
            perfiles = ['perfil1', 'perfil2', 'perfil3',\
                        'perfil4', 'perfil5', 'perfil6']

                                   #-------------------  
            self.imprimirGenerico('Selecciona perfil:  ',
                                  '(1)Perfil  (2)Perfil',
                                  '(3)Perfil  (4)Perfil',
                                  '(5)Perfil  (6)Perfil')
            
            
            opcion = input()

            opcion = perfiles[int(opcion) - 1]
            
            pickle.dump(diccionario, open('juegos/{}.cpc'.format(opcion), 'wb'))

            self.imprimirGenerico('Juego guardado en', "'/juegos/{}.cpc'!!".format(opcion))
            time.sleep(2)


            
    ### Formatear juego
    def formatearJuego(self):
        
        if len(Juego.juego) <= 4:
            Juego.ultimas = Juego.juego + ([' '] * (4 - len(Juego.juego)))

        else:
            Juego.ultimas = Juego.juego[-4:]

            


    def configuracion(self):

        ### Perfil o juego nuevo
        while True:
            self.imprimirGenerico('CyberPunkChess', line3='(1)Juego nuevo', line4='(2)Cargar perfil')

            opcion = input()

            try:
                opcion = int(opcion)
            except ValueError:
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)

                continue

            if opcion == 1:
                self.imprimirGenerico('¡Juego nuevo!')
                time.sleep(0.5)

                break

            elif opcion == 2:
                self.imprimirGenerico('[No implementado]')
                time.sleep(0.5)

            else: 
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)



        ### Inteligencia UCI (Modelo replicante)
        while True:
            self.imprimirGenerico('Modelo Replicante?', '(1-20)')

            opcion = input()

            try:
                opcion = int(opcion)
            except ValueError:
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)

                continue

            if (opcion >= 1) & (opcion <= 20):
                stockfish.set_skill_level(opcion)

                self.imprimirGenerico('Replicante', 'Modelo: {}.'.format(opcion))
                time.sleep(0.5)

                break

            else:
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)
            

        ### Version replicante (tiempo jugada)        
        while True:
            self.imprimirGenerico('Versión Replicante?','(1-600)')

            opcion = input()

            try:
                opcion = int(opcion)
            except ValueError:
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)

                continue

            if (opcion >= 1) & (opcion <= 600):
                Juego.dificultad = opcion * 1000

                self.imprimirGenerico('Replicante', 'Versión {}.'.format(opcion))
                time.sleep(0.5)

                break

            else:
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)
            


        ### Color        
        while True:
            self.imprimirGenerico('Elige color', '(b) Blancas', '(n) Negras', '(a) Aleatorio')

            opcion = input().lower()

            try:
                opcion = str(opcion)
            except ValueError:
                self.imprimirGenerico('Opción incorrecta!')
                time.sleep(0.5)

                continue


            if opcion == 'a':
                opcion = random.choice(['b', 'n'])

                self.imprimirGenerico('Sorteando...')
                time.sleep(0.5)

            
            if opcion == 'b':
                self.color = 'b'

                self.imprimirGenerico('Juegas con blancas.')
                time.sleep(0.5)
                break

            elif opcion == 'n':
                self.imprimirGenerico('Juegas con negras.')
                time.sleep(0.5)
                break

            else:
                self.imprimirGenerico('¡Opción incorrecta!')
                time.sleep(0.5)



        self.imprimirGenerico('Iniciando juego...')
        time.sleep(0.5)