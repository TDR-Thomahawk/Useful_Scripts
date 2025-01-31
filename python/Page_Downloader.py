import urllib.request

for i in range(33,34):
    url = "http://www.dspguide.com/CH{}.PDF".format(i+1)
    print("Getting", url)
    try:
        urllib.request.urlretrieve(url, filename="CH{}.pdf".format(i+1))
    except (Exception, e):
        logging.warn("error downloading %s: %s" % (url, e))
