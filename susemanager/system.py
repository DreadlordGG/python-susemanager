import xmlrpclib
class list:
	def __init__(self, client, session):
	    self.session = session
	    self.client = client

	def ActivationKeys(self, pid):
	    return self.client.system.listActivationKeys(self.session, sid)

	@property
	def ActiveSystems(self):
	    return self.client.system.listActiveSystems(self.session)

	def ActiveSystemsDetails(self, *args):
	    return self.client.system.listActiveSystemsDetails(self.session, args)
	@property
	def Systems(self):
	    return self.client.system.listSystems(self.session)

	def SystemsWithPackage(self, pid):
	    return self.client.system.listSystemsWithPackage(self.session, pid)
