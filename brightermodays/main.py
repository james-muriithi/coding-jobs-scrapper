# import packages
import requests
import pandas as pd
import time
from .functions import *
from datetime import datetime
import os
import json

# give the filename the name of the current folder
folder = os.path.join(os.getcwd(), 'jobs')
file_name = os.path.join(folder, 'brightermondays-' +
                         datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.csv')

domain = 'https://www.brightermonday.co.ke/jobs/it-software'

# dataframe
df = pd.DataFrame(columns=['title', 'location',
                           'company', 'summary', 'salary', 'link', 'post_date', 'full_text', 'fetch_date'])


def scrap_jobs():
    print('scrapping jobs from '+domain + '....')

    # get dom
    page = requests.get(domain)

    #ensuring at least 1 second between page grabs
    time.sleep(1)

    #fetch data
    soup = get_soup(page.text)
    divs = soup.find_all(name="article", attrs={"class": "search-result"})

    # for all jobs on a page
    for div in divs:
        #specifying row num for index of job posting in dataframe
        num = (len(df) + 1)
        link = extract_link(div)

        #job data after parsing
        job_post = []

        #grabbing job title
        job_post.append(extract_job_title(div))

        #grabbing location name
        job_post.append(extract_location(div))

        #grabbing company
        job_post.append(extract_company(div))

        #grabbing summary text
        job_post.append(extract_summary(link))

        #grabbing salary
        job_post.append(extract_salary(div))

        #grabbing link
        job_post.append(link)

        #grabbing date
        job_post.append(extract_date(div))

        #grabbing full_text
        job_post.append(extract_fulltext(link))

        # current time
        job_post.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        #appending list of job post info to dataframe at index num
        df.loc[num] = job_post

        postJob(df.loc[num].to_dict())
        
    saveCSV()

def saveCSV():
    #saving df as a local csv file
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df.to_csv(file_name, encoding='utf-8')

def postJob(data):
    endpoint = 'http://localhost/coding-jobs/public/new'

    x = requests.post(endpoint, json=data)
    print(x.json())


def main():
    scrap_jobs()


if __name__ == "__main__":
    main()
