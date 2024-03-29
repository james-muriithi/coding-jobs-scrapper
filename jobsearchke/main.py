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
file_name = os.path.join(folder, 'jobsearchke-' +
                         datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'.csv')

# dataframe
df = pd.DataFrame(columns=['title', 'location',
                           'company', 'summary', 'salary', 'link', 'post_date', 'full_text', 'fetch_date'])


def scrap_jobs(domain):
    print('scrapping jobs from '+domain + '....')

    # get dom
    page = requests.get(domain)

    #ensuring at least 1 second between page grabs
    time.sleep(1)

    #fetch data
    soup = get_soup(page.text)
    divs = soup.find_all(name="div", attrs={"class": "job-list"})

    # jobsearchke limit
    limit = 25

    # for all jobs on a page
    for index, div in enumerate(divs):
        if index >= limit:
            break
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
        job_post.append(extract_summary(div))

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
        
    # saveCSV()

def saveCSV():
    #saving df as a local csv file
    if not os.path.isdir(folder):
        os.makedirs(folder)

    df.to_csv(file_name, encoding='utf-8')

def postJob(data):
    token = os.environ['ACCESS_TOKEN']
    endpoint = os.environ['API_ENDPOINT']

    try:
        x = requests.post(endpoint, headers={
                          'Authorization': 'Bearer {}'.format(token)}, json=data)
        print(x.json())
    except Exception as error:
        print(error)
        pass


def main():
    page1 = 'https://jobsearchke.com/category/software-engineering/'
    scrap_jobs(page1)


if __name__ == "__main__":
    main()
