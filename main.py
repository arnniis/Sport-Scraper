from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

url = 'chrome://newtab'
url1 = 'https://www.espn.com/nba/schedule'
url2 = 'https://www.espn.com/soccer/schedule'
url3 = 'https://www.espn.com/nfl/schedule'
url4 = 'https://www.espn.com/mlb/schedule'
url5 = 'https://www.espn.com/nhl/schedule'
url6 = 'https://www.espn.com/mma/schedule'

path = 'D:\\code\\fiverr\\mikepodge\\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(executable_path = path, options=chrome_options)
driver.get(url)
time.sleep(5)

print()
print()
print()
print()
print()
print()
print()
print()
print('source: ESPN')
print('                  Sport fixtures')
print()
print('                   bot by arnis')
print()
print('Press 1 to see the Basketball matches')
print('Press 2 to see the Soccer Matches')
print('Press 3 to see the American Football matches')
print('Press 4 to see the Baseball matches')
print('Press 5 to see the Hockey matches')
print('Press 6 to see the MMA matches')
print()

choice = input('(1/2/3/4/5/6): ')

if choice == '1':
    driver.get(url1)
    time.sleep(3)
    basketballdate = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div/section[1]/div[1]/div/div[2]/h2[2]')
    printbasketballdate = basketballdate.text
    print('DATE: '+printbasketballdate+" (Today's matches)")
    print('')
    basketballmatches = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div/section[1]/div[1]/div/div[2]/div[3]/table')
    printbasketballmatches = basketballmatches.text
    print(printbasketballmatches)

if choice == '2':
    driver.get(url2)
    time.sleep(3)
    soccerschedule = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div/section').text
    print(soccerschedule)
    
if choice == '3':
    driver.get(url3)
    time.sleep(3)
    nflschedule = driver.find_element(By.XPATH, '/html/body/div[5]/section/section/div/section/div/div').text
    print(nflschedule)

if choice == '4':
    driver.get(url4)
    time.sleep(3)
    print("Today's matches / Upcoming matches")
    mlbschedule = driver.find_element(By.XPATH, '//*[@id="sched-container"]').text
    print(mlbschedule)

if choice == '5':
    driver.get(url5)
    time.sleep(3)
    nhlschedule = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/section/div').text
    print(nhlschedule)

if choice == '6':
    driver.get(url6)
    time.sleep(3)
    mmaschedule = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/section/div').text
    print(mmaschedule)

driver.close()


