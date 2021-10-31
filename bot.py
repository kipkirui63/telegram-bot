import pandas_datareader as pdR
class AssBot:
    def __init__(self):
        pass
    
    @staticmethod
    def start(update, ctx):
        update.message.reply_text("Hi, Welcome to LazyGeek Support Bot")

    @staticmethod
    def help(update, ctx):
        update.message.reply_text(
            """
                The following commands are available for our bot:

                /start -> The welcome message
                /help -> A help guide to commands of using our bot.
                /content -> The available information about LarnTechGeek Bot
                /contact ->  Our contact Information
                /stock -> Helps in Getting the stock of any given Items
            """
        )

    @staticmethod
    def content(update, ctx):
        update.message.reply_text("We offer the best tech support to building Machine Learning Models and Chatbots")

    @staticmethod
    def contact(update, ctx):
        update.message.reply_text("Call us Cellphone: 0718686209 or e-mail us on vincentedepaulo@gmail.com for our support 24/7")

    @staticmethod
    def stock(update, ctx):
        ticker = ctx.args[0]
        data = pdR.DataReader(ticker, 'yahoo')
        price = data.iloc[-1]['Close']
        update.message.reply_text(f"Current {ticker} Stock Price is ${price:.2f}")
    @staticmethod
    def conv(update, ctx):
        #The users Message
        #q = update.message.text
        update.message.reply_text(f"We are integrating a real time AI that will be able to reply to your messages soon.")
