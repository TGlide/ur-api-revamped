import os
import re
import json
import glob
import argparse
import requests

from tqdm import tqdm
from pprint import pprint as pp


def generate_entries(pred_obj, pred_type):
    if pred_type == 'cases':
        dates = sorted([pred['date'] for pred in pred_obj])
        entries = []

        for date in dates:
            entry = {"date": date, }

            for case in pred_obj:
                if case['date'] == date and case['tipo'] == 'previsao':
                    entry['cases'] = case['casos']
                    break

            entries.append(entry)

        return entries

    elif pred_type == 'leitos':
        dates = sorted([l['data'] for l in leitos])
        entries = []

        for date in dates:
            entry = {"date": date, }

            for leito in pred_obj:
                if leito['data'] == date:
                    entry['leitos'] = leito['leitos']

            entries.append(entry)

        return entries


def main(file_dir, pred_type):
    API_URL = "https://ur-api-revamped.herokuapp.com/"
    API_URL = "http://localhost:5000/"
    API_HEADERS = {"Content-Type": "application/json"}

    print(f"\nReading {file_dir} {pred_type} file...")
    file = open(file_dir)
    prediction_obj = json.load(file)
    file.close()
    print("Generating entries...")

    if pred_type.lower() == 'cases':
        cases_city = [c for c in prediction_obj if c['city'] ==
                      'Rio de Janeiro' and c['tipo'] == 'previsao']
        cases_state = [c for c in prediction_obj if c['city'] ==
                       'Estado RJ' and c['tipo'] == 'previsao']

        city_entries = generate_entries(cases_city, pred_type.lower())
        state_entries = generate_entries(cases_state, pred_type.lower())

    elif pred_type.lower() == 'leitos':

        leitos_city = [c for c in prediction_obj if c['city'] ==
                       'Rio de Janeiro']
        leitos_state = [c for c in prediction_obj if c['city'] ==
                        'Estado RJ']

        city_entries = generate_entries(leitos_city, pred_type.lower())
        state_entries = generate_entries(leitos_state, pred_type.lower())

    else:
        print("Invalid file type.")
        return

    print("\nSending city entries...")
    for entry in tqdm(city_entries):
        requests.post(f"{API_URL}projection/city",
                      data=json.dumps(entry), headers=API_HEADERS)

    print("\nSending state entries...")
    for entry in tqdm(state_entries):
        requests.post(f"{API_URL}projection/state",
                      data=json.dumps(entry), headers=API_HEADERS)

    print("\nDone!\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Send json files to projection API')
    parser.add_argument('file', type=str, nargs=1,
                        help='JSON file to submit')
    parser.add_argument('type', type=str, nargs=1,
                        help='Type of prediction file. Can be "cases" or "leitos".')

    args = parser.parse_args()
    main(args.file[0], args.type[0])
