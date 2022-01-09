"""
File:           filehandler.py
Author:         Michalis Iona
Description:    Reads and writes the game states into a file
"""
class ReadWrite:
    def  write(self, filename, message):
        f = None
        try :                
            f = open(filename, 'w') 
            f.write(message) 
        except IOError as error :
            print(f'Error: {error}')
        finally :
            if f != None :
                f.close()

    def read(self, filename): 
        content = ""
        try :
            f =  open(filename, 'r')
            content = f.read()                                     
            f.close()
        except (FileNotFoundError, IOError) as error :
            print(f'Error: {error}')
        finally :
            if f != None :
                f.close()  
        return content
