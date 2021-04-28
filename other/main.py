import csv
import re

def write_to_file(write_info, file_name):# can use list as input for write_info
    file = open(file_name, 'w')
    writer = csv.writer(file)
    writer.writerows(write_info)

def read_from_file(file_name):# returns list of rows
    file_content = []
    file = open(file_name, 'r')
    reader = csv.reader(file)
    for row in reader:
        file_content.append(row)
    return file_content

def extract_hashtag(tweet): # returns list of hashtags
    hashtags = re.findall(r'(^|\s)(#[a-z\d_]+)', tweet)
    return hashtags