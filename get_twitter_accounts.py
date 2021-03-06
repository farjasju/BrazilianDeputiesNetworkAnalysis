import time
import csv
import os
import twitter
from config import API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET


def fetch_accounts(api):
    accounts_fetched = 0
    with open(os.path.join('data', 'accounts_raw_list.txt'), mode='w') as raw_list:
        with open(os.path.join('data', 'deputies_names.csv'), mode='r') as list_file:
            reader = csv.reader(list_file)
            with open(os.path.join('data', 'deputies_accounts.csv'), mode='w') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(['name', 'party', 'screen_name', 'id'])
                for line in list_file:
                    name, party = line.strip('\n').split(',')
                    for user in api.GetUsersSearch(name):
                        if "deputad" in user.description.lower():
                            accounts_fetched += 1
                            raw_list.write(
                                '"@' + user.screen_name + '",' + '\n')
                            writer.writerow(
                                [name, party, user.screen_name, user.id_str])
                            print("Number of accounts found:", accounts_fetched)
                    time.sleep(1)


def main(api):
    fetch_accounts(api)


if __name__ == '__main__':
    api = twitter.Api(consumer_key=API_KEY,
                      consumer_secret=API_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=TOKEN_SECRET)
    main(api=api)
