import streamlit as st
from selenium.webdriver import Chrome , ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

st.title("Translations and Definitions of the words")
st.header("**Guidelines**")
st.markdown("* **If You want to translate words or sentences click Translation**")
st.markdown("* **If you want to get the defination of words click Definition**")

st.header("Translation or Defination")
choice = st.radio(label = "Make your choice" , options = ["Translation" , "Definition"])


if choice == "Definition" : 
    st.header("Which word's definition would you like to know")
    user_input = st.text_input(label = "Enter your word please.")
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get(url = "https://www.dictionary.com/")
    search_box = WebDriverWait(driver = driver , timeout=10).until(method = EC.element_to_be_clickable(mark = (By.XPATH , '//*[@id="global-search"]')))
    time.sleep(0.5)
    search_box.clear()
    search_box.send_keys(user_input)
    search_box.send_keys(Keys.ENTER)
    
    time.sleep(0.5)
    first_def = driver.find_elements(by = By.CSS_SELECTOR , value = 'span[class = "one-click-content css-nnyc96 e1q3nk1v1"]')
    
    btn_3 = st.button("Submit")
    
    if btn_3 :
        try :
            st.header("The Definitions")
            time.sleep(0.5)
            st.markdown(f"* The First Definition is : **{first_def[0].text}**")
            st.markdown(f"* The Second Definition is : **{first_def[1].text}**")
            st.markdown(f"* The Third Definition is : **{first_def[2].text}**")
        except IndexError : 
            pass
        
elif choice == "Translation" : 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    driver.get(url = "https://translate.google.com/")
    
    st.header("Select languages")
    from_lang_ex = st.selectbox("Translate from" , options = ["English" , "Azerbaijan" , "Russian"])
    to_lang_ex = st.selectbox("Translate to" , options = ["Azerbaijan" , "English" , "Russian"])
    
    user_input_2 = st.text_input(label = "Enter you word or sentence please.")
    
    sign = WebDriverWait(driver=driver , timeout=10).until(method = EC.element_to_be_clickable(mark = (By.CSS_SELECTOR , "div[class = 'VfPpkd-Bz112c-RLmnJb']"))).click()
    from_lang = driver.find_element(by = By.TAG_NAME , value = "input")
    time.sleep(0.5)
    from_lang.clear()
    from_lang.send_keys(from_lang_ex)
    time.sleep(0.5)
    from_lang.send_keys(Keys.ENTER)

    sign_2 = WebDriverWait(driver=driver , timeout=10).until(method = EC.element_to_be_clickable(mark = (By.XPATH  , '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]'))).click()
    to_lang = driver.find_element(by = By.XPATH , value = "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input")
    time.sleep(0.5)
    to_lang.clear()
    to_lang.send_keys(to_lang_ex)
    time.sleep(0.5)
    to_lang.send_keys(Keys.ENTER)
    
    btn_4 = st.button("Submit")
    
    if btn_4 : 
        
        writing = WebDriverWait(driver=driver , timeout=10).until(method = EC.element_to_be_clickable(mark=(By.XPATH , "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")))
        writing.clear()
        writing.send_keys(user_input_2)
        time.sleep(2)
        answer = driver.find_elements(by = By.CSS_SELECTOR , value = "div[class = 'J0lOec']")

        time.sleep(1)
        for x in answer : 
            st.markdown(f"The translation is : **{x.text}**")
