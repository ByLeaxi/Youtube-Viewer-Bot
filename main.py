#Codder ByLeaxi =)
import random
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from multiprocessing import Process
#Codder ByLeaxi =)
def show_banner():
    print(r'''
      ____        _                     _ 
     |  _ \      | |                   (_)
     | |_) |_   _| |     ___  __ ___  ___ 
     |  _ <| | | | |    / _ \/ _` \ \/ / |
     | |_) | |_| | |___|  __/ (_| |>  <| |
     |____/ \__, |______\___|\__,_/_/\_\_|
             __/ |                        
            |___/                         

            Youtube View Bot =)
    ''')
    
if __name__ == '__main__':
    show_banner()
    
with open('pr.txt', 'r') as f:
    proxies = f.read().splitlines()
used_proxies = set()

with open('config.json', 'r') as f:
    config = json.load(f)

url = config['url']
num_processes = config['num_processes']
min_wait_time = config['min_wait_time']
max_wait_time = config['max_wait_time']
num_runs = config['num_runs']
os.system(f"title Codder ByLeaxi - Link : {url} - Kaç Adet İzlenecek : {num_runs} ")
def run(proxy, process_num):
    options = Options()
    options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    options.set_preference('network.proxy.type', 1)
    options.set_preference('network.proxy.http', proxy.split(':')[0])
    options.set_preference('network.proxy.http_port', int(proxy.split(':')[1]))
    options.set_preference('network.proxy.ssl', proxy.split(':')[0])
    options.set_preference('network.proxy.ssl_port', int(proxy.split(':')[1]))
    browser = webdriver.Firefox(options=options)

    print(f'İşlem {process_num}: Seçilen Proxy: {proxy}')
    browser.get(url)
    time.sleep(10)
    try:
        consent_button = browser.find_element(By.XPATH, '/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
        consent_button.click()
        time.sleep(5)
        print(f'İşlem {process_num}: Doğrulama Başarıyla Geçildi')
    except NoSuchElementException:
        print(f'İşlem {process_num}: Doğrulama Gelmedi =)')
        pass
        
    time.sleep(5)
    try:
        money_button = browser.find_element(By.CSS_SELECTOR, 'button.ytp-play-button.ytp-button')
        money_button.click()
        wait_time = random.randint(min_wait_time, max_wait_time)
        print(f'İşlem {process_num}: Video {wait_time} saniye Oynatılıyor')
        time.sleep(1)
        play_button = browser.find_element(By.CSS_SELECTOR, 'button.ytp-mute-button.ytp-button')
        play_button.click()
        print(f'İşlem {process_num}: Sessiz Oynatılıyor')
        time.sleep(wait_time)
    except NoSuchElementException:
        pass

    browser.quit()
    print(f'İşlem {process_num}: Tamamlandı. Proxy: {proxy}')

used_proxies = set()

if __name__ == '__main__':
    for run_count in range(num_runs):
        processes = []
        for i in range(num_processes):
            while True:
                proxy = random.choice(proxies)
                if proxy not in used_proxies:
                    used_proxies.add(proxy)
                    break
            process = Process(target=run, args=(proxy, i+1))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()   
