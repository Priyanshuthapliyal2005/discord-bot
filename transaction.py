import pymongo
import config
class Transaction:
    def __init__(self, db):
        self.transaction_collection = db["transactions"]

    def initiate_transaction(self, user_id, user_to_pay_id, from_currency, to_currency, amount, timestamp):
        transaction_document = {
            "user_id": user_id,
            "user_to_pay_id": user_to_pay_id,
            "from_currency": from_currency.lower(),
            "to_currency": to_currency.lower(),
            "amount": float(amount),
            "status": "pending",
            "timestamp": timestamp
        }
        self.transaction_collection.insert_one(transaction_document)
        return transaction_document['_id']

    def confirm_transaction(self, user_id, transaction_id):
        transaction_document = self.transaction_collection.find_one({"_id": transaction_id, "user_id": user_id, "status": "pending"})
        if transaction_document:
            self.transaction_collection.update_one({"_id": transaction_id}, {"$set": {"status": "completed"}})
            return True
        return False
