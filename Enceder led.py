import pyfirmata

import time

board = pyfirmata.Arduino('COM3')


while True:
    
    # led rojo
    board.digital [13]. write (1)
    time.sleep(2)
    board.digital [13]. write (0)
    time.sleep(1)
    
    # led amarillo
    board.digital [11]. write (1)
    time.sleep(3)
    board.digital [11]. write (0)
    time.sleep(1)
    
    # led verde
    board.digital [9]. write (1)
    time.sleep(1)
    board.digital [9]. write (0)
    time.sleep(3)
    
