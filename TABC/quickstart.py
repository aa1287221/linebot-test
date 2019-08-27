import json
import sys
import time
import datetime

#import Adafruit_DHT
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver

# Type of sensor, can be Adafruit_DHT.DHT11, Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
#DHT_TYPE = Adafruit_DHT.DHT22

# Example of sensor connected to Raspberry Pi pin 23
#DHT_PIN  = 23
# Example of sensor connected to Beaglebone Black pin P8_11
#DHT_PIN  = 'P8_11'

# Google Docs OAuth credential JSON file.  Note that the process for authenticating
# with Google docs has changed as of ~April 2015.  You _must_ use OAuth2 to log
# in and authenticate with the gspread library.  Unfortunately this process is much
# more complicated than the old process.  You _must_ carefully follow the steps on
# this page to create a new OAuth service in your Google developer console:
#   http://gspread.readthedocs.org/en/latest/oauth2.html
#
# Once you've followed the steps above you should have downloaded a .json file with
# your OAuth2 credentials.  This file has a name like SpreadsheetData-<gibberish>.json.
# Place that file in the same directory as this python script.
#
# Now one last _very important_ step before updating the spreadsheet will work.
# Go to your spreadsheet in Google Spreadsheet and share it to the email address
# inside the 'client_email' setting in the SpreadsheetData-*.json file.  For example
# if the client_email setting inside the .json file has an email address like:
#   149345334675-md0qff5f0kib41meu20f7d1habos3qcu@developer.gserviceaccount.com
# Then use the File -> Share... command in the spreadsheet to share it with read
# and write acess to the email address above.  If you don't do this step then the
# updates to the sheet will fail!
GDOCS_OAUTH_JSON       = 'PythonUpload.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 't2'

# How long to wait (in seconds) between measurements.
FREQUENCY_SECONDS      = 30


def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)

#print('Press Ctrl-C to quit.')
worksheet = None
while True:
    # Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
    worksheet.clear()
    for j in range(1,8):
        url="http://training.tabc.org.tw/files/901-1000-6,c0-"+str(j)+".php"
        browser = webdriver.Chrome()
        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        tabc = soup.find_all('a',class_='otabc_link')
        tabcc = soup.find_all('font')
        content = ''
        title = []
        link = []
        status = []
        for t in tabc:
            title.append(t.get_text())
            link.append(t.get('href'))
        for tt in tabcc:
            status.append(tt.get_text())
        #check = ''
        for i in range(0, len(title)):
            if '報名中' in status[i]:
                try:
                    worksheet.append_row((datetime.datetime.now().isoformat(), title[i], link[i], status[i], j))
                except:
                    # Error appending data, most likely because credentials are stale.
                    # Null out the worksheet so a login is performed at the top of the loop.
                    print('Append error, logging in again')
                    worksheet = None
                    time.sleep(FREQUENCY_SECONDS)
                    continue
            check='標題：{}\n\n網址：{}\n\n報名狀態：{}\n\n'.format(title[i],link[i],status[i])
            content+=check

        #print(content+str(j))
        browser.quit()

    break
    # Wait 30 seconds before continuing
    #print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    #time.sleep(FREQUENCY_SECONDS)
#print('over!!!')
