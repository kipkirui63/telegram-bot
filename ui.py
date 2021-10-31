from telegram import ext as Ext

from bot import  AssBot

with open('token.key', 'r') as file_:
    TOKEN = file_.read()

def main():
    #Creating our update
    updater = Ext.Updater(TOKEN, use_context=True)
    #Creating a didpatcher
    dispatcher = updater.dispatcher
    #Adding Command Handlers to handle Commands
    dispatcher.add_handler(Ext.CommandHandler("start", AssBot.start))
    dispatcher.add_handler(Ext.CommandHandler("contact", AssBot.contact))
    dispatcher.add_handler(Ext.CommandHandler("help", AssBot.help))
    dispatcher.add_handler(Ext.CommandHandler("context", AssBot.content))
    dispatcher.add_handler(Ext.CommandHandler("stock", AssBot.stock))
    #Message hadlers
    dispatcher.add_handler(Ext.MessageHandler(Ext.Filters.text, AssBot.conv))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()