#!/usr/bin/env python
import xmlrpclib
import sys

class auth:

    def __init__(self, url, username, password):
        self.selfurl = url
        self.username = username
        self.password = password
        self.client = xmlrpclib.Server(url)

    @property
    def login(self):
        try:
            self.session = self.client.auth.login(self.username, self.password)
            print ("Successfully connected to SuSE Manager")
            print self.client, self.session
        except (xmlrpclib.ProtocolError, xmlrpclib.Fault) as error:
            print ("Unable to login to SUSE Manager server: %s" % str(error))
            sys.exit(1)
        return self.client, self.session

    @property
    def logout(self):
        try:
            self.client.auth.logout(self.session)
            print ("Login Successfull")
        except (xmlrpclib.ProtocolError, xmlrpclib.Fault) as error:
            print ("Unable to logout to SUSE Manager server:: %s" % str(error))

class system:
    def __init__(self, client, session):
        self.session = session
        self.client = client

    def listActivationKeys(self, pid):
        return self.client.system.listActivationKeys(self.session, sid)

    @property
    def listActiveSystems(self):
        return self.client.system.listActiveSystems(self.session)

    def listActiveSystemsDetails(self, *args):
        return self.client.system.listActiveSystemsDetails(self.session, args)
    @property
    def listSystems(self):
        return self.client.system.listSystems(self.session)

    def listSystemsWithPackage(self, pid):
        return self.client.system.listSystemsWithPackage(self.session, pid)

if __name__ == "__main__":
        pass


