from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import UnexpectedAlertPresentException
from bs4 import BeautifulSoup
import pyautogui
import pandas as pd
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://etender.cpwd.gov.in")

# Try to close the alert if it appears
try:
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.dismiss()  # or alert.accept()
    print("Alert dismissed.")

except:
    print("No alert.")
    True #while true if the alert box not works  at a time
    


    


while True:

    driver.find_element(By.PARTIAL_LINK_TEXT, "All").click()
    print("Clicked 'All'")
    dropdown = Select(driver.find_element(By.NAME, "awardedDataTable_length"))
    dropdown.select_by_value("20") 
    print("clicked show 20")
    

    # Wait for you to manually focus the Chrome window
    time.sleep(5)

    # Simulate Ctrl + S
    pyautogui.hotkey('ctrl', 's')

    # Wait for the save dialog to appear
    time.sleep(2)

    # Enter file name (optional)
    pyautogui.write('web.html')

    # Press Enter to save
    pyautogui.press('enter')






    time.sleep(2)
    print("web downloaded")

    with open('web.html', 'r', encoding='utf-8') as f:
      print("file opened")
      soup = BeautifulSoup(f, 'html.parser')
    table = soup.find('table', {'id': 'awardedDataTable'})
    rows = table.find('tbody').find_all('tr')
    print("rows found")
    data = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 8:
            nit_no = cols[1].get_text(strip=True)
            name_of_work = cols[2].get_text(" ", strip=True)
            estimated_cost = cols[4].get_text(strip=True).replace('₹', '').strip()
            emd_amount = cols[5].get_text(strip=True).replace('₹', '').strip()
            bid_close = cols[6].get_text(strip=True)
            bid_open = cols[7].get_text(strip=True)
            data.append({
                
                'NIT/RFP NO': nit_no,
                'Name of Work / Subwork / Packages': name_of_work,
                'Estimated Cost': estimated_cost,
                'EMD Amount': emd_amount,
                'Bid Submission Closing Date & Time': bid_close,
                'Bid Opening Date & Time': bid_open
             })
            
            print("saving data")
        
    time.sleep(3)      
    df = pd.DataFrame(data)
    df.to_csv('tenders.csv', index=False)
    print("Data saved to tenders.csv")
    
    driver.quit()

 