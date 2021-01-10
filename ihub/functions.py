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
        return (div.find('div', attrs={'class', 'item-data'}).find('div', attrs={'class', 'job-company'}).find('a').text)
    except:
        return ''


# extract job salary
def extract_salary(div): 
    return 'Ksh Confidential'
    


# extract job location
def extract_location(div):
    try:
        return (div.find('div', attrs={'class', 'item-data'})
        .find('div', attrs={'class', 'job-company'})
            .find('div', attrs={'class', 'job-location'}).text)
    except:
        return ''


# extract job title
def extract_job_title(div):
    try:
        return (div.find('div', attrs={'class', 'item-data'}).find('h3').find('a').text)
    except:
        return ''


# extract jd summary 
def extract_summary(div): 
    try:
        return (div.find('div', attrs={'class', 'item-data'}).find('div', attrs={'class', 'post-description'})
                .find('a').text)
    except Exception as e:
        write_logs(e.text)
        return ''
    return ''
 

# extract link of job description 
def extract_link(div): 
    myurl = 'https://ihub.co.ke'
    try:
        title = div.find(
            'div', attrs={'class', 'item-data'}).find('h3').find('a')
        return (myurl+title.get('href'))
    except:
        return ''


# extract date of job when it was posted 
def extract_date(div):
    try:
        return (div.find('div', attrs={'class', 'item-data'})
                .find('div', attrs={'class', 'job-links'})
                .find('div', attrs={'class', 'job-time'}).text)
    except:
        return ''

def extract_category(div):
    try:
        return (div.find('div', attrs={'class', 'item-data'})
                .find('div', attrs={'class', 'job-links'})
                .find('div', attrs={'class', 'job-cat'}).text)
    except:
        return ''      


# extract full job description from link
def extract_fulltext(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
        div = soup.find('div', attrs={
            'class': 'job-content'}).find('div', attrs={'class', 'vacancy-description'})
        return '\n'.join(div.stripped_strings)
    except:
        return ''
    return ''


# write logs to file
def write_logs(text):
    # print(text + '\n')
    f = open('log.txt','a')
    f.write(text + '\n')  
    f.close()
