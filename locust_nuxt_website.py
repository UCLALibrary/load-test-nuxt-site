#!/usr/bin/python

import random

from locust import HttpUser, TaskSet, task
from pyquery import PyQuery

class RandomSitemapWalk(TaskSet):
    def on_start(self):
        r = self.client.get("/sitemap.xml")
        pq = PyQuery(r.content, parser='html')
        self.sitemap_links = []
        for loc in pq.find('loc'):
            self.sitemap_links.append(PyQuery(loc).text())

    @task
    def load_page(self):
        url = random.choice(self.sitemap_links)
        r = self.client.get(url)

class AwesomeUser(HttpUser):
    tasks = [RandomSitemapWalk]
    host = "https://uclalibrary.netlify.app/"
    
    min_wait = 1  * 1000
    max_wait = 10 * 1000
