#
# PySNMP MIB module CISCO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file://./CISCO-SMI.mib
# Produced by pysmi-1.1.10 at Tue Nov 28 11:02:57 2023
# On host simtve-ThinkPad-X1-Carbon-Gen-9 platform Linux version 5.15.0-84-generic by user simon
# Using Python version 3.9.18 (main, Aug 25 2023, 13:20:04) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Unsigned32, iso, ObjectIdentity, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Counter32, Gauge32, enterprises, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Unsigned32", "iso", "ObjectIdentity", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Counter32", "Gauge32", "enterprises", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2016-01-15 00:00', '2012-08-29 00:00', '2009-02-03 00:00', '2002-03-21 00:00', '2001-05-22 00:00', '2000-11-01 22:46', '2000-01-11 00:00', '1997-04-09 00:00', '1995-05-16 00:00', '1994-04-26 20:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cisco.setRevisionsDescriptions(('Added ciscoLDAP under cisco', 'Added ciscoSMB under otherEnterprises', 'Added ciscoSB under otherEnterprises', 'Added ciscoPKI for PKI policy and extension OIDs', 'Added transport protocol domains.', 'Added ciscoDomains to define new transports. Also added ciscoCpeCIB, which will contain managed objects that contribute to the CPE Configuration Information Base (CIB).', 'Added ciscoPolicy, ciscoPolicyAuto, ciscoPIB, and ciscoPibToMib.', 'Added ciscoPartnerProducts to generate sysObjectID for partner platforms', 'New oid assignments for Cisco REPEATER MIB and others.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cisco.setLastUpdated('201601150000Z')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cisco.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: cisco.setDescription('The Structure of Management Information for the Cisco enterprise.')
ciscoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 1))
if mibBuilder.loadTexts: ciscoProducts.setStatus('current')
if mibBuilder.loadTexts: ciscoProducts.setDescription('ciscoProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in CISCO-PRODUCTS-MIB.')
local = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 2))
if mibBuilder.loadTexts: local.setStatus('current')
if mibBuilder.loadTexts: local.setDescription('Subtree beneath which pre-10.2 MIBS were built.')
temporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 3))
if mibBuilder.loadTexts: temporary.setStatus('current')
if mibBuilder.loadTexts: temporary.setDescription('Subtree beneath which pre-10.2 experiments were placed.')
pakmon = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 4))
if mibBuilder.loadTexts: pakmon.setStatus('current')
if mibBuilder.loadTexts: pakmon.setDescription('reserved for pakmon')
workgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 5))
if mibBuilder.loadTexts: workgroup.setStatus('current')
if mibBuilder.loadTexts: workgroup.setDescription('subtree reserved for use by the Workgroup Business Unit')
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6))
if mibBuilder.loadTexts: otherEnterprises.setStatus('current')
if mibBuilder.loadTexts: otherEnterprises.setDescription('otherEnterprises provides a root object identifier from which mibs produced by other companies may be placed. mibs produced by other enterprises are typicially implemented with the object identifiers as defined in the mib, but if the mib is deemed to be uncontrolled, we may reroot the mib at this subtree in order to have a controlled version.')
ciscoSB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1))
if mibBuilder.loadTexts: ciscoSB.setStatus('current')
if mibBuilder.loadTexts: ciscoSB.setDescription('ciscoSB provides root Object Identifier for Management Information Base for products of Cisco Small Business. This includes products rebranded from linksys aquisition. MIB numbers under this root are managed and controlled by ciscosb_mib@cisco.com.')
ciscoSMB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 2))
if mibBuilder.loadTexts: ciscoSMB.setStatus('current')
if mibBuilder.loadTexts: ciscoSMB.setDescription('ciscoSMB provides root Object Identifier for Management Information Base for products of Cisco built for Small and Medium Business market.The MIB numbers under this root are managed and controlled by ciscosmb_mib@cisco.com')
ciscoAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 7))
if mibBuilder.loadTexts: ciscoAgentCapability.setStatus('current')
if mibBuilder.loadTexts: ciscoAgentCapability.setDescription('ciscoAgentCapability provides a root object identifier from which AGENT-CAPABILITIES values may be assigned.')
ciscoConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 8))
if mibBuilder.loadTexts: ciscoConfig.setStatus('current')
if mibBuilder.loadTexts: ciscoConfig.setDescription('ciscoConfig is the main subtree for configuration mibs.')
ciscoMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9))
if mibBuilder.loadTexts: ciscoMgmt.setStatus('current')
if mibBuilder.loadTexts: ciscoMgmt.setDescription('ciscoMgmt is the main subtree for new mib development.')
ciscoExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10))
if mibBuilder.loadTexts: ciscoExperiment.setStatus('current')
if mibBuilder.loadTexts: ciscoExperiment.setDescription('ciscoExperiment provides a root object identifier from which experimental mibs may be temporarily based. mibs are typicially based here if they fall in one of two categories 1) are IETF work-in-process mibs which have not been assigned a permanent object identifier by the IANA. 2) are cisco work-in-process which has not been assigned a permanent object identifier by the cisco assigned number authority, typicially because the mib is not ready for deployment. NOTE WELL: support for mibs in the ciscoExperiment subtree will be deleted when a permanent object identifier assignment is made.')
ciscoAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11))
if mibBuilder.loadTexts: ciscoAdmin.setStatus('current')
if mibBuilder.loadTexts: ciscoAdmin.setDescription('ciscoAdmin is reserved for administratively assigned OBJECT IDENTIFIERS, i.e. those not associated with MIB objects')
ciscoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 12))
if mibBuilder.loadTexts: ciscoModules.setStatus('current')
if mibBuilder.loadTexts: ciscoModules.setDescription('ciscoModules provides a root object identifier from which MODULE-IDENTITY values may be assigned.')
lightstream = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 13))
if mibBuilder.loadTexts: lightstream.setStatus('current')
if mibBuilder.loadTexts: lightstream.setDescription('subtree reserved for use by Lightstream')
ciscoworks = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 14))
if mibBuilder.loadTexts: ciscoworks.setStatus('current')
if mibBuilder.loadTexts: ciscoworks.setDescription('ciscoworks provides a root object identifier beneath which mibs applicable to the CiscoWorks family of network management products are defined.')
newport = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 15))
if mibBuilder.loadTexts: newport.setStatus('current')
if mibBuilder.loadTexts: newport.setDescription('subtree reserved for use by the former Newport Systems Solutions, now a portion of the Access Business Unit.')
ciscoPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 16))
if mibBuilder.loadTexts: ciscoPartnerProducts.setStatus('current')
if mibBuilder.loadTexts: ciscoPartnerProducts.setDescription('ciscoPartnerProducts is the root OBJECT IDENTIFIER from which partner sysObjectID values may be assigned. Such sysObjectID values are composed of the ciscoPartnerProducts prefix, followed by a single identifier that is unique for each partner, followed by the value of sysObjectID of the Cisco product from which partner product is derived. Note that the chassisPartner MIB object defines the value of the identifier assigned to each partner.')
ciscoPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17))
if mibBuilder.loadTexts: ciscoPolicy.setStatus('current')
if mibBuilder.loadTexts: ciscoPolicy.setDescription('ciscoPolicy is the root of the Cisco-assigned OID subtree for use with Policy Management.')
ciscoPIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17, 2))
if mibBuilder.loadTexts: ciscoPIB.setStatus('current')
if mibBuilder.loadTexts: ciscoPIB.setDescription('ciscoPIB is the root of the Cisco-assigned OID subtree for assignment to PIB (Policy Information Base) modules.')
ciscoPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18))
if mibBuilder.loadTexts: ciscoPolicyAuto.setStatus('current')
if mibBuilder.loadTexts: ciscoPolicyAuto.setDescription('ciscoPolicyAuto is the root of the Cisco-assigned OID subtree for OIDs which are automatically assigned for use in Policy Management.')
ciscoPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18, 2))
if mibBuilder.loadTexts: ciscoPibToMib.setStatus('current')
if mibBuilder.loadTexts: ciscoPibToMib.setDescription("ciscoPibToMib is the root of the Cisco-assigned OID subtree for MIBs which are algorithmically generated/translated from Cisco PIBs with OIDs assigned under the ciscoPIB subtree. These generated MIBs allow management entities (other the current Policy Server) to read the downloaded policy. By convention, for PIB 'ciscoPIB.x', the generated MIB shall have the name 'ciscoPibToMib.x'.")
ciscoDomains = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19))
if mibBuilder.loadTexts: ciscoDomains.setStatus('current')
if mibBuilder.loadTexts: ciscoDomains.setDescription('ciscoDomains provides a root object identifier from which different transport mapping values may be assigned.')
ciscoCIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20))
if mibBuilder.loadTexts: ciscoCIB.setStatus('current')
if mibBuilder.loadTexts: ciscoCIB.setDescription('ciscoCIB is the root of the Cisco-assigned OID subtree for assignment to MIB modules describing managed objects that part of the CPE automatic configuration framework.')
ciscoCibMmiGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 1))
if mibBuilder.loadTexts: ciscoCibMmiGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCibMmiGroup.setDescription('ciscoCibMmiGroup is the root of the Cisco-assigned OID subtree for assignment to MIB modules describing managed objects supporting the Modem Management Interface (MMI), the interface that facilitates CPE automatic configuration.')
ciscoCibProvGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 2))
if mibBuilder.loadTexts: ciscoCibProvGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCibProvGroup.setDescription('ciscoCibStoreGroup is the root of the Cisco-assigned OID subtree for assignment to MIB modules describing managed objects contributing to the Configuration Information Base (CIB).')
ciscoPKI = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 21))
if mibBuilder.loadTexts: ciscoPKI.setStatus('current')
if mibBuilder.loadTexts: ciscoPKI.setDescription('ciscoPKI is the root of cisco-assigned OID subtree for PKI Certificate Policies and Certificate Extensions.')
ciscoLDAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 22))
if mibBuilder.loadTexts: ciscoLDAP.setStatus('current')
if mibBuilder.loadTexts: ciscoLDAP.setDescription('ciscoLDAP is the root of the Cisco-assigned OID subtree for assignment to LDAP (Lightweight Directory Access Protocol) modules.')
ciscoProxy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 1))
if mibBuilder.loadTexts: ciscoProxy.setStatus('current')
if mibBuilder.loadTexts: ciscoProxy.setDescription('ciscoProxy OBJECT IDENTIFIERS are used to uniquely name party mib records created to proxy for SNMPv1.')
ciscoPartyProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 1))
ciscoContextProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 2))
ciscoRptrGroupObjectID = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2))
if mibBuilder.loadTexts: ciscoRptrGroupObjectID.setStatus('current')
if mibBuilder.loadTexts: ciscoRptrGroupObjectID.setDescription('ciscoRptrGroupObjectID OBJECT IDENTIFIERS are used to uniquely identify groups of repeater ports for use by the SNMP-REPEATER-MIB (RFC 1516) rptrGroupObjectID object.')
ciscoUnknownRptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 1))
if mibBuilder.loadTexts: ciscoUnknownRptrGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoUnknownRptrGroup.setDescription('The identity of an unknown repeater port group.')
cisco2505RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 2))
if mibBuilder.loadTexts: cisco2505RptrGroup.setStatus('current')
if mibBuilder.loadTexts: cisco2505RptrGroup.setDescription('The authoritative identity of the Cisco 2505 repeater port group.')
cisco2507RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 3))
if mibBuilder.loadTexts: cisco2507RptrGroup.setStatus('current')
if mibBuilder.loadTexts: cisco2507RptrGroup.setDescription('The authoritative identity of the Cisco 2507 repeater port group.')
cisco2516RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 4))
if mibBuilder.loadTexts: cisco2516RptrGroup.setStatus('current')
if mibBuilder.loadTexts: cisco2516RptrGroup.setDescription('The authoritative identity of the Cisco 2516 repeater port group.')
ciscoWsx5020RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 5))
if mibBuilder.loadTexts: ciscoWsx5020RptrGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoWsx5020RptrGroup.setDescription('The authoritative identity of the wsx5020 repeater port group.')
ciscoChipSets = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3))
if mibBuilder.loadTexts: ciscoChipSets.setStatus('current')
if mibBuilder.loadTexts: ciscoChipSets.setDescription('Numerous media-specific MIBS have an object, defined as an OBJECT IDENTIFIER, which is the identity of the chipset realizing the interface. Cisco-specific chipsets have their OBJECT IDENTIFIERS assigned under this subtree.')
ciscoChipSetSaint1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 1))
if mibBuilder.loadTexts: ciscoChipSetSaint1.setStatus('current')
if mibBuilder.loadTexts: ciscoChipSetSaint1.setDescription('The identity of the Rev 1 SAINT ethernet chipset manufactured for cisco by LSI Logic.')
ciscoChipSetSaint2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 2))
if mibBuilder.loadTexts: ciscoChipSetSaint2.setStatus('current')
if mibBuilder.loadTexts: ciscoChipSetSaint2.setDescription('The identity of the Rev 2 SAINT ethernet chipset manufactured for cisco by LSI Logic.')
ciscoChipSetSaint3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 3))
if mibBuilder.loadTexts: ciscoChipSetSaint3.setStatus('current')
if mibBuilder.loadTexts: ciscoChipSetSaint3.setDescription('The identity of the Rev 3 SAINT ethernet chipset manufactured for cisco by Plessey.')
ciscoChipSetSaint4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 4))
if mibBuilder.loadTexts: ciscoChipSetSaint4.setStatus('current')
if mibBuilder.loadTexts: ciscoChipSetSaint4.setDescription('The identity of the Rev 4 SAINT ethernet chipset manufactured for cisco by Mitsubishi.')
ciscoTDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 19, 99999))
ciscoTDomainUdpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 1))
if mibBuilder.loadTexts: ciscoTDomainUdpIpv4.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainUdpIpv4.setDescription('The UDP over IPv4 transport domain. The corresponding transport address is of type CiscoTAddressIPv4.')
ciscoTDomainUdpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 2))
if mibBuilder.loadTexts: ciscoTDomainUdpIpv6.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainUdpIpv6.setDescription('The UDP over IPv6 transport domain. The corresponding transport address is of type CiscoTAddressIPv6 for global IPv6 addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.')
ciscoTDomainTcpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 3))
if mibBuilder.loadTexts: ciscoTDomainTcpIpv4.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainTcpIpv4.setDescription('The TCP over IPv4 transport domain. The corresponding transport address is of type CiscoTAddressIPv4.')
ciscoTDomainTcpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 4))
if mibBuilder.loadTexts: ciscoTDomainTcpIpv6.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainTcpIpv6.setDescription('The TCP over IPv6 transport domain. The corresponding transport address is of type CiscoTAddressIPv6 for global IPv6 addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.')
ciscoTDomainLocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 5))
if mibBuilder.loadTexts: ciscoTDomainLocal.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainLocal.setDescription('The Posix Local IPC transport domain. The corresponding transport address is of type CiscoTAddressLocal. The Posix Local IPC transport domain incorporates the well known UNIX domain sockets.')
ciscoTDomainClns = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 6))
if mibBuilder.loadTexts: ciscoTDomainClns.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainClns.setDescription('The CLNS transport domain. The corresponding transport address is of type CiscoTAddressOSI.')
ciscoTDomainCons = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 7))
if mibBuilder.loadTexts: ciscoTDomainCons.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainCons.setDescription('The CONS transport domain. The corresponding transport address is of type CiscoTAddressOSI.')
ciscoTDomainDdp = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 8))
if mibBuilder.loadTexts: ciscoTDomainDdp.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainDdp.setDescription('The DDP transport domain. The corresponding transport address is of type CiscoTAddressNBP.')
ciscoTDomainIpx = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 9))
if mibBuilder.loadTexts: ciscoTDomainIpx.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainIpx.setDescription('The IPX transport domain. The corresponding transport address is of type CiscoTAddressIPX.')
ciscoTDomainSctpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 10))
if mibBuilder.loadTexts: ciscoTDomainSctpIpv4.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainSctpIpv4.setDescription('The SCTP over IPv4 transport domain. The corresponding transport address is of type CiscoTAddressIPv4.')
if mibBuilder.loadTexts: ciscoTDomainSctpIpv4.setReference('RFC 2960 - Stream Control Transmission Protocol. R. Stewart, Q. Xie, K. Morneault, C. Sharp, H. Schwarzbauer, T. Taylor, I. Rytina, M. Kalla, L. Zhang, V. Paxson. October 2000.')
ciscoTDomainSctpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 11))
if mibBuilder.loadTexts: ciscoTDomainSctpIpv6.setStatus('current')
if mibBuilder.loadTexts: ciscoTDomainSctpIpv6.setDescription('The SCTP over IPv6 transport domain. The corresponding transport address is of type CiscoTAddressIPv6 for global IPv6 addresses and CiscoTAddressIPv6s for scoped IPv6 addresses.')
if mibBuilder.loadTexts: ciscoTDomainSctpIpv6.setReference('RFC 2960 - Stream Control Transmission Protocol. R. Stewart, Q. Xie, K. Morneault, C. Sharp, H. Schwarzbauer, T. Taylor, I. Rytina, M. Kalla, L. Zhang, V. Paxson. October 2000.')
mibBuilder.exportSymbols("CISCO-SMI", ciscoRptrGroupObjectID=ciscoRptrGroupObjectID, ciscoDomains=ciscoDomains, ciscoChipSets=ciscoChipSets, ciscoPKI=ciscoPKI, ciscoPartnerProducts=ciscoPartnerProducts, ciscoAdmin=ciscoAdmin, ciscoPolicyAuto=ciscoPolicyAuto, ciscoTDomains=ciscoTDomains, ciscoChipSetSaint4=ciscoChipSetSaint4, ciscoTDomainUdpIpv6=ciscoTDomainUdpIpv6, ciscoTDomainCons=ciscoTDomainCons, cisco=cisco, ciscoSB=ciscoSB, pakmon=pakmon, ciscoAgentCapability=ciscoAgentCapability, newport=newport, cisco2507RptrGroup=cisco2507RptrGroup, ciscoworks=ciscoworks, ciscoTDomainUdpIpv4=ciscoTDomainUdpIpv4, ciscoTDomainTcpIpv4=ciscoTDomainTcpIpv4, ciscoCIB=ciscoCIB, ciscoTDomainDdp=ciscoTDomainDdp, ciscoCibProvGroup=ciscoCibProvGroup, cisco2516RptrGroup=cisco2516RptrGroup, ciscoTDomainLocal=ciscoTDomainLocal, ciscoPartyProxy=ciscoPartyProxy, ciscoWsx5020RptrGroup=ciscoWsx5020RptrGroup, ciscoTDomainTcpIpv6=ciscoTDomainTcpIpv6, ciscoTDomainClns=ciscoTDomainClns, ciscoTDomainSctpIpv6=ciscoTDomainSctpIpv6, ciscoPibToMib=ciscoPibToMib, temporary=temporary, otherEnterprises=otherEnterprises, ciscoTDomainIpx=ciscoTDomainIpx, ciscoProxy=ciscoProxy, ciscoTDomainSctpIpv4=ciscoTDomainSctpIpv4, PYSNMP_MODULE_ID=cisco, ciscoCibMmiGroup=ciscoCibMmiGroup, ciscoPolicy=ciscoPolicy, workgroup=workgroup, ciscoChipSetSaint1=ciscoChipSetSaint1, ciscoLDAP=ciscoLDAP, ciscoChipSetSaint3=ciscoChipSetSaint3, local=local, ciscoUnknownRptrGroup=ciscoUnknownRptrGroup, ciscoSMB=ciscoSMB, ciscoExperiment=ciscoExperiment, ciscoConfig=ciscoConfig, ciscoModules=ciscoModules, ciscoPIB=ciscoPIB, cisco2505RptrGroup=cisco2505RptrGroup, lightstream=lightstream, ciscoContextProxy=ciscoContextProxy, ciscoMgmt=ciscoMgmt, ciscoProducts=ciscoProducts, ciscoChipSetSaint2=ciscoChipSetSaint2)
