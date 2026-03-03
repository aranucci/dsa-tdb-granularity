Portal:Data Services
====================

[![WMCS data services](//upload.wikimedia.org/wikipedia/commons/thumb/d/d2/WMCS_data_services.svg/120px-WMCS_data_services.svg.png)](https://wikitech.wikimedia.org/wiki/File:WMCS_data_services.svg)

**Data Services** includes services that allow for direct access to databases and dumps, as well as web interfaces for querying and programmatic access to data stores.

Data services currently include: Wiki Replicas, Wikimedia Dumps, Shared Storage, CirrusSearch Elasticsearch replicas, Quarry and PAWS.

Data stores
-----------

[**Wiki Replicas**](https://wikitech.wikimedia.org/wiki/Wiki_Replicas "Wiki Replicas")

[Wiki Replicas](https://wikitech.wikimedia.org/wiki/Wiki_Replicas "Wiki Replicas") are MySQL/MariaDB databases that replicate near-realtime from the production MediaWiki databases of Wikimedia Foundation wikis.

[**Wikimedia Dumps**](https://wikitech.wikimedia.org/wiki/Data_dumps "Data dumps")

[Wikimedia Dumps](https://wikitech.wikimedia.org/wiki/Data_dumps "Data dumps") offers a range of data downloads including full text dumps, and other datasets.

[**Shared Storage**](https://wikitech.wikimedia.org/wiki/Help:Shared_storage "Help:Shared storage")

[Shared Storage](https://wikitech.wikimedia.org/wiki/Help:Shared_storage) is offered via NFS. It includes shared directories offered to VPS and Toolforge users. Wikimedia Dumps are also offered via the Shared Storage services, but treated as a Data Service because of their wide use.

[**CirrusSearch OpenSearch replicas**](https://wikitech.wikimedia.org/wiki/Help:CirrusSearch_OpenSearch_replicas "Help:CirrusSearch OpenSearch replicas")

The "[Cloud Elastic](https://wikitech.wikimedia.org/wiki/Help:CirrusSearch_OpenSearch_replicas)" servers are a replica of the CirrusSearch OpenSearch indices made available to Wikimedia Cloud Services applications (both Cloud VPS and Toolforge).

[**Wikimedia Enterprise**](https://meta.wikimedia.org/wiki/Wikimedia_Enterprise "m:Wikimedia Enterprise")

[Wikimedia Enterprise](https://meta.wikimedia.org/wiki/Wikimedia_Enterprise "m:Wikimedia Enterprise") is a set of API's targeting large scale user needs. These APIs are maintained and developed by the Commercial Partnerships division. Users of Toolforge, Cloud VPS, or PAWS have access to the On-demand and Snapshot APIs.

Web interfaces
--------------

Quarry and PAWS require a Wikimedia SUL account to login.

[**Quarry**](https://wikitech.wikimedia.org/wiki/Quarry "Quarry")

[Quarry](https://wikitech.wikimedia.org/wiki/Quarry "Quarry") is a graphical web interface that allows users to query Wiki Replicas and ToolsDB using SQL.

[**PAWS**](https://wikitech.wikimedia.org/wiki/PAWS "PAWS")

[PAWS](https://wikitech.wikimedia.org/wiki/PAWS "PAWS") is a Jupyter notebooks installation hosted by Wikimedia Cloud Services that hosts Python notebooks and a terminal accessible through a web browser. You can access Wiki Replicas, ToolsDB and Dumps with PAWS.

See also
--------

*   [Data Services administrative documentation](https://wikitech.wikimedia.org/wiki/Portal:Data_Services/Admin "Portal:Data Services/Admin")

![](https://wikitech.wikimedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)