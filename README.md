# Solution
Solution for Dkatalis take home test. You'll get:
- the historical table of accounts, cards and saving account
- the denormalized table of all tables
- the analysis of transactions

## The structure
The repo contains:
- The base folder, contains all other folders, running script, docker files, documentation
- data, contains json data of accounts, cards and saving accounts
- src, contains table solution script 


## Run the code
- build docker image `docker image build -t dkatalis-solution .`
- run image `docker run dkatalis-solution`


## Solution explanation
1. Visualize the complete historical table view of each tables in tabular format 
- get the list of json files of each data source
- read each json file
- define fields for each dictionary
- convert unix timestamp to date string for readability
- if dictionary has field `set` then normalize the fields as defined
- convert dictionary to dataframe (table)
- save it to excel for readability

2. Visualize the complete historical table view of the denormalized joined table 
- left join table accounts and saving_accounts -> table denormalized1
- left join table denormalized1 and cards -> table denormalized2

3. How many transactions has been made, when did each of them occur, and how much the value of each transaction?
- number of transaction of saving accounts -> count of not NaN value in data.balance column (0 value is included as it means that the there is transaction that make the balance 0)
- number of transaction of cards -> count of not NaN value and not 0 value in data.credit_used column (0 value is ot included because 0 means no card used)
- saving account transaction history -> get data of `data.savings_account_id`, `ts_y`, `data.balance` where `data.balance` column is not NaN
- saving account transaction history -> get data of `data.card_id`, `ts`, `data.credit_used`, `data.monthly_limit`, `data.card_number`, `data.status_y` where `data.credit_used` column is not NaN to get all the transaction context





