# import packages
import bs4
import requests
from bs4 import BeautifulSoup

# get soup object
def get_soup(text):
	return BeautifulSoup(text, "lxml", from_encoding='utf-8')


# extract company
def extract_company(div): 
    
    try:
        # return (div.find('div', attrs={'class', 'job-list-content'}).find('h4').find('a').text.split(' at ')[1])
        job_title = extract_job_title(div)
        return job_title.split(' at ')[1].strip()
    except:
        return ''


# extract job salary
def extract_salary(div): 
    return 'Ksh Confidential'
    


# extract job location
def extract_location(div):
    try:
        return (div.find('div', attrs={'class', 'job-list-content'})
                .find('div', attrs={'class', 'meta-tag'}).findAll('span')[1].text)
    except:
        return 'Nairobi'


# extract job title
def extract_job_title(div):
    try:
        return (div.find('li', attrs={'class', 'mag-b'}).find('h2').find('a').text)
    except:
        return ''


# extract jd summary 
def extract_summary(div): 
    try:
        return (div.find('li', attrs={'class', 'job-desc'}).text)
    except Exception as e:
        write_logs(str(e))
        return ''
    return ''
 

# extract link of job description 
def extract_link(div): 
    myurl = 'https://www.myjobmag.co.ke/'
    try:
        title = div.find(
            'li', attrs={'class', 'mag-b'}).find('h2').find('a')
        return (myurl+title.get('href'))
    except:
        return ''


# extract date of job when it was posted 
def extract_date(div):
    try:
        return (div.find('li', attrs={'class', 'job-item'}).find('ul')
                .find('li', attrs={'id', 'job-date'}).text)
    except:
        return ''


# extract full job description from link
def extract_fulltext(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
        div = soup.find('div', attrs={
            'class': 'job-details'})
        return '\n'.join(div.stripped_strings)
    except:
        return ''


# write logs to file
def write_logs(text):
    # print(text + '\n')
    f = open('log.txt','a')
    f.write(text + '\n')  
    f.close()
