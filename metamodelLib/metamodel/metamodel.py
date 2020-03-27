"""Definition of meta model 'metamodel'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'metamodel'
nsURI = 'http://www.example.org/metamodel'
nsPrefix = 'metamodel'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
DataTypes = EEnum('DataTypes', literals=['float32', 'int32', 'string'])

ROSVersion = EEnum('ROSVersion', literals=['Eloquent'])

AritectureTypes = EEnum('AritectureTypes', literals=['x86', 'x64'])

OSType = EEnum('OSType', literals=['Ubuntu_14', 'Ubuntu_16', 'Ubuntu_18'])


class Client(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    servicePath = EAttribute(eType=EString, derived=False, changeable=True)
    servicemessage = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, servicemessage=None, servicePath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if servicePath is not None:
            self.servicePath = servicePath

        if servicemessage is not None:
            self.servicemessage = servicemessage


class Node(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    hasSubscribers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasPublishers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasClients = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasServers = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasParameters = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasActions = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasSubscribers=None, hasPublishers=None, hasClients=None, hasServers=None, hasParameters=None, name=None, hasActions=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if hasSubscribers:
            self.hasSubscribers.extend(hasSubscribers)

        if hasPublishers:
            self.hasPublishers.extend(hasPublishers)

        if hasClients:
            self.hasClients.extend(hasClients)

        if hasServers:
            self.hasServers.extend(hasServers)

        if hasParameters:
            self.hasParameters.extend(hasParameters)

        if hasActions:
            self.hasActions.extend(hasActions)


class Subscriber(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    topicPath = EAttribute(eType=EString, derived=False, changeable=True)
    smsg = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, smsg=None, topicPath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if topicPath is not None:
            self.topicPath = topicPath

        if smsg is not None:
            self.smsg = smsg


class Publisher(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    topicPath = EAttribute(eType=EString, derived=False, changeable=True)
    publishRate = EAttribute(eType=EFloat, derived=False, changeable=True)
    pmsg = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, pmsg=None, topicPath=None, publishRate=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if topicPath is not None:
            self.topicPath = topicPath

        if publishRate is not None:
            self.publishRate = publishRate

        if pmsg is not None:
            self.pmsg = pmsg


class Server(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    servicePath = EAttribute(eType=EString, derived=False, changeable=True)
    servicemessage = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, name=None, servicemessage=None, servicePath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if servicePath is not None:
            self.servicePath = servicePath

        if servicemessage is not None:
            self.servicemessage = servicemessage


class Parameter(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    type = EAttribute(eType=DataTypes, derived=False, changeable=True)
    value = EAttribute(eType=EString, derived=False, changeable=True, upper=-1)

    def __init__(self, *, name=None, type=None, value=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type

        if value:
            self.value.extend(value)


class Package(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    rosVersion = EAttribute(eType=ROSVersion, derived=False, changeable=True, upper=-1)
    packagePath = EAttribute(eType=EString, derived=False, changeable=True)
    hasDependencies = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasNodes = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasDocumentation = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, hasDependencies=None, hasNodes=None, hasDocumentation=None, name=None, rosVersion=None, packagePath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if rosVersion:
            self.rosVersion.extend(rosVersion)

        if packagePath is not None:
            self.packagePath = packagePath

        if hasDependencies:
            self.hasDependencies.extend(hasDependencies)

        if hasNodes:
            self.hasNodes.extend(hasNodes)

        if hasDocumentation is not None:
            self.hasDocumentation = hasDocumentation


class Dependency(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Documentation(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


class Graph(EObject, metaclass=MetaEClass):

    hasTopics = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasServiceLinks = EReference(ordered=True, unique=True, containment=True, upper=-1)
    nodes = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, hasTopics=None, hasServiceLinks=None, nodes=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasTopics:
            self.hasTopics.extend(hasTopics)

        if hasServiceLinks:
            self.hasServiceLinks.extend(hasServiceLinks)

        if nodes:
            self.nodes.extend(nodes)


class Topic(EObject, metaclass=MetaEClass):

    topicPath = EAttribute(eType=EString, derived=False, changeable=True)
    publisher = EReference(ordered=True, unique=True, containment=False)
    subscriber = EReference(ordered=True, unique=True, containment=False, upper=-1)

    def __init__(self, *, publisher=None, subscriber=None, topicPath=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if topicPath is not None:
            self.topicPath = topicPath

        if publisher is not None:
            self.publisher = publisher

        if subscriber:
            self.subscriber.extend(subscriber)


class ServiceLink(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    server = EReference(ordered=True, unique=True, containment=False)
    client = EReference(ordered=True, unique=True, containment=False)

    def __init__(self, *, server=None, client=None, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if server is not None:
            self.server = server

        if client is not None:
            self.client = client


class ServiceMessage(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    hasRequest = EReference(ordered=True, unique=True, containment=True)
    hasResponse = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, name=None, hasRequest=None, hasResponse=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if hasRequest is not None:
            self.hasRequest = hasRequest

        if hasResponse is not None:
            self.hasResponse = hasResponse


class Request(EObject, metaclass=MetaEClass):

    hasCommunicationObjects = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasCommunicationObjects=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasCommunicationObjects:
            self.hasCommunicationObjects.extend(hasCommunicationObjects)


class Response(EObject, metaclass=MetaEClass):

    hasCommunicationObjects = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasCommunicationObjects=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasCommunicationObjects:
            self.hasCommunicationObjects.extend(hasCommunicationObjects)


class TopicMessage(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    hasCommunicationObjects = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, name=None, hasCommunicationObjects=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if hasCommunicationObjects:
            self.hasCommunicationObjects.extend(hasCommunicationObjects)


class ROSSystem(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    topology = EReference(ordered=True, unique=True, containment=True)
    hasPackages = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasGraphs = EReference(ordered=True, unique=True, containment=True)
    hasTopicMessages = EReference(ordered=True, unique=True, containment=True, upper=-1)
    hasServiceMessages = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, topology=None, hasPackages=None, hasGraphs=None, name=None, hasTopicMessages=None, hasServiceMessages=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if topology is not None:
            self.topology = topology

        if hasPackages:
            self.hasPackages.extend(hasPackages)

        if hasGraphs is not None:
            self.hasGraphs = hasGraphs

        if hasTopicMessages:
            self.hasTopicMessages.extend(hasTopicMessages)

        if hasServiceMessages:
            self.hasServiceMessages.extend(hasServiceMessages)


class Topology(EObject, metaclass=MetaEClass):

    hasPlatforms = EReference(ordered=True, unique=True, containment=True, upper=-1)
    network = EReference(ordered=True, unique=True, containment=True)

    def __init__(self, *, hasPlatforms=None, network=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasPlatforms:
            self.hasPlatforms.extend(hasPlatforms)

        if network is not None:
            self.network = network


class Platform(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    hasHost = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, hasHost=None, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if hasHost:
            self.hasHost.extend(hasHost)


class LocalNetwork(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    ip = EAttribute(eType=EString, derived=False, changeable=True)
    subnetMask = EAttribute(eType=EString, derived=False, changeable=True)
    gateway = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, ip=None, subnetMask=None, gateway=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if ip is not None:
            self.ip = ip

        if subnetMask is not None:
            self.subnetMask = subnetMask

        if gateway is not None:
            self.gateway = gateway


class Host(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    architecture = EAttribute(eType=AritectureTypes, derived=False, changeable=True)
    OS = EAttribute(eType=OSType, derived=False, changeable=True)
    hardDisk = EAttribute(eType=EFloat, derived=False, changeable=True)
    memory = EAttribute(eType=EFloat, derived=False, changeable=True)
    rosVersion = EAttribute(eType=ROSVersion, derived=False, changeable=True)
    hasNetworkInterfaces = EReference(ordered=True, unique=True, containment=True, upper=-1)

    def __init__(self, *, name=None, architecture=None, OS=None, hardDisk=None, memory=None, rosVersion=None, hasNetworkInterfaces=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if architecture is not None:
            self.architecture = architecture

        if OS is not None:
            self.OS = OS

        if hardDisk is not None:
            self.hardDisk = hardDisk

        if memory is not None:
            self.memory = memory

        if rosVersion is not None:
            self.rosVersion = rosVersion

        if hasNetworkInterfaces:
            self.hasNetworkInterfaces.extend(hasNetworkInterfaces)


@abstract
class Action(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class NetworkInterface(EObject, metaclass=MetaEClass):

    gateway = EAttribute(eType=EString, derived=False, changeable=True)
    subnetMask = EAttribute(eType=EString, derived=False, changeable=True)
    name = EAttribute(eType=EString, derived=False, changeable=True)
    ip = EAttribute(eType=EString, derived=False, changeable=True)

    def __init__(self, *, gateway=None, subnetMask=None, name=None, ip=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if gateway is not None:
            self.gateway = gateway

        if subnetMask is not None:
            self.subnetMask = subnetMask

        if name is not None:
            self.name = name

        if ip is not None:
            self.ip = ip


class CommunicationObject(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, derived=False, changeable=True)
    type = EAttribute(eType=DataTypes, derived=False, changeable=True)

    def __init__(self, *, name=None, type=None, **kwargs):
        if kwargs:
            raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if type is not None:
            self.type = type


class ActionServer(Action):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ActionClient(Action):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)