import re
import pandas as pd
import math

def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)
    return new_url


def latexscript():
    issue = input('Mention ddmmyyyy of the newsletter issue\n')
    issue=float(issue)
    url = 'https://docs.google.com/spreadsheets/d/1pkfSimtd0-Qu-5HRD-W2g0L0NpBfZric5ExJ2GBVIyo/edit#gid=1284969652'
    new_url = convert_google_sheet_url(url)
    df= pd.read_csv(new_url)
    for i in range(0,len(df)):
        if df.Issue[i]==issue:
            if str(df.Position[i])!='nan':
                print('\n\n'+'----------------------'+df.Position[i]+'----------------------'+'\n\n')
            print( "\item \href{" + df["Link"][i] + "}{" + df["About"][i] + "}" + " --- " + df["Location"][i]
                  + " --- Application deadline: " + df["Application Deadline"][i] + "\n")
        else:
            print('No entry found!')

    
    
if __name__ == "__main__":
    latexscript()
