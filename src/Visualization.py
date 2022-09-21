import json
import os
import pandas as pd
import glob
import datetime

MAIN_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))
pd.set_option('display.max_columns', 30)

class Vizualization:
    def __init__(self):
        self.file_list_accounts = glob.glob(os.path.join(MAIN_DIR, 'data\\accounts\\','*.json'))
        self.file_list_cards = glob.glob(os.path.join(MAIN_DIR, 'data\\cards\\','*.json'))
        self.file_list_saving_accounts = glob.glob(os.path.join(MAIN_DIR, 'data\\savings_accounts\\','*.json'))
        self.df_accounts = None
        self.df_cards = None
        self.df_saving_accounts = None
        self.denormalized2 = None


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
                        "phone_number": data_accounts.get("set", {}).get("phone_number", str()),
                        "email": data_accounts.get("set", {}).get("email", str()),
                        "savings_account_id": data_accounts.get("set", {}).get("savings_account_id", str()),
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
                        "phone_number": data_accounts.get("data", {}).get("phone_number", str()),
                        "email": data_accounts.get("data", {}).get("email", str()),
                        "savings_account_id": data_accounts.get("data", {}).get("savings_account_id", str()),
                        "card_id":data_accounts.get("data", {}).get("card_id", str())
                        }
                    }
            info_account_hist.append(info_accounts)
            self.df_accounts = pd.json_normalize(info_account_hist)
        print(self.df_accounts)

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
                        "card_id": data_cards.get("id", str())[:2],
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
            self.df_cards = pd.json_normalize(info_card_hist)
        print(self.df_cards)
    
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
                        "savings_account_id": data_saving_accounts.get("id", str())[:3],
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
            self.df_saving_accounts = pd.json_normalize(info_saving_accounts_hist)
        print(self.df_saving_accounts)
    
    @staticmethod
    def timestamp_to_stringdate(ts):
        value = datetime.datetime.fromtimestamp(ts/1000, tz=datetime.timezone.utc)
        string_date = f"{value:%Y-%m-%d %H:%M:%S}"
        return string_date
    
    def denormalized_historical_table(self):
        denormalized1 = pd.merge(self.df_accounts, self.df_saving_accounts, how="left", on=["data.savings_account_id"])
        denormalized1.loc[denormalized1['op_y'] == 'u', 'ts_x'] = denormalized1.loc[denormalized1['op_y'] == 'u', 'ts_y']
        self.denormalized2 = pd.merge(denormalized1, self.df_cards, how="left", on=["data.card_id"])
        self.denormalized2.loc[self.denormalized2['op'] == 'u', 'ts_x'] = self.denormalized2.loc[self.denormalized2['op'] == 'u', 'ts']
        print(self.denormalized2)

    def transaction_analysis(self):
        print('Number of saving accounts transactions\n')
        number_of_saving_accounts_transc = self.denormalized2['data.balance'].count()
        print(number_of_saving_accounts_transc)
        print('\nNumber of credit cards transactions\n')
        number_of_credit_cards_transc = self.denormalized2['data.credit_used'].count() - self.denormalized2['data.credit_used'].isin([0]).sum()
        print(number_of_credit_cards_transc)
        print('\nSaving accounts history transactions\n')
        history_transaction_saving_accounts = self.denormalized2.loc[self.denormalized2['data.balance'].notna(), ["data.savings_account_id", "ts_y", "data.balance"]]
        print(history_transaction_saving_accounts)
        print('\nCredit cards history transactions\n')
        history_transaction_cards = self.denormalized2.loc[self.denormalized2['data.credit_used'].notna(), ["data.card_id", "ts", "data.credit_used", "data.monthly_limit", "data.card_number", "data.status_y"]]
        print(history_transaction_cards)