#################################
# Author: Ankit Murdia
# Created: 2017-12-14
# Updated: 
# Version: 1.0.0
# Description: Helper to manage connections and provide tools to fetch data from RETS servers
#################################

class RETSConnector:
    def __init__(self, cred,account_flag=''):
        self.url = str(cred.get('url', ''))
        self.user =str(cred.get('user'+account_flag, cred.get('user', '')))
        self.passwd =str(cred.get('passwd'+account_flag, cred.get('passwd', '')))
        self.user_agent = str(cred.get('userAgent'+account_flag, cred.get('userAgent', '')))
        self.userAgentPasswd = str(cred.get('userAgentPasswd'+account_flag, cred.get('userAgentPasswd','')))
        self.rets_version = str(cred.get('rets_version', ''))
        

    def _getSession(self):
        self._session = librets.RetsSession(self.url)
        self._session.SetRetsVersion(CONFIG['mls_versions'][self.rets_version])
        self._session.SetUserAgent(self.user_agent)
        self._session.SetUserAgentPassword(self.userAgentPasswd)

        self.login()

        self._session.SetDefaultEncoding(librets.RETS_XML_UTF8_ENCODING)
        return self._session

    def login(self):
        if not self._session.Login(self.user, self.passwd):
            raise Exception('Invalid RETS login')