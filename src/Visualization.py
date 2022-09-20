import json
import os
import pandas as pd
import glob
import datetime

MAIN_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

class Vizualization:
    def __init__(self):
        self.file_list_accounts = glob.glob(os.path.join(MAIN_DIR, 'data\\accounts\\','*.json'))
        self.file_list_cards = glob.glob(os.path.join(MAIN_DIR, 'data\\cards\\','*.json'))
        self.file_list_saving_accounts = glob.glob(os.path.join(MAIN_DIR, 'data\\savings_accounts\\','*.json'))

    def create_historical_table_accounts(self):
        info_account_hist = list()
        for file in self.file_list_accounts:
            with open(file) as f:
                data_accounts = json.load(f)

            if data_accounts.get('set'): 
                info_accounts = {
                    "id": data_accounts.get("id", str()),
                    "op": data_accounts.get("op", str()),
                    "ts": self.timestamp_to_stringdate(data_accounts.get("ts")),
                    "data": {
                        "account_id": data_accounts.get("set", {}).get("account_id", str()),
                        "name": data_accounts.get("set", {}).get("name", str()),
                        "address": data_accounts.get("set", {}).get("address", str()),
                        "phone_number": data_accounts.get("set", {}).get("account_id", str()),
                        "email": data_accounts.get("set", {}).get("phone_number", str()),
                        "savings_account_id": data_accounts.get("set", {}).get("savings_account_id", str()),
                        "credit_used": data_accounts.get("set", {}).get("credit_used", str()),
                        "card_id":data_accounts.get("set", {}).get("card_id", str())
                        }
                    }
                
            else:
                info_accounts = {
                    "id": data_accounts.get("id", str()),
                    "op": data_accounts.get("op", str()),
                    "ts": self.timestamp_to_stringdate(data_accounts.get("ts")),
                    "data": {
                        "account_id": data_accounts.get("data", {}).get("account_id", str()),
                        "name": data_accounts.get("data", {}).get("name", str()),
                        "address": data_accounts.get("data", {}).get("address", str()),
                        "phone_number": data_accounts.get("data", {}).get("account_id", str()),
                        "email": data_accounts.get("data", {}).get("phone_number", str()),
                        "savings_account_id": data_accounts.get("data", {}).get("savings_account_id", str()),
                        "credit_used": data_accounts.get("data", {}).get("credit_used", str()),
                        "card_id":data_accounts.get("data", {}).get("card_id", str())
                        }
                    }
            info_account_hist.append(info_accounts)
            df_accounts = pd.json_normalize(info_account_hist)
        print(df_accounts)
        #data.sort_values(by='AdmissionDate')

    def create_historical_table_cards(self):
        info_card_hist = list()
        for file in self.file_list_cards:
            with open(file) as f:
                data_cards = json.load(f)

            if data_cards.get('set'): 
                info_cards = {
                    "id": data_cards.get("id", str()),
                    "op": data_cards.get("op", str()),
                    "ts": self.timestamp_to_stringdate(data_cards.get("ts")),
                    "data": {
                        "card_id": data_cards.get("set", {}).get("card_id", str()),
                        "card_number": data_cards.get("set", {}).get("card_number", str()),
                        "credit_used": data_cards.get("set", {}).get("credit_used", 0),
                        "monthly_limit": data_cards.get("set", {}).get("monthly_limit", int()),
                        "status": data_cards.get("set", {}).get("status", str()),
                        }
                    }
                
            else:
                info_cards = {
                    "id": data_cards.get("id", str()),
                    "op": data_cards.get("op", str()),
                    "ts": self.timestamp_to_stringdate(data_cards.get("ts")),
                    "data": {
                        "card_id": data_cards.get("data", {}).get("card_id", str()),
                        "card_number": data_cards.get("data", {}).get("card_number", str()),
                        "credit_used": data_cards.get("data", {}).get("credit_used", int()),
                        "monthly_limit": data_cards.get("data", {}).get("monthly_limit", int()),
                        "status": data_cards.get("data", {}).get("status", str()),
                        }
                    }
            info_card_hist.append(info_cards)
            df_cards = pd.json_normalize(info_card_hist)
        print(df_cards)
    
    def create_historical_table_saving_accounts(self):
        info_saving_accounts_hist = list()
        for file in self.file_list_saving_accounts:
            with open(file) as f:
                data_saving_accounts = json.load(f)

            if data_saving_accounts.get('set'): 
                 info_saving_accounts = {
                    "id": data_saving_accounts.get("id", str()),
                    "op": data_saving_accounts.get("op", str()),
                    "ts": self.timestamp_to_stringdate(data_saving_accounts.get("ts")),
                    "data": {
                        "savings_account_id": data_saving_accounts.get("set", {}).get("savings_account_id", str()),
                        "balance": data_saving_accounts.get("set", {}).get("balance", int()),
                        "interest_rate_percent": data_saving_accounts.get("set", {}).get("interest_rate_percent", float()),
                        "status": data_saving_accounts.get("set", {}).get("status", str()),
                        }
                    }
                
            else:
                info_saving_accounts = {
                    "id": data_saving_accounts.get("id", str()),
                    "op": data_saving_accounts.get("op", str()),
                    "ts": self.timestamp_to_stringdate(data_saving_accounts.get("ts")),
                    "data": {
                        "savings_account_id": data_saving_accounts.get("data", {}).get("savings_account_id", str()),
                        "balance": data_saving_accounts.get("data", {}).get("balance", int()),
                        "interest_rate_percent": data_saving_accounts.get("data", {}).get("interest_rate_percent", float()),
                        "status": data_saving_accounts.get("data", {}).get("status", str()),
                        }
                    }
            info_saving_accounts_hist.append(info_saving_accounts)
            df_saving_accounts = pd.json_normalize(info_saving_accounts_hist)
        print(df_saving_accounts)
    
    @staticmethod
    def timestamp_to_stringdate(ts):
        value = datetime.datetime.fromtimestamp(ts/1000, tz=datetime.timezone.utc)
        string_date = f"{value:%Y-%m-%d %H:%M:%S}"
        return string_date
    
    def denormalized_table(self):
        pass

if __name__ == '__main__':  
    viz = Vizualization()
    viz.create_historical_table_accounts()
    viz.create_historical_table_cards()
    viz.create_historical_table_saving_accounts()