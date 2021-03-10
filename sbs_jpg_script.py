from selenium import webdriver
import time
import urllib.request

photo_class = 'img.aba_img'  # Change class name here (e.g. <img class='aba_img'>)
url = 'https://xxx.xxx.xxx'  # change url here

# Start chromedriver
option = webdriver.ChromeOptions()
chromedriver = 'chromedriver.exe'
option.add_argument('--headless')
driver = webdriver.Chrome(options=option)
driver.get(url)

print('Waiting for page loading...')
time.sleep(2)
img_list = driver.find_elements_by_css_selector(photo_class)
count = len(img_list)
download_count = 0
print('Found', count, 'matched image.')
print('Start downloading...')

errorimg_list = []
for i, img in enumerate(img_list):
    # print(img.get_attribute("src"))
    try:
        urllib.request.urlretrieve(img.get_attribute("src"), 'resource/' + img.get_attribute("src").split('/')[-1])
        download_count += 1
        print('Download {}/{} successful'.format(i + 1, count))
    except Exception:
        errorimg_list.append(img)
        print('Error: Download {}/{} not successful!'.format(i + 1, count))
print('Total image amount: {} Downloaded: {}'.format(count, download_count))
# print(driver.page_source)
driver.close()
driver.quit()
