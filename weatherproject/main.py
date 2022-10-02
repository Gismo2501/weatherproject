import os
import requests
from dotenv import load_dotenv
import json
import csv


# Load constants from .env file (API Key, Latitude and Longitude Postion)
load_dotenv()
AGS = os.getenv('AGS')
PATH_File = os.getenv('PATH_File')

# Functions
# wid = WarningID from the API(Format:
# dwd.2.49.0.0.276.0.DWD.PVW.1661520240000.938b3d41-e91d-4dcc-88d0-30c4f480d6c9.MUL)
# headline_warning = Headline of the warning
# severity_warning = severity of the warning
# sent_warning = Date of the warning


def WriteToCSV(path, id_warning, headline_warning, severity_warning, sent_warning):
    rowdata = {
        'id': id_warning,
        'headline': headline_warning,
        'severity': severity_warning,
        'sent': sent_warning
    }

    # read header automatically
    with open(path, "r") as f:
        reader = csv.reader(f)
        for header in reader:
            break

    # add row to CSV file
    with open(path, "a", encoding='utf-8', newline='') as csv_data:
        writer = csv.DictWriter(csv_data, fieldnames=header, delimiter=',')
        writer.writerow(rowdata)


# Make & Send request to OpenWeatherMap.com
d = requests.get("https://nina.api.proxy.bund.dev/api31/dashboard/"+AGS+".json")
warningdata = json.loads(d.text)
for warningdatadict in warningdata:
    provider = warningdatadict["payload"]["data"].get("provider")
    if "DWD" in provider:
        warningid = warningdatadict["id"]
        headline = warningdatadict["payload"]["data"].get("headline")
        severity = warningdatadict["payload"]["data"].get("severity")
        sent = warningdatadict["sent"]
        WriteToCSV(PATH_File, warningid, headline, severity, sent)


