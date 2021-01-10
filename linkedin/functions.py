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
        return (div.find('div', attrs={'class', 'job-result-card__contents'}).find('h4').text)
    except:
        return ''


# extract job salary
def extract_salary(div):
    return 'Ksh Confidential'


# extract job location
def extract_location(div):
    try:
        return (div.find('div', attrs={'class', 'job-result-card__contents'})
                .find('div', attrs={'class', 'job-result-card__meta'}).find('span').text)
    except:
        return ''


# extract job title
def extract_job_title(div):
    try:
        return (div.find('div', attrs={'class', 'job-result-card__contents'}).find('h3').text)
    except:
        return ''


# extract jd summary
def extract_summary(link):
    try:
        text = extract_fulltext(link)
        sentences = text.splitlines()
        print(' '.join(sentences[0:2]))
        print('*'*10 + '\n\n')
        return ' '.join(sentences[0:2])
    except Exception as e:
        write_logs(str(e))
        return ''
    return ''


# extract link of job description
def extract_link(div):
    myurl = 'https://linkedin.com/jobs/view/'
    try:
        job_id = div.attrs['data-id']
        return (myurl+job_id)
    except:
        return ''


# extract date of job when it was posted
def extract_date(div):
    try:
        return (div.find('div', attrs={'class', 'job-result-card__contents'})
                .find('div', attrs={'class', 'job-result-card__meta'}).find('time').attrs['datetime'])
    except:
        return ''


# extract full job description from link
def extract_fulltext(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml", from_encoding='utf-8')
        div = soup.find('section', attrs={
            'class': 'show-more-less-html'}).find('div', attrs={
                'class': 'show-more-less-html__markup'})
        return '\n'.join(div.stripped_strings)
    except Exception as e:
        write_logs(str(e))
        return ''
    return ''


# write logs to file
def write_logs(text):
    # print(text + '\n')
    f = open('log.txt', 'a')
    f.write(text + '\n')
    f.close()
