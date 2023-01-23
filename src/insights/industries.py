from src.insights.jobs import read
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    industries_list = []
    result_from_read = read(path)
    for industries in result_from_read:
        if industries['industry'] not in industries_list and :
            if len(industries['industry']):
                print(industries['industry'])
                industries_list.append(industries['industry'])
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
