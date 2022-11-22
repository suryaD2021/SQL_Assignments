import snowflake.connector
#import pandas as pd
conn = snowflake.connector.connect(
          user= 'QA_KOMHAR',
          password='hI@oc9#jrO@T',
          account='NEXT_PATHWAY_PARTNER.us-east-1',
          warehouse='INFA_POC',
          database='IA_Financials'
          )

cur = conn.cursor()
sql = "SELECT ORDER_ID,SUM(CASE WHEN ORDER_TYPE = 'Credit Card' THEN ORDER_AMOUNT ELSE 0 END) CC_Amount,SUM(CASE WHEN ORDER_TYPE = 'Debit Card' THEN ORDER_AMOUNT ELSE 0 END) Debit_Card_Amount,sum(CASE WHEN ORDER_TYPE = 'UPI' THEN ORDER_AMOUNT ELSE 0 END) UPI,sum(CASE WHEN ORDER_TYPE = 'CASH' THEN ORDER_AMOUNT ELSE 0 END) CASH FROM komhar.hyd.PAYMENT_DTLS GROUP BY ORDER_ID ORDER BY ORDER_ID"
cur.execute(sql)
df = cur.fetch_pandas_all()
print(df)


