"""
# crawler.py
# Author: Karen
# Date: 2023.07.11

"""
import os
import random
import requests
import pandas as pd
from tqdm import tqdm 
from datetime import datetime
from bs4 import BeautifulSoup


class BaseCrawler:
    def __init__(self, root_url, topic_url):
        self.root_url = root_url
        self.topic_url = topic_url

    def send_http_request(self, url):
        response = requests.get(url)
        return response

    def parse_html(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def limit_20_links(self, link_list):
        if len(link_list) > 20:
            link_list = link_list[:20]
        else:
            pass    
        return link_list
    
    def create_folder(self):
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        folder_path = os.path.join('./crawler_output', current_time)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    def save_data(self, folder_path, title, content):

        # check title and data is str
        if not isinstance(title, str):
            title = str(title)
        if not isinstance(content, str):
            content = str(content)
        
        # valid title when it as filename
        filename = "".join(c for c in title if c.isalnum() or c.isspace()).rstrip()
        file_path = os.path.join(folder_path, f"{filename}.txt")

        # save  
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return file_path


def run_crawler(config, logger):

    # init crawler
    
    # create output dir by config
    config['crawler']
    names = [item['name'] for item in config['crawler']]

