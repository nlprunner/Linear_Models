__author__ = 'jerry'

import sys,urllib
import time
def get_title(page):
    title_pos = page.find("article-header")
    title = page[title_pos + 43 + len(url):]
    return title[:title.find("</h1>")]

def get_content(page):
    content_pos = page.find("article-content")
    content = page[content_pos:]
    content = content[content.find("<p>"):]
    return content[:content.find("</section>")]

def get_topics(page):
    topic_pos = page.find("article-topics")
    topic = page[topic_pos + 25:]
    topics = []
    for item in  topic[:topic.find("</footer>")].split(","):
        topics.append(item[item.find(">") + 1:item.find("</a>")])
    return topics

def get_labels(page):
    label_pos = page.find("data-labels")
    label = page[label_pos + 14:]
    label = label[:label.find("]")]
    return label

in_file = open("/home/jerry/Downloads/AML/OnlineNewsPopularity/OnlineNewsPopularity.csv")
lines = in_file.readlines()
i = 1
for line in lines[1:]:
    terms = line.strip().split(", ")
    url = terms[0]
    time.sleep(0.5)
    wp = urllib.urlopen(url)
    #print "start download..."
    page = wp.read()
    #print get_title(page)
    out_file = open("/home/jerry/Downloads/AML/OnlineNewsPopularity/html/" + str(i) + ".txt", 'wb')
    out_file.write(page)
    out_file.close()
    #print url + "\t" + "\t".join(get_topics(page))
    #print get_labels(page)
    #print get_content(page)
    i += 1
in_file.close()