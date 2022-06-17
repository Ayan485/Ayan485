from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

d=int(input('enter the digit\n'))

n={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35, 'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, 'F': 41, 'G': 42, 'H': 43, 'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 50, 'P': 51, 'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59, 'Y': 60, 'Z': 61}


i= 0 
j= 0
k= 0
l= 0

try:

    if d==2:

        i= 0
        j= 0

        time.sleep(5)

        for letter in str(j):
             
                    #Keyboard.press(letter)
                    #Keyboard.release(letter)
             
                    for letter in str(i):
             
                        #Keyboard.press(letter)
                        #Keyboard.release(letter)        #typer
             
                        time.sleep(0.015)
             
                        #Keyboard.press(Key.enter)
             
                        time.sleep(0.015)
             
                        #Keyboard.release(Key.enter)

        for i in n:
            
            if i == 'Z':
                i= 9
                j= 0
                
                print(j,i,'\n')
                
                for letter in str(j):
             
                    #Keyboard.press(letter)
                    #Keyboard.release(letter)
             
                    for letter in str(i):
             
                        #Keyboard.press(letter)
                        #Keyboard.release(letter)        #typer
             
                        time.sleep(0.015)
             
                        #Keyboard.press(Key.enter)
             
                        time.sleep(0.015)
             
                        #Keyboard.release(Key.enter)
                                    
                
                for j in n:
                    for i in n:
                            
                            print(j,i,'\n')
                            
                            for letter in str(j):
             
                                #Keyboard.press(letter)
                                #Keyboard.release(letter)
             
                                for letter in str(i):
             
                                    #Keyboard.press(letter)
                                    #Keyboard.release(letter)        #typer
             
                                    time.sleep(0.015)
             
                                    #Keyboard.press(Key.enter)
             
                                    time.sleep(0.015)
             
                                    #Keyboard.release(Key.enter)

            else:
                
                print(j,i,'\n')
                
                for letter in str(j):
             
                    #Keyboard.press(letter)
                    #Keyboard.release(letter)
             
                    for letter in str(i):
             
                        #Keyboard.press(letter)
                        #Keyboard.release(letter)        #typer
             
                        time.sleep(0.015)
             
                        #Keyboard.press(Key.enter)
             
                        time.sleep(0.015)
             
                        #Keyboard.release(Key.enter)

    if d==3:
        i= 0
        j= 0
        k= 0
        
        time.sleep(5)
        
        for letter in str(k):
             
            #Keyboard.press(letter)
            #Keyboard.release(letter)          

            for letter in str(j):

                #Keyboard.press(letter)
                #Keyboard.release(letter)

                for letter in str(i):

                    #Keyboard.press(letter)
                    #Keyboard.release(letter)        #typer

                    time.sleep(0.015)

                    #Keyboard.press(Key.enter)

                    time.sleep(0.015)

                    #Keyboard.release(Key.enter) 

        for i in n:
            
            if i == 'Z':
                i= 9
                j= 0
                k= 0
                
                print(k,j,i,'\n')
                
                for letter in str(k):
                    
                    #Keyboard.press(letter)
                    #Keyboard.release(letter)          

                    for letter in str(j):
                
                        #Keyboard.press(letter)
                        #Keyboard.release(letter)
                
                        for letter in str(i):
                
                            #Keyboard.press(letter)
                            #Keyboard.release(letter)        #typer
                
                            time.sleep(0.015)
                
                            #Keyboard.press(Key.enter)
                
                            time.sleep(0.015)
                
                            #Keyboard.release(Key.enter)
                                    
                for j in n:
                    for i in n:
                            
                            print(k,j,i,'\n')
                            
                            for letter in str(k):
             
                                #Keyboard.press(letter)
                                #Keyboard.release(letter)

                                for letter in str(j):
                
                                    #Keyboard.press(letter)
                                    #Keyboard.release(letter)
                
                                    for letter in str(i):
                
                                        #Keyboard.press(letter)
                                        #Keyboard.release(letter)        #typer
                
                                        time.sleep(0.015)
                
                                        #Keyboard.press(Key.enter)
                
                                        time.sleep(0.015)
                
                                        #Keyboard.release(Key.enter)

            z= ord('Z')+ord('Z')

            if z == 180:
                
                for k in n:
                    for j in n:
                        for i in n:
                            
                            print(k,j,i,'\n')
                            
                            for letter in str(k):
             
                                #Keyboard.press(letter)
                                #Keyboard.release(letter)          
             
                                for letter in str(j):
             
                                    #Keyboard.press(letter)
                                    #Keyboard.release(letter)
             
                                    for letter in str(i):
             
                                        #Keyboard.press(letter)
                                        #Keyboard.release(letter)        #typer
             
                                        time.sleep(0.015)
             
                                        #Keyboard.press(Key.enter)
             
                                        time.sleep(0.015)
             
                                        #Keyboard.release(Key.enter)

            else:    
                
                print(k,j,i,'\n')
                
                for letter in str(k):
             
                    #Keyboard.press(letter)
                    #Keyboard.release(letter)          

                    for letter in str(j):
                
                        #Keyboard.press(letter)
                        #Keyboard.release(letter)
                
                        for letter in str(i):
                
                            #Keyboard.press(letter)
                            #Keyboard.release(letter)        #typer
                
                            time.sleep(0.015)
                
                            #Keyboard.press(Key.enter)
                
                            time.sleep(0.015)
                
                            #Keyboard.release(Key.enter)

    if d==4:

        time.sleep(5)

        for i in n:
            
            if i == 'Z':
                i= 9
                j= 0
                k= 0
                l= 0
                
                #print(l,k,j,i,'\n')
                
                for letter in str(l):
                   
                    Keyboard.press(letter)
                    Keyboard.release(letter)

                    for letter in str(k):
                   
                        Keyboard.press(letter)
                        Keyboard.release(letter)

                        for letter in str(j):
                        
                            Keyboard.press(letter)
                            Keyboard.release(letter)
                        
                            for letter in str(i):
                        
                                Keyboard.press(letter)
                                Keyboard.release(letter)        #typer
                        
                                time.sleep(0.015)
                        
                                Keyboard.press(Key.enter)
                        
                                time.sleep(0.015)
                        
                                Keyboard.release(Key.enter)
                                    
                for j in n:
                    for i in n:
                            
                            #print(l,k,j,i,'\n')
                            
                            for letter in str(l):
                   
                                Keyboard.press(letter)
                                Keyboard.release(letter)

                                for letter in str(k):
                            
                                    Keyboard.press(letter)
                                    Keyboard.release(letter)

                                    for letter in str(j):
                                    
                                        Keyboard.press(letter)
                                        Keyboard.release(letter)
                                    
                                        for letter in str(i):
                                    
                                            Keyboard.press(letter)
                                            Keyboard.release(letter)        #typer
                                    
                                            time.sleep(0.015)
                                    
                                            Keyboard.press(Key.enter)
                                    
                                            time.sleep(0.015)
                                    
                                            Keyboard.release(Key.enter)
            z= ord('Z')+ord('Z')

            if z == 180:
                
                for k in n:
                    for j in n:
                        for i in n:
                            
                            #print(l,k,j,i,'\n')
                            
                            for letter in str(l):
                   
                                Keyboard.press(letter)
                                Keyboard.release(letter)

                                for letter in str(k):
                            
                                    Keyboard.press(letter)
                                    Keyboard.release(letter)

                                    for letter in str(j):
                                    
                                        Keyboard.press(letter)
                                        Keyboard.release(letter)
                                    
                                        for letter in str(i):
                                    
                                            Keyboard.press(letter)
                                            Keyboard.release(letter)        #typer
                                    
                                            time.sleep(0.015)
                                    
                                            Keyboard.press(Key.enter)
                                    
                                            time.sleep(0.015)
                                    
                                            Keyboard.release(Key.enter)

            y= ord('Z')+ord('Z')+ord('Z')

            if y == 270:

                for l in n:
                    for k in n:
                        for j in n:
                            for i in n:

                                #print(l,k,j,i,'\n')
                                
                                for letter in str(l):

                                    Keyboard.press(letter)
                                    Keyboard.release(letter)

                                    for letter in str(k):
                                        
                                        Keyboard.press(letter)
                                        Keyboard.release(letter)          
                                        
                                        for letter in str(j):
                                            
                                            Keyboard.press(letter)
                                            Keyboard.release(letter)
                                            
                                            for letter in str(i):

                                                Keyboard.press(letter)
                                                Keyboard.release(letter)        #typer

                                                time.sleep(0.015)

                                                Keyboard.press(Key.enter)

                                                time.sleep(0.015)

                                                Keyboard.release(Key.enter)

            else:    
                
                #print(l,k,j,i,'\n')
                
                for letter in str(l):
                   
                    Keyboard.press(letter)
                    Keyboard.release(letter)

                    for letter in str(k):
                   
                        Keyboard.press(letter)
                        Keyboard.release(letter)

                        for letter in str(j):
                        
                            Keyboard.press(letter)
                            Keyboard.release(letter)
                        
                            for letter in str(i):
                        
                                Keyboard.press(letter)
                                Keyboard.release(letter)        #typer
                        
                                time.sleep(0.015)
                        
                                Keyboard.press(Key.enter)
                        
                                time.sleep(0.015)
                        
                                Keyboard.release(Key.enter)

except KeyboardInterrupt: # ctrl + c
    
    print("program terminated")

    exit()
