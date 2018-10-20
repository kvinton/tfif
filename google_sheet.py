import gspread
from oauth2client.service_account import ServiceAccountCredentials
import send_email


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

        if(row['email_sent'] != 'yes') and row['admiree_1_email_address'] == 'katie@branch.co': 

          for admiree_number in ["1", "2", "3"]:
            send_email_to_admiree(admiree_number, row)
            
    return all_rows


def send_email_to_admiree(admiree_number, row):

  adj1 = row['admiree_' + admiree_number + '_adjective_1']
  adj2 = row['admiree_' + admiree_number + '_adjective_2']
  adj3 = row['admiree_' + admiree_number + '_adjective_3']
  admiree_name = row['admiree_' + admiree_number + '_first_name']
  admiree_email = row['admiree_' + admiree_number + '_email_address']  

  if(admiree_email):  
    send_email.send_email(admiree_name, admiree_email, adj1, adj2, adj3)


if __name__ == "__main__":
    get
