# A script for generating LaTeX compatible code for the 'New Article Alert' section of INDUS Newsletters
# To know more about INDUS: https://sites.google.com/view/indus-solphys/home
# Code written by Chitradeep Saha, CESSI, IISER Kolkata
# Redirect your queries to chitrodeephysics1729@gmail.com

import re
import pandas as pd
import datetime

def convert_spreadsheet_url(url):    
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'    
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'    
    new_url = re.sub(pattern, replacement, url)
    return new_url


def latexscript():
    yyyy = int(input('Year\n'))
    mm = int(input('Month\n'))
    url = 'https://docs.google.com/spreadsheets/d/16OHUBT5WB0kiHAXvDJMs-XKKSqG46An0VoE0MhvtVXk/edit?resourcekey#gid=798690173'
    new_url = convert_spreadsheet_url(url)
    df= pd.read_csv(new_url)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'],format="%m/%d/%Y %H:%M:%S")
    
       
    for i in range(len(df)):
        if (df['Timestamp'][i]>datetime.datetime(yyyy,mm,1)) & (df['Timestamp'][i]<datetime.datetime(yyyy,mm+1,1)):
            if df["Article status"][i] == 'Accepted':
                print( "\item " + str(df["Authors' list"][i]) + ", \href{" + str(df['ADS Link.1'][i]) + "}{" +  
                    str(df['Article title'][i])+ "}. \ textit{Accepted in " + str(df["Name of the journal"][i]) + "}("+str(yyyy)+").\n")

            else:
                print( "\item " + str(df["Authors' list"][i]) + ", \href{" + str(df['ADS Link.1'][i]) + "}{" +  
                    str(df['Article title'][i])+ "}. \ textit{" + str(df["Name of the journal"][i]) + "}("+str(yyyy)+").\n")
                    
        else:
        	print("Sorry! No entry found!")
         

if __name__ == "__main__":
    latexscript()
