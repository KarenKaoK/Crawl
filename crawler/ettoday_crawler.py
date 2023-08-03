"""
# ettoday_crawler.py
# Author: Karen
# Date: 2023.07.12

"""

import os
import pandas as pd
from tqdm import tqdm 
from datetime import datetime
from bs4 import BeautifulSoup
from utils.utils import limit_articles
from crawler.base_crawler import BaseCrawler




class EttodayCrawler(BaseCrawler):

   

    def crawl_title_category_link(self, topic_url, root_url):

        response = super().send_http_request(topic_url)
        soup = self.parse_html(response.text, 'lxml')
        elem = soup.select(".part_list_2")
        
        # crawler specific tag
        elem = soup.select(".part_list_2")
        title_list, date_list, cate_list, link_list = [], [], [], []
        for e in elem:
            title_list = [title.text for title in e.select("a")]
            link_list = [os.path.join(root_url, i.get('href').lstrip('/')) for i in e.select("a")]
            date_list = [date.text for date in e.select(".date")]
            cate_list = [cate.text for cate in e.select("em")]

        df = pd.DataFrame()
        df["title"], df["category"], df["date"], df["link"] = title_list, cate_list, date_list, link_list
        

        return df
    
    def crawl_content(self, df):

        contents = []
        links = df['link']

        for link in tqdm(links):

            response = super().send_http_request(link)
            soup = super().parse_html(response.text, 'html.parser')
            div_story = soup.find('div', class_='story')
            paragraphs = div_story.find_all('p')

            contents.append(paragraphs)
            
        df["content"] = contents
        return df
    


def run_crawler(topic_url, root_url):
    ettoday_crawler = EttodayCrawler(root_url, topic_url)
    df = ettoday_crawler.crawl_title_category_link(root_url,topic_url)
    df = ettoday_crawler.crawl_content(df)
    df.to_csv('./output.csv', index=False, encoding="utf-8-sig")


    return df

# if __name__ == "__main__":
      
#     topic_url = 'https://www.ettoday.net/news/news-list-2023-07-10-21.htm'
#     root_url = 'https://www.ettoday.net'

#     c = EttodayCrawler(root_url, topic_url)
  
#     df = c.crawl_title_category_link(topic_url,root_url)

#     print(df)
    