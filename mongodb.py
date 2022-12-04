import pymongo

client = pymongo.MongoClient("mongodb+srv://aakiliqbal:Aadiliqbal645@cluster0.fjefnuj.mongodb.net/?retryWrites=true&w=majority")
mydb = client.expense_tracker
mycol = mydb.monthly_report


def insert_period(period, incomes, expenses, comment):
    mycol.insert_one({"key": period, "incomes": incomes, "expenses": expenses, "comment": comment})

def fetch_all_periods():
    items = mycol.find()
    periods = [item["key"] for item in items]
    return periods #prints keys of all db


def get_period(period):
    items = mycol.find_one({'key':period})
    period_data = items
    return period_data
    