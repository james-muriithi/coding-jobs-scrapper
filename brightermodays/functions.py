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
        return (div.find('div', attrs={'class', 'search-result__job-meta'}).text)
    except:
        return ''


# extract job salary
def extract_salary(div): 
    try:
        return (div.find('div', attrs={'class', 'search-result__job-salary'}).text.strip())
    except:
        return ''
    


# extract job location
def extract_location(div):
    try:
        return (div.find('div', attrs={'class', 'search-result__location'}).text)
    except:
        return ''


# extract job title
def extract_job_title(div):
    try:
        company = div.find(name="h3")
        return (company.text)
    except:
        return ''


# extract jd summary 
def extract_summary(url): 
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
        summary = soup.find('div', attrs={
                             'class': 'job__details__user-edit wrapper--inline-block float--left'})
        summary.h3.decompose()
        return '\n'.join(summary.stripped_strings)
    except Exception as e:
        write_logs(str(e))
        return ''
    return ''
 

# extract link of job description 
def extract_link(div): 
    try:
        company = div.find(
            name="a", attrs={"class", "search-result__job-title"})
        return (company.get('href'))
    except:
        return ''


# extract date of job when it was posted 
def extract_date(div):
    try:
        company = div.find(
            name="div", attrs={"class", "search-result__job-function"}).find(name="div", attrs={"class", "if-wrapper-column align-self--end text--right"})
        if company is None:
            company = name="div", attrs={"class", "search-result__job-function"}).find(name="div", attrs={"class", "top-jobs__content__time"})
        return (company.text+ " ago")
    except:
        return ''


# extract full job description from link
def extract_fulltext(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
        divs = soup.findAll('div', attrs={
                             'class': 'job__details__user-edit wrapper--inline-block float--left'})
        return '\n'.join(divs[1].stripped_strings)
    except:
        return ''
    return ''


# write logs to file
def write_logs(text):
    # print(text + '\n')
    f = open('log.txt','a')
    f.write(text + '\n')  
    f.close()
