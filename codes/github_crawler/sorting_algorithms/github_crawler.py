import urllib2
import time
import sys
import socket

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

# def getlistlinks(page_count, html):
#     flag = html.find('"next_page disabled"')
#     if flag == -1:
#         page_count += 1
#         return start_url + '&p=' + str(page_count) 
#     else:
#         return None

def getlinks(fout, start_url_front, start_page):
    for i in range(1,7):
        target_url = start_url_front + str(start_page * 6 + i)
        try:
            response = urllib2.urlopen(target_url)
            realsock = response.fp._sock.fp._sock
        except urllib2.HTTPError, e:
            if e.code == 429:
                time.sleep(1)
                response = urllib2.urlopen(target_url)
                realsock = response.fp._sock.fp._sock
            else:
                raise
        html = response.read() 
        realsock.close()
        response.close()

        links = getrepolinks(html)
        for link in links:
            fout.write(link + '\n')
    # sys.exit()
        # listlink = getlistlinks(start_url + i, html)
        # while listlink!=None:
        #     try:
        #         request = urllib2.Request(listlink, headers = request_headers)
        #         response = urllib2.urlopen(request)
        #     except urllib2.HTTPError, e:
        #         if e.code == 429:
        #             time.sleep(1)
        #             request = urllib2.Request(listlink, headers = request_headers)
        #             response = urllib2.urlopen(request)
        #             raise
        #     html = response.read()
        #     response.close()
        #     links = getrepolinks(html)
        #     for link in links:
        #         fout.write(link + '\n')
        #     listlink = getlistlinks(start_url + i, html)

def main(start_page):
    keyword = 'sorting+algorithms'
    # global start_url_front
    start_url_front = 'https://github.com/search?l=Python&q=' + keyword + '&type=Repositories&p='
    global request_headers
    request_headers = {
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Accept": "application/vnd.github.v3+json",
            "Referer": "https://github.com",
            "Connection": "close" 
    }
    fout = open('links2.txt','a')
    getlinks(fout, start_url_front, start_page)
    fout.close()
    sys.exit()


if __name__ == "__main__":
    start_page = int(sys.argv[1])
    main(start_page)
