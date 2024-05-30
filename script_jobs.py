# A script for generating LaTeX compatible code for the 'Jobs and Opportunities' section of INDUS Newsletters
# To know more about INDUS: https://sites.google.com/view/indus-solphys/home
# Code written by Chitradeep Saha, CESSI, IISER Kolkata
# Redirect your queries to chitrodeephysics1729@gmail.com

import re
import pandas as pd


def convert_spreadsheet_url(url):    
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'    
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'    
    new_url = re.sub(pattern, replacement, url)
    return new_url


def latexscript():
    issue = input('Mention ddmmyyyy of the newsletter issue\n')
    issue=float(issue)
    url = 'https://docs.google.com/spreadsheets/d/1pkfSimtd0-Qu-5HRD-W2g0L0NpBfZric5ExJ2GBVIyo/edit#gid=1284969652'
    new_url = convert_spreadsheet_url(url)
    df= pd.read_csv(new_url)
    
    for i in range(0,len(df)):
        if df.Issue[i]==issue:
            if str(df.Position[i])!='nan':
                print('\n\n'+'----------------------'+df.Position[i]+'----------------------'+'\n\n')
            print( "\item \href{" + str(df["Link"][i]) + "}{" + str(df["About"][i]) + "}" + " --- " + str(df["Location"][i])
                  + " --- Application deadline: " + str(df["Application Deadline"][i]) + "\n")
        else:
            print('No entry found!')


if __name__ == "__main__":
    latexscript()
