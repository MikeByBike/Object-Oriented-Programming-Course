"""
File:           FileHandler.py
Authors:        Louis Lautz, Ayush Pradhan, Michalis Iona, Bogdan Neacsa
Description:    Reads and writes values into a savefile
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
