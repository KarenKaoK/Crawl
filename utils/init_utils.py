"""
# init_utils.py
# Author: Karen
# Date: 2023.07.11
# Description: 
"""
import os
import yaml
from datetime import datetime
from logger import create_logger


def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def creat_dir(path):
    os.makedirs(path) if not os.path.exists(path) else None
    return 
        
def get_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y%m%d_%H%M%S")
    return formatted_datetime

   
def init_config(config_path, save_dir_name):

    # config setting
    config = load_config(config_path)
    output_dir = config['output_dir']
    log_dir = config['log_dir'] 
    article_dir = config['article_dir']
    article_crawl_raw = config['article_crawl_raw']
    article_processed = config['article_processed']
    summary = config['summary']


    print(output_dir)
    print(log_dir)
    print(article_dir)
    print(article_crawl_raw)
    print(article_processed)
    print(summary)

    # creat output dir 
    creat_dir(save_dir_name)
    creat_dir(os.path.join(save_dir_name, output_dir))
    # creat_dir(os.path.join(save_dir_name, log_dir))
    # creat_dir(os.path.join(save_dir_name, article_dir))
    # creat_dir(os.path.join(save_dir_name, article_crawl_raw))
    # creat_dir(os.path.join(save_dir_name, article_processed))
    # creat_dir(os.path.join(save_dir_name, summary))

    

    return config


def init_logger(config, save_dir_name):

    # log_dir = config['log_dir']    

    # init log
    log_file_path = os.path.join(save_dir_name,'log.log')
    logger = create_logger(log_file_path)
    logger.info('finish init setting')

    return logger


    


