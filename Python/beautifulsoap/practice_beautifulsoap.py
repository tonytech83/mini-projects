from bs4 import BeautifulSoup
import requests

from datetime import datetime, timedelta

# Start and end dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 6, 30)

url = "https://rxinfinitybox.com/"

#  wod-26-05-2023/

for current_date in (start_date + timedelta(days=n) for n in range((end_date - start_date).days + 1)):
    wod_date = f'wod-{current_date.strftime("%d-%m-%Y")}'
    wod_url = url + wod_date

    response = requests.get(wod_url)

    print('=' * 50)
    print(response.status_code)

    if response.status_code == 200:
        file_path = f'output/{wod_date}.txt'
        soup = BeautifulSoup(response.text, 'html.parser')

        the_div = soup.find_all('div', class_='single-post-wrap entry-content')

        result = []
        for line in the_div:
            result.append(str(line))

        with open(file_path, 'w', encoding="utf-8") as file:
            file.write('\n'.join(l for l in result))
            print(f'WOD for {wod_date} saved!')
    else:
        print(f'No WOD for {wod_date}')

    print('=' * 50)
