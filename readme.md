The purpose of this effort is to allow for folks who want to make projections for personal finance reason. Of course all of this could be done in Excel, but if you want to tweak and record the different scenarios this is useful. I also wanted to setup a process for writing data to Snowflake and learn some new things!

What is needed:
- Snowflake Account & "newConnection" credentials (set in the snowflake config file [.snowsql folder])
- Snowflake CLI installed locally
- Python installed locally

Technical Details:
All of this is meant to be run locally. If you download this repo, you need to do the following:



Database Objects:
    - ACCOUNT_BALANCES: Contains the balances of your account at a certain point in time.
        - Primary Key: UPDATE_DATE, ACCOUNT_NAME
        - Fields:
            UPDATE_DATE: Date the data is from (if balance for account pulled January 16 2022, value would be 2022-01-16)
            ACCOUNT_NAME: English readable account name. Something you will recognize (John's personal checking, Company Checking, etc.)
            AMOUNT: Account balance at the specific date
    - DATE_PROJECTION_LOOKUP: Contains every date from 2022 through 2029 for projecting out. Specific FREQUENCY_NAME are what you join to in order to create projections.
        - Primary Key: FREQUENCY_NAME, PROJECTION_DATE
        - Fields:
            FREQUENCY_NAME: The frequency of the expense/revenue
            PROJECTION_DATE: The date which the projection will be done on
    - RECURRING_TRANSACTIONS: Income and expenses. The basis of your projection models.
        - Primary Key: ID
        - Fields:
            ID: the PK of table 1..N
            TRANSACTION_TYPE: Contains english readable name of the type of transaction (Recurring Cost, Income, Recurring Savings, etc.)
            TRANSACTION_NAME: The english identifier for the transaction (wages, house electricity)
            MONETARY_AMOUNT: How the transaction impacts your savings and checking accounts. A cost will have a negative amount shown, income a positive.
            FREQUENCY_NAME: Join key to the DATE_PROJECTION lookup table.
            END_DATE: The last date which this transaction will occur
            INSERT_DATE: The date the transaction was inserted.
    - PROJECTIONS: Contains the transactions that will occur with a specific transaction. Used to power the visualization.
        - Primary Key: PROJECTION_ID, ID, PROJECTION_DATE
        - Fields:
            PROJECTION_ID: The identifier for the specific projection
            ID: ID from the recurring transactions table
            TRANSACTION_TYPE: TRANSACTION_TYPE from the RECURRING_TRANSACTIONS table.
            TRANSACTION_NAME: TRANSACTION_NAME from the RECURRING_TRANSACTIONS table.
            PROJECTION_DATE: PROJECTION_DATE from the DATE_PROJECTION_LOOKUP. For a monthly cost will be first of the month until 2029, or the end date of the transaction.
            MONETARY_AMOUNT: MONETARY_AMOUNT from RECURRING_TRANSACTIONS table.
            FREQUENCY_NAME: FREQUENCY_NAME from RECURRING_TRANSACTIONS table.
            INSERT_DATE: Date the projection was run.
            PROJECTION_DESCRIPTION: Description of the projection, what was included, not included, why, etc. Basically, why you ran the specific transaction.
