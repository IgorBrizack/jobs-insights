from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    read_list = read("data/jobs.csv")

    sort_by(read_list, "min_salary")
    assert read_list[0]["min_salary"] == '19857'

    sort_by(read_list, "max_salary")
    assert int(read_list[0]["max_salary"]) > int(read_list[1]["max_salary"])

    # sort_by(read_list, "date_posted")
    # assert int(read_list[0]["max_salary"]) > int(read_list[2]["max_salary"])
