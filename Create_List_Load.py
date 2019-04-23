__author__ = 'Nikki'
from pb_py import main as API
import sys
import os

# Global parameters
HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"

'''
Program allows you to do the following with a given bot belonging to the ASU Pandorabots account:
* Create
* Compile
* Upload a directory
* Upload a single file
* Get a list of files

IMPORTANT
    For any file upload, the files have to be in the same directory as the program
'''



# Create bot - only use this if want to create a new bot; need a different bot name
def createBot(BOT):
    result = API.create_bot(USER_KEY, APP_ID, HOST, BOT)
    print result

def deleteBot(BOT):
    result = API.delete_bot(USER_KEY, APP_ID, HOST, BOT)
    print result

# provides a list of all the current files associated with a bot
def listFiles(BOT):
    fileList = API.list_files(USER_KEY, APP_ID, HOST,BOT)
    print "File List is...", fileList


# compiles bot - need to run this if adding a new file/before chatting
def compileBot(BOT):
    compiled = API.compile_bot(USER_KEY, APP_ID, HOST, BOT)
    print "Compiled: ", compiled


def upload(BOT, dirf):
    print dirf
    print os.listdir(dirf)
    for filename in os.listdir(dirf):
        print filename
        result = API.upload_file(USER_KEY, APP_ID, HOST, BOT, filename)
        print result


def uploadSingleFile(BOT, filename):
    result = API.upload_file(USER_KEY, APP_ID, HOST, BOT, filename)
    print result

def resetBot(BOT):
    result = API.debug_bot(USER_KEY, APP_ID, HOST, BOT, "generic", reset=True)
    print result

def deleteFile(BOT, filename):
    result = API.delete_file(USER_KEY, APP_ID, HOST, BOT, filename)
    print result

def main():
    if len(sys.argv) < 3:
        print 'usage: ./Create_List_Load.py command BOT optional'
        sys.exit(1)

    command = sys.argv[1]
    BOT = sys.argv[2]

    if command == "list":
        listFiles(BOT)
    elif command == "create":
        createBot(BOT)
    elif command == "delete":
        deleteBot(BOT)
    elif command == "reset":
        resetBot(BOT)
    elif command == "upload":
        if len(sys.argv) != 4:
            print "Need directory to upload"
            sys.exit(1)
        filedirectory = sys.argv[3]
        upload(BOT, filedirectory)
    elif command == "compile":
        compileBot(BOT)
    elif command == "uploadsingle":
        if len(sys.argv) != 4:
            print "Need file to upload"
            sys.exit(1)
        filename = sys.argv[3]
        uploadSingleFile(BOT, filename)
    elif command == "list":
        listFiles(BOT)
    elif command == "deleteFile":
        if len(sys.argv) != 4:
            print "Need file to delete"
            sys.exit(1)
        filename = sys.argv[3]
        deleteFile(BOT, filename)
    else:
        print "Command not found"

    print "\n\n-------Done-------"


if __name__ == '__main__': main()
