#!/usr/bin/python

import csv
import random
from locust import HttpUser, TaskSet, task, between

class RandomSitemapWalk(TaskSet):
    def on_start(self):
        with open('topURL.csv', newline='') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=' ')
            # store the headers in a separate variable,
            # move the reader object to point on the next row
            headings = next(readCSV)

            self.urls = []
            for row in readCSV:
                self.urls.append(row[0])

    @task
    def load_page(self):
        url = random.choice(self.urls)
        r = self.client.get(url)

    @task(10)
    def load_homepage(self):
        r = self.client.get("/")

class AwesomeUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [RandomSitemapWalk]
    host = "https://www.library.ucla.edu"
