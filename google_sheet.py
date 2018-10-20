import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('tfif-a623c8b3e1a6.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("The Future is Female (Responses)").sheet1

all_rows = wks.get_all_records()

