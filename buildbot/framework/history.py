from zope.interface import implements
from twisted.python import log, components
from twisted.internet import defer, reactor
from buildbot.framework import pools, interfaces, process
from buildbot import uthreads

class HistoryManager(pools.PoolMember):
    """
    Parent class for all history managers.  See
    L{buildbot.framework.interfaces.IHistoryManager} for requirements
    for subclasses.
    """
    def __init__(self, name):
        pools.PoolMember.__init__(self, name)