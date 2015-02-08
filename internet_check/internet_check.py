WEBCHECK_PAGE_LIST = ['http://google.com',
                      'http://www.python.org',
                      'http://github.com',
                      'http://www.amazon.com',
                      'http://www.nasa.gov',
                      'http://lhcathome.web.cern.ch']

def webCheck():
    """
        This function opens web page to check if internet is working

        Input:
        Nothing

        Returns:
        True/False
    """
    import urllib2
    import random

    urls = WEBCHECK_PAGE_LIST[:]
    for idx in range(3):
        url = random.choice(urls)

        try:
            page = urllib2.urlopen(url)
        except Exception:
            urls.remove(url)
        else:
            return True

    else: return False

def internet_check(root):
    """
        This function performs internet check
        Blocking function

        Input:
        root        - Path to root folder

        Returns:
        Nothing
    """
    import time
    import datetime
    import os

    logs = os.path.join(root,"logs")

    if not os.path.exists(logs):
        os.mkdir(logs)

    while True:
        now = datetime.datetime.now()

        if webCheck():
            info = "WEB CHECK OK"
        else:
            info = "WEB CHECK NOT OK"

        with open(os.path.join(logs,now.strftime("%Y-%m-%d.txt")),"a") as fp:
            fp.write(str(now) + " - " + info + "\n")

        print str(now) + " - " + info

        time.sleep(60)

################################################################################
################################ Main ##########################################
################################################################################
if __name__ == "__main__":
    import os
    root = os.path.dirname(os.path.abspath(__file__))
    internet_check(root)
