import urllib2
import time

def getrepolinks(html):
    prefix = 'https://github.com'
    flag = html.find('repo-list-name')
    links = []
    while flag!=-1:
        flag_href = html.find('href="', flag)
        flag_href_end = html.find('">', flag_href)
        link = prefix + html[flag_href + 6 : flag_href_end]
        print link
        links.append(link)
        flag = html.find('repo-list-name', flag_href_end)
    return links

def getlistlinks(page_count, html):
    flag = html.find('"next_page disabled"')
    if flag == -1:
        page_count += 1
        return start_url + '&p=' + str(page_count) 
    else:
        return None

def getlinks(fout, start_url):
    page_count = 1
    try:
        response = urllib2.urlopen(start_url)
    except urllib2.HTTPError, e:
        if e.code == 429:
            time.sleep(10)
            response = urllib2.urlopen(start_url)
        raise
    html = response.read() 
    response.close()
    links = getrepolinks(html)
    for link in links:
        fout.write(link + '\n')
    listlink = getlistlinks(page_count, html)
    while listlink!=None:
        page_count += 1
        try:
            request = urllib2.Request(listlink, headers = request_headers)
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            if e.code == 429:
                time.sleep(100)
                request = urllib2.Request(listlink, headers = request_headers)
                response = urllib2.urlopen(request)
                raise
        html = response.read()
        response.close()
        links = getrepolinks(html)
        for link in links:
            fout.write(link + '\n')
        listlink = getlistlinks(page_count, html)

def main():
    keyword = 'sorting'
    global start_url
    start_url = 'https://github.com/search?l=Python&q=' + keyword + '&ref=searchresults&type=Repositories'
    global request_headers
    request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "http://thewebsite.com",
            "Connection": "keep-alive" 
    }
    fout = open('links.txt','w')
    getlinks(fout, start_url)
    fout.close


if __name__ == "__main__":
    main()
