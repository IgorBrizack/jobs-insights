from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode='r') as files:
        data = list(csv.DictReader(files))
        return data


def get_unique_job_types(path: str) -> List[str]:
    job_list = []
    result_from_read = read(path)
    for jobs in result_from_read:
        if jobs['job_type'] not in job_list:
            job_list.append(jobs['job_type'])
    return job_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
