'''
:w: write
:r: read
:a: append
:r+: read and write
'''
class FilesIO:
    file = None

    def __init__(self, file):
        self.file = file

    def create():
        file = open("text_file.txt", "w")
        file.write("This is the best code ever\nSure, sir!\n")
        file.close()

    '''
    :we should loop when having multiple lines in the file
    '''
    def read():
        file = open("text_file.txt", "r")
        return file.read()
    