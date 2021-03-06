 [![GitHub license](https://img.shields.io/github/license/james-muriithi/coding-jobs-scrapper?style=for-the-badge)](https://github.com/opensource254/corona-api/blob/master/LICENSE)

# Coding Jobs Scraper
scrap coding jobs from various sites
> e.g
- [Brighter Mondays](https://www.brightermonday.co.ke/jobs/software-data)
- [Job Search Ke](https://www.jobsearchke.com/category/ICT/)
- [ihub](https://ihub.co.ke/jobs)

## API Endpoints
- <code>GET</code> [https://developer.coding-jobs.oyaa.co.ke/all-jobs](https://developer.coding-jobs.oyaa.co.ke/all-jobs) ➡️ all jobs (new and old)
    > parameters
    - `limit=2` The number of jobs to return (default is 10)

- <code>GET</code> [https://developer.coding-jobs.oyaa.co.ke/new](https://developer.coding-jobs.oyaa.co.ke/new) ➡️ new jobs
    > parameters
    - `limit=3` The number of jobs to return (default is 10) optional
    - `platform=twitter` new jobs for a certain platform (e.g. twitter, telegram) optional

- <code>POST</code> [https://developer.coding-jobs.oyaa.co.ke/new](https://developer.coding-jobs.oyaa.co.ke/new) ➡️ post a new job
    > Auth required: Yes (OAuth 2.0)
    ```python
    headers = {
        "Authorization": "Bearer [ACCESS_TOKEN_HERE]" 
    }
    ```

    > Data
    ```JSON
    {
        "title":"Data Analyst",
        "location":"Nairobi",
        "company":"Potential Staffing Limited",
        "summary":"A small job description",
        "salary":"KSh 40000",
        "link":"https://www.brightermonday.co.ke/listings/data-analyst-mpjwzz",
        "post_date":"5d ago",
        "full_text" : "full job description"
    }
    ```
[checkout the api repository](https://github.com/james-muriithi/coding-jobs-api)

## How to Run
 

```
$ pip install -r requirements.txt 
$ python main.py
```

## Licence
[MIT](https://github.com/james-muriithi/coding-jobs-scrapper/blob/master/LICENCE)

