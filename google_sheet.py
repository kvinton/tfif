import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_all_rows_from_db():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('tfif-a623c8b3e1a6.json', scope)

    gc = gspread.authorize(credentials)

    wks = gc.open("The Future is Female (Responses)").sheet1

    all_rows = wks.get_all_records()


    for row in all_rows:
        print("Timestamp: " + row['timestamp'])
        print("Sender email: " + row['sender_email_address'])
        print("Sender first name: " + row['sender_first_name'])
        print("Sender work: " + row['sender_work'])
        print("Admiree first name: " + row['admiree_1_first_name'])
        print("Admiree email address: " + row['admiree_1_email_address'])
        print("Adjective 1: " + row['admiree_1_adjective_1'])
        print("Adjective 2: " + row['admiree_1_adjective_2'])
        print("Adjective 3: " + row['admiree_1_adjective_3'])
        print("More info: " + row['admiree_1_more_info'])

    return all_rows




