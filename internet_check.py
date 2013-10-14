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

    theurl = 'http://192.168.1.1'
    username = 'admin'
    password = 'admin'

    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, theurl, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    pagehandle = urllib2.urlopen(theurl+"/status/status_deviceinfo.htm")

    return pagehandle.read()

def getModemStatus(page):
    """
        This function analises status pages and looks for string that
        says it is connected to line
        
        Input:
        Nothing
        
        Returns:
        True/False
    """

    stan_lini_idx = page.find("Stan linii")

    if page[stan_lini_idx: stan_lini_idx + 200].find("Showtime") != -1:
        return True
    else:
        return False

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

        try: modem_status = getModemStatus(getModemPage())
        except BaseException as error: info = "ERROR: " + str(error)
        else:
            if modem_status:
                info = "INTERNET"
            else:
                info = "NOP"

        with open(os.path.join(logs,now.strftime("%Y-%m-%d.txt")),"a") as fp:
            fp.write(str(now) + " - " + info + "\n")

        print str(now) + " - " + info

        time.sleep(60)    
        
if __name__ == "__main__":
    import os
    root = os.path.dirname(os.path.abspath(__file__))
    startup(root)
    internet_check(root)
    
    

    
