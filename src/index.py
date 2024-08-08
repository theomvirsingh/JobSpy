import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="Game Developer",
    location="India",
    results_wanted=200,
    # hours_old=72, # (only Linkedin/Indeed is hour specific, others round up to days old)
    easy_apply=True,
    description_format="html",
    linkedin_fetch_description=True, # get full description , direct job url , company industry and job level (seniority level) for linkedin (slower)
    proxies=["104.207.45.42:3128","104.167.28.222:3128","104.207.63.29:3128","104.167.30.39:3128","104.207.61.238:3128",
             "104.207.36.33:3128","104.207.40.114:3128","104.207.38.13:3128","104.167.29.102:3128"],
)
print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs1.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel