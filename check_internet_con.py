import urllib.request

if __name__=='__main__':
    try:
        urllib.request.urlopen("http://baidu.com", timeout=2)
        print ("working connection")

    except urllib.error.URLError:
        print ("No internet connection")
