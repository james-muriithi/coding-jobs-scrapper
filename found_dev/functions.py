# import packages
import bs4
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# get soup object
def get_soup(text):
	return BeautifulSoup(text, "lxml", from_encoding='utf-8')


# extract company
def extract_company(div): 
    
    try:
        lastDiv = div.find_all('div')[-1]
        return (lastDiv.find_all('a')[0].text)
    except:
        return ''


# extract job salary
def extract_salary(div): 
    try:
        lastDiv = div.find_all('div')[-1]
        salaryIcon = lastDiv.find(name="i", attrs={"class", "fas fa-money-bill color-money"})
        return (salaryIcon.find_parent('span').text.strip())
    except:
        return ''
    


# extract job location
def extract_location(div):
    try:
        lastDiv = div.find_all('div')[-1]
        locationIcon = lastDiv.find(name="i", attrs={"class", "fas fa-map-marker color-red"})
        return (locationIcon.find_parent('span').text.strip())
    except:
        return ''


# extract job title
def extract_job_title(div):
    try:
        company = div.find(name="a", attrs={"class", "h-title"})
        return (company.text)
    except:
        return ''


# extract jd summary 
def extract_summary(url): 
    try:
        text = extract_fulltext(url)
        sentences = text.splitlines()
        return ' '.join(sentences[0:2])
    except Exception as e:
        write_logs(str(e))
        return ''
    return ''
 

# extract link of job description 
def extract_link(div): 
    try:
        url = "https://found.dev"
        company = div.find(
            name="a", attrs={"class", "h-title"})
        return (url + company.get('href'))
    except:
        return ''


# extract date of job when it was posted 
def extract_date(div):
    try:
        company = div.find(
            name="div", attrs={"class", "search-result__job-function"}).find(name="div", attrs={"class", "if-wrapper-column align-self--end text--right"})
        if company is None:
            company = div.find(
                name="div", attrs={"class", "search-result__job-function"}).find(name="div", attrs={"class", "top-jobs__content__time"})
        return (company.text+ " ago")
    except:
        return datetime.now().strftime('%Y-%m-%d')


# extract full job description from link
def extract_fulltext(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
        div = soup.find('section', attrs={
                             'id': 'about-job'})
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
