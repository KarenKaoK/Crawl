
import os
# from init_utils import init_config, init_logger, get_datetime
from utils.init_utils import init_config, init_logger,get_datetime
from crawler.base_crawler import BaseCrawler
from crawler.ettoday_crawler import EttodayCrawler,run_crawler
from utils.utils import limit_articles

logger = None

def main(config_path,output_path):

    global logger

    # init
    save_dir_name = os.path.join(output_path,get_datetime())
    print('save_dir_name:', save_dir_name)
    config = init_config(config_path, save_dir_name)
    logger = init_logger(config, save_dir_name)
    
    topic_url = 'https://www.ettoday.net/news/news-list-2023-07-10-21.htm'
    root_url = 'https://www.ettoday.net'

    ettoday_crawler = EttodayCrawler(root_url, topic_url)

  
    df = ettoday_crawler.crawl_title_category_link(topic_url,root_url)
    df = limit_articles(df)
    # print(df)
    
    df = run_crawler(root_url,topic_url)
    csv_path_name = os.path.join(save_dir_name,'output.csv')
    df.to_csv(csv_path_name, index=False, encoding="utf-8-sig")

    logger.info('finish crawling')
    return 



if __name__ == "__main__":
    output_path = './output'
    config_path = './config.yaml'
    # main(config_path)

    main(config_path,output_path)