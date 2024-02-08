import pymongo
import config

def init_db(bot):
    client = pymongo.MongoClient(config.MONGODB_CONNECTION_STRING)
    db = client["middleman"]
    bot.db = db
    bot.transaction_collection = db["transactions"]
    bot.user_balance_collection = db["user_balances"]
