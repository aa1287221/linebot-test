import numpy as np
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name("read.json",scope)

client = gspread.authorize(creds)

sheet = client.open("報到系統").sheet1

data = sheet.get_all_records()

col = sheet.col_values(5)

del col[0]

my_obj = pd.Series(col)

df = pd.DataFrame(data,my_obj)

value = df.ix[id,'QRcode']
