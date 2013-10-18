################################################################################
########################## Modem Analyzer ######################################
################################################################################
def getModemPage():
    """
        This function connects to modem internal web pages and
        gets status information

        Input:
        Nothing

        Returns:
        Pages string
    """
    import urllib2
    import config

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None,config.MODEM_URL_ADDRESS,config.MODEM_USERNAME,config.MODEM_PASSWORD)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    pagehandle = urllib2.urlopen(config.MODEM_URL_STATUS_ADDRESS)

    return pagehandle.readlines()

def analizeModemStatus(page):
    """
        This function analises status pages and looks for string that
        says it is connected to line

        Input:
        Nothing

        Returns:
        True/False
    """
    import re
    import config

    regexp = re.compile(config.MODEM_REGEXP_INTERNET_ACTIVE)

    for line in page:
        if regexp.match(line): return True
    else:
        return False

################################################################################
################################ Web check #####################################
################################################################################
def webCheck():
    """
        This function opens web page to check if internet is working

        Input:
        Nothing

        Returns:
        True/False
    """
    import urllib2
    import config
    import random

    urls = config.WEBCHECK_PAGE_LIST[:]
    for idx in range(3):
        url = random.choice(urls)

        try: page = urllib2.urlopen(url)
        except BaseException:
            urls.remove(url)
        else: return True

    else: return False

################################################################################
############################## Startup #########################################
################################################################################
def startup(root):
    """
        This function performs some start up actions
            - Prepares pid

        Input:
        root    - Root path

        Returns:
        Nothing
    """
    import os

    pid = os.path.join(root,"pid")
    with open(pid,"w") as fp:
        fp.write(str(os.getpid()))

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

    if not os.path.exists(logs): os.mkdir(logs)

    while True:
        now = datetime.datetime.now()

        try: modem_internet_status = analizeModemStatus(getModemPage())
        except BaseException as error: info = "ERROR: " + str(error)
        else:
            if modem_internet_status: info = "MODEM CHECK OK"
            else: info = "MODEM CHECK NOT OK"

            if webCheck(): info += " - WEB CHECK OK"
            else: info += " - WEB CHECK NOT OK"

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
    startup(root)
    internet_check(root)
