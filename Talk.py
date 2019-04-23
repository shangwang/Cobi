__author__ = 'Nikki'
from pb_py import main as API
import sys

# Global parameters
HOST = 'aiaas.pandorabots.com'
USER_KEY = "7d387c332ebfa536b90b7820426ed63b"
APP_ID = "1409611535153"


# gets a response from the bot
def response(text, BOT, debugMode, reset, recent):
    if (debugMode == "trace" and reset == 'reset' and recent == 'recent'):
        fullresponse = API.debug_bot(USER_KEY, APP_ID, HOST, BOT, text, session_id=True, reset=True, trace=True,
                           recent=True)
        print "Bot Response: ", fullresponse
    elif (debugMode == "trace" and reset == 'none'):
        fullresponse = API.debug_bot(USER_KEY, APP_ID, HOST, BOT, text, trace=True)
        print "Bot Response: ", fullresponse
    else:
        fullresponse = API.talk(USER_KEY, APP_ID, HOST, BOT, text)
        bot_response = fullresponse['response']

        #session_id = fullresponse['sessionid']
        print BOT + " says: \" ", bot_response, " \" "


# enables continuous talk with the bot
def talk(BOT, debugMode, recent, reset):
    print "Converse with " + BOT + "! When you are finished conversing with " + BOT + ", enter 'quit.' "
    question = raw_input("What would you like to say first? ")
    done = False
    while not done:
        if question == "quit":
            done = True
            break
        else:
            response(question, BOT, debugMode, reset, recent)
            question = raw_input("How would you like to respond?  ")



def main():
    if len(sys.argv) < 3:
        print 'usage: ./Talk.py BOT debugMode recent reset'
        sys.exit(1)

    BOT = sys.argv[1]
    debugMode = sys.argv[2]
    recent = sys.argv[3]
    reset = sys.argv[4]
    talk(BOT, debugMode, recent, reset)

    print "\n\n-------Conversation Done-------"


if __name__ == '__main__': main()