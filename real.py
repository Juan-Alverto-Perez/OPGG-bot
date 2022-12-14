from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)


#go to website and prints the title
driver.get('https://www.op.gg/')
print(driver.title)

#searches and goes to my profile
driver.find_element(by=By.ID, value = "searchHome").send_keys("Pobelter" + Keys.ENTER)




#waits for live game to load then clicks it
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Live Game")))
driver.find_element(By.PARTIAL_LINK_TEXT,"Live Game").click()



WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "queue-type")))
print(driver.title)

playerNames = driver.find_elements(By.CLASS_NAME,'summoner-name')
playerRank = driver.find_elements(By.CLASS_NAME,'current-rank')
playerWr = driver.find_elements(By.CLASS_NAME,'winratio')
playerNames.pop(0)
# for name in playerNames[1:]:
#     print(name.text)

# for rank in playerRank:
#     print(rank.text)
# for wr in playerWr:
#         print(wr.text)
print('Name:    -   Rank:   -   WR%\n')
for x in range(10):
   
    print(f'{playerNames[x].text}           {playerRank[x].text}    ')

  
