from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    max_salary = 0
    salary_list = []
    result_from_read = read(path)

    for salary in result_from_read:
        if len(salary["max_salary"]) > 0 and salary["max_salary"] != "invalid":
            salary_list.append(salary["max_salary"])

    for max_salarys in salary_list:
        if int(max_salarys) > max_salary:
            max_salary = int(max_salarys)

    return int(max_salary)


def get_min_salary(path: str) -> int:
    min_salary = 0
    salary_list = []
    result_from_read = read(path)

    for salary in result_from_read:
        if len(salary["min_salary"]) > 0 and salary["min_salary"] != "invalid":
            salary_list.append(salary["min_salary"])

    min_salary = min(int(salary) for salary in salary_list)

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if not int(job["min_salary"]) and not int(job["max_salary"]):
            raise ValueError
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    result = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except Exception:
            pass
    return result
