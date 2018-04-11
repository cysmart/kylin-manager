#!/usr/bin/env python
# -*- coding: utf-8 -*-


from enum import Enum
import requests
import datetime

KYLIN_API_GET_JOB_LIST = 'http://{host}:{port}/kylin/api/jobs'


class JobStatus(Enum):
    NEW = 0
    PENDING = 1
    RUNNING = 2
    FINISHED = 4
    ERROR = 8
    DISCARDED = 16
    STOPPED = 32


class TimeFilter(Enum):
    LAST_ONE_DAY = 0
    LAST_ONE_WEEK = 1
    LAST_ONE_MONTH = 2
    LAST_ONE_YEAR = 3
    ALL = 4


class Job():
    def __init__(self, name, related_cube, job_status, last_modified, duration):
        self.name = name
        self.related_cube = related_cube
        self.job_status = job_status
        self.last_modified = datetime.datetime.fromtimestamp(last_modified / 1000.0).isoformat(' ')
        self.duration = str(datetime.timedelta(seconds=duration))


def exception_job(host, port, username, password, max_duration, *args, **kwargs):
    payload = {'timeFilter': TimeFilter.LAST_ONE_DAY.value,
               'limit': 1000,
               'status': [JobStatus.NEW.value, JobStatus.PENDING.value, JobStatus.RUNNING.value,
                          JobStatus.ERROR.value, JobStatus.FINISHED.value]}
    get_job_list_url = KYLIN_API_GET_JOB_LIST.format(host=host, port=port)
    r = requests.get(get_job_list_url, auth=(username, password), params=payload)
    r.raise_for_status()

    job_list = r.json()
    exception_job_list = []
    for job in job_list:
        if job['job_status'] == JobStatus.ERROR.name or job['duration'] > max_duration:
            exception_job_list.append(Job(name=job['name'],
                                          related_cube=job['related_cube'],
                                          job_status=job['job_status'],
                                          last_modified=job['last_modified'],
                                          duration=job['duration']).__dict__)
    return exception_job_list
