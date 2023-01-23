from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    industries_list = []
    result_from_read = read(path)
    for industries in result_from_read:
        if industries['industry'] not in industries_list:
            if len(industries['industry']):
                print(industries['industry'])
                industries_list.append(industries['industry'])
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_list_of_industry = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_list_of_industry.append(job)

    return filtered_list_of_industry
