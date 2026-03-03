Research:Data
=============

There is a great deal of **publicly-available, open-licensed data about Wikimedia projects**. This page is intended to help community members, developers, and researchers who are interested in analyzing raw data learn what data and infrastructure is available.

If you have any questions, you might find the answer in the [Frequently Asked Questions about Data](https://meta.wikimedia.org/wiki/Research:Data/FAQ "Research:Data/FAQ"). If you still have questions, you can email your question to the [Analytics mailing list](https://lists.wikimedia.org/postorius/lists/analytics.lists.wikimedia.org/ "mail:analytics") ([more information](https://meta.wikimedia.org/wiki/Mailing_lists "Mailing lists")). You can also find a guide about basic concepts for researchers working with Wikimedia Data in the [data introduction](https://meta.wikimedia.org/wiki/Research:Data_introduction "Research:Data introduction") page.

If you wish to browse pre-computed metrics and dashboards, see [statistics](https://meta.wikimedia.org/wiki/Statistics "Statistics").

If this publicly available data isn't sufficient, you can look at the page on [private data access](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_access "wikitech:Data Platform/Data access") to see what non-public data exists and how you can gain access.

See also [inspirational example uses](https://seealso.org/).

Also consider searching for datasets at [Zenodo](https://zenodo.org/search?page=1&size=20&q=Wikipedia%20OR%20Wikimedia%20OR%20Wikidata&type=dataset), [Figshare](https://figshare.com/search?q=wikipedia&searchMode=1&types=3), [Dimensions.ai](https://app.dimensions.ai/discover/data_set?search_text=Wikipedia%20OR%20Wikimedia%20OR%20Wikidata&search_type=kws&search_field=full_search), [Google Dataset Search](https://datasetsearch.research.google.com/search?query=Wikipedia%20OR%20Wikidata%20OR%20Wikimedia), [Academic Torrents](https://academictorrents.com/browse.php?search=Wiki*), [DataHub](https://old.datahub.io/organization/wikimedia) (historical) or [Hugging Face](https://huggingface.co/datasets?sort=trending&search=Wikipedia) (see also a curated "[Wikimedia Datasets](https://huggingface.co/collections/frimelle/wikimedia-datasets-6645dd27f2a976b607e767be)" list on Huggingface).

Quick glance
------------

### By access method

**Data Dumps** ([details](#Data_dumps))

[Homepage](https://meta.wikimedia.org/wiki/Data_dumps "Data dumps") – [Download](https://dumps.wikimedia.org/backup-index.html)

Dumps of all [WMF projects](https://meta.wikimedia.org/wiki/Wikimedia_projects "Wikimedia projects") for backup, offline use, research, etc.

*   Wiki content, revisions, metadata, and page-to-page and outside links
*   XML and SQL format
*   once/twice a month
*   large file sizes
*   The dumps.wikimedia.org domain also hosts [other data](https://dumps.wikimedia.org/other/), including [MediaWiki history dumps](https://dumps.wikimedia.org/other/mediawiki_history/readme.html), a historical record of revision (without text), user and page events.

**APIs** ([details](#MediaWiki_API))

*   The **[MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page "mw:API:Main page")** provides direct, high-level access to the data contained in MediaWiki databases over the web.
    *   Meta info about the wiki and logged-in user, properties of pages (revisions, content, etc.) and lists of pages based on criteria
    *   JSON, XML, and PHP's native serialization format

*   The **Wikimedia REST API** provides [page content in various formats](https://wikimedia.org/api/rest_v1/).

*   The [**Wikimedia Analytics API**](https://doc.wikimedia.org/analytics-api "wmdoc:analytics-api") provides pageviews and aggregate edit stats.

**Wiki Replicas** ([details](#Wiki_Replicas))

**[Data Services](https://wikitech.wikimedia.org/wiki/Portal:Data_Services "wikitech:Portal:Data Services")** allows [Wikimedia Cloud Services](https://wikitech.wikimedia.org/wiki/Help:Cloud_Services_introduction "wikitech:Help:Cloud Services introduction") users to query a sanitized copy of the Wikimedia MediaWiki databases.

*   **[Toolforge](https://wikitech.wikimedia.org/wiki/Portal:Toolforge "wikitech:Portal:Toolforge")** and **[Cloud VPS](https://wikitech.wikimedia.org/wiki/Portal:Cloud_VPS "wikitech:Portal:Cloud VPS")** hosting environments include access to the Wiki Replicas.
*   **[PAWS](https://wikitech.wikimedia.org/wiki/PAWS "wikitech:PAWS")** is a [Jupyter Notebook](https://en.wikipedia.org/wiki/Jupyter "w:Jupyter") environment that allows e.g. querying the Wiki Replicas and APIs for analysis.
*   **[Quarry](https://meta.wikimedia.org/wiki/Research:Quarry "Research:Quarry")** and [Superset](https://wikitech.wikimedia.org/wiki/Superset "wikitech:Superset") are a public web interfaces for SQL queries to the Wiki Replicas.

**Recent changes stream** ([details](#Recent_changes_stream))

[Homepage](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams "wikitech:Event Platform/EventStreams")

Wikimedia broadcasts every [change](https://www.mediawiki.org/wiki/Help:Recent_changes "mw:Help:Recent changes") to every Wikimedia wiki using Server Sent Events over HTTP.

**Analytics Dumps** ([details](#Analytics_dumps))

[Homepage](https://dumps.wikimedia.org/other/analytics/)

Raw [pageviews](https://meta.wikimedia.org/wiki/Research:Page_view "Research:Page view"), [unique device estimates](https://meta.wikimedia.org/wiki/Research:Unique_devices "Research:Unique devices"), [mediacounts](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Traffic/Mediacounts "wikitech:Data Platform/Data Lake/Traffic/Mediacounts"), etc.

*   Delimited, usually: Project, (Page title,) Count
*   Aggregated hourly or daily
*   [pageviews complete](https://dumps.wikimedia.org/other/pageview_complete/readme.html) – [mediacounts](https://dumps.wikimedia.org/other/mediacounts/) – [unique devices](https://dumps.wikimedia.org/other/unique_devices/)

**WikiStats** ([details](#WikiStats))

[Homepage](https://stats.wikimedia.org/)

Reports based on data dumps and server log files.

*   Unique visits, page views, active editors and more
*   Intermediate CSV files available
*   Graphical presentation

**DBpedia** ([details](#DBpedia))

DBpedia extracts structured data from Wikipedia. It allows users to run complex queries and link Wikipedia data to other data sets.

*   RDF, N-triplets, SPARQL endpoint, Linked Data
*   Billions of triplets of info in a consistent ontology

**DataHub and Figshare** ([details](#DataHub))

[DataHub Homepage](https://datahub.io/organization/wikimedia)

A collection of various Wikimedia-related datasets.

*   Smaller (usually one-time) surveys/studies
*   DBpedia-Live and others
*   [Figshare (datasets tagged 'wikipedia')](https://figshare.com/search?q=:tag:%20wikipedia)

**Differential privacy** ([details](#Differential_privacy))

[Differential privacy](https://meta.wikimedia.org/wiki/Differential_privacy "Differential privacy") homepage

A collection of differentially-private datasets, released daily, weekly, or monthly.

*   pageview data
*   editor/edit data
*   centralnotice data
*   search data

**Training data for AI/ML models** ([details](#Training_datasets_for_machine_learning_models))

[Machine learning models](https://meta.wikimedia.org/wiki/Machine_learning_models "Machine learning models") homepage

A collection of AI/ML models in production that are used to power user-facing tools and features across Wikimedia projects. All such models have a corresponding model card which includes a variety of information about the model including information about the models’ training datasets.

### By data domain

The table below is a quick reference of data sources organized by data domain. For a more detailed overview of Wikimedia data domains and how to access data in each domain, use the links in the table or see [Research:Data introduction](https://meta.wikimedia.org/wiki/Research:Data_introduction "Research:Data introduction").

| Data domain | Data source | Access method |
| --- | --- | --- |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [MediaWiki REST API](https://www.mediawiki.org/wiki/API:REST_API "mw:API:REST API") | API |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [MediaWiki Action API:Parse](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Parse "mw:Special:MyLanguage/API:Parse") (HTML) | API |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [MediaWiki Action API:Revisions](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Revisions "mw:Special:MyLanguage/API:Revisions") (wikitext) | API |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [Wikidata:REST\_API](https://www.wikidata.org/wiki/Wikidata:REST_API "wikidata:Wikidata:REST API") | API |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [Wikimedia Enterprise APIs](https://enterprise.wikimedia.com/docs/) (require separate accounts, free access may have limits) | API |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [Wikidata:REST\_API](https://www.wikidata.org/wiki/Wikidata:REST_API "wikidata:Wikidata:REST API") | API |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [Wikidata SPARQL query service](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service "wikidata:Wikidata:SPARQL query service") | API |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [Commons SPARQL query service](https://commons.wikimedia.org/wiki/Commons:SPARQL_query_service "c:Commons:SPARQL query service") | API |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [DBpedia SPARQL endpoint](https://dbpedia.org/sparql) | API |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [MediaWiki Action API: Revisions](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Revisions "mw:Special:MyLanguage/API:Revisions") | API |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [MediaWiki Action API: Allrevisions](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Allrevisions "mw:Special:MyLanguage/API:Allrevisions") | API |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Wikimedia Analytics API](https://doc.wikimedia.org/analytics-api "wmdoc:analytics-api"): Edits data | API |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [MediaWiki Event Streams](https://stream.wikimedia.org/?doc#/streams) | API |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Wikimedia Enterprise APIs](https://enterprise.wikimedia.com/docs/) (require separate accounts, free access may have limits) | API |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Wikimedia Analytics API](https://doc.wikimedia.org/analytics-api "wmdoc:analytics-api"): Editors by country | API |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [MediaWiki Action API: Users](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Users "mw:Special:MyLanguage/API:Users") | API |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [MediaWiki Action API: Usercontribs](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Usercontribs "mw:Special:MyLanguage/API:Usercontribs") | API |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Wikimedia Analytics API](https://doc.wikimedia.org/analytics-api "wmdoc:analytics-api"): Pageviews | API |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Wikimedia Analytics API](https://doc.wikimedia.org/analytics-api "wmdoc:analytics-api"): Unique devices | API |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Wikimedia Analytics API](https://doc.wikimedia.org/analytics-api "wmdoc:analytics-api"): Mediarequests | API |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Wikistats](https://stats.wikimedia.org/) | Dashboard |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [XTools](https://xtools.wmcloud.org/ "xtools:") | Dashboard |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Bitergia: technical community metrics](https://wikimedia.biterg.io/app/dashboards#/view/Overview?_g=\(\)&_a=h@8ce1541) | Dashboard |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Wikistats](https://stats.wikimedia.org/) | Dashboard |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [XTools](https://xtools.wmcloud.org/ "xtools:") | Dashboard |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Bitergia: technical community metrics](https://wikimedia.biterg.io/app/dashboards#/view/Overview?_g=\(\)&_a=h@8ce1541) | Dashboard |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Devices](https://analytics.wikimedia.org/dashboards/browsers/#all-sites-by-os) | Dashboard |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Wikistats](https://stats.wikimedia.org/) | Dashboard |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Readers:Pageviews and Unique Devices](https://analytics.wikimedia.org/dashboards/vital-signs/) | Dashboard |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Pageviews Tool](https://pageviews.wmcloud.org/) | Dashboard |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [WikiNav](https://wikinav.toolforge.org/) | Dashboard |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [Wikitext](https://dumps.wikimedia.org/backup-index.html) | Download |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | Static HTML and Enterprise HTML (use mwparserfromhtml) | Download |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [Knowledge gaps](https://meta.wikimedia.org/wiki/Research:Knowledge_Gaps_Index/Datasets "Research:Knowledge Gaps Index/Datasets") | Download |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [Commons image depicts](https://dumps.wikimedia.org/other/wikibase/commonswiki/) | Download |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [Wikidata dumps (JSON, RDF, XML)](https://www.wikidata.org/wiki/Wikidata:Database_download "wikidata:Wikidata:Database download") | Download |
| [Content – structured data](https://meta.wikimedia.org/wiki/Research:Data_introduction#Structured_data "Research:Data introduction") | [DBpedia.org](https://dbpedia.org/) | Download |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Mediawiki\_history](https://dumps.wikimedia.org/other/mediawiki_history/readme.html) | Download |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [geoeditors](https://dumps.wikimedia.org/other/geoeditors/readme.html) | Download |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Differential privacy: Geoeditors](https://meta.wikimedia.org/wiki/Differential_privacy/Completed/Geoeditors "Differential privacy/Completed/Geoeditors") | Download |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Clickstream](https://dumps.wikimedia.org/other/clickstream/readme.html) | Download |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Pageview hourly](https://dumps.wikimedia.org/other/pageview_complete/readme.html) | Download |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Unique devices](https://dumps.wikimedia.org/other/unique_devices/readme.html) | Download |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Mediacounts](https://dumps.wikimedia.org/other/mediacounts/readme.html) | Download |
| [Traffic](https://meta.wikimedia.org/wiki/Research:Data_introduction#Traffic-data "Research:Data introduction") | [Differential privacy pageviews](https://meta.wikimedia.org/wiki/Differential_privacy/Completed/Country-project-page "Differential privacy/Completed/Country-project-page") | Download |
| [Content](https://meta.wikimedia.org/wiki/Research:Data_introduction#Content-data "Research:Data introduction") | [Text](https://www.mediawiki.org/wiki/Manual:Text_table "mw:Manual:Text table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributions / edits](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Revision\_table](https://www.mediawiki.org/wiki/Manual:Revision_table "mw:Manual:Revision table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Mediawiki\_history](https://dumps.wikimedia.org/other/mediawiki_history/readme.html) | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [geoeditors](https://dumps.wikimedia.org/other/geoeditors/readme.html) | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [Differential privacy: Geoeditors](https://meta.wikimedia.org/wiki/Differential_privacy/Completed/Geoeditors "Differential privacy/Completed/Geoeditors") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [actor](https://www.mediawiki.org/wiki/Manual:Actor_table "mw:Manual:Actor table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [user](https://www.mediawiki.org/wiki/Manual:User_table "mw:Manual:User table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [user\_groups](https://www.mediawiki.org/wiki/Manual:User_groups_table "mw:Manual:User groups table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [user\_former\_groups](https://www.mediawiki.org/wiki/Manual:User_former_groups_table "mw:Manual:User former groups table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [user\_properties](https://www.mediawiki.org/wiki/Manual:User_properties_table "mw:Manual:User properties table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [globaluser](https://www.mediawiki.org/wiki/Extension:CentralAuth/globaluser_table "mw:Extension:CentralAuth/globaluser table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |
| [Contributors / editors](https://meta.wikimedia.org/wiki/Research:Data_introduction#Contributing-data "Research:Data introduction") | [user\_groups](https://www.mediawiki.org/wiki/Manual:User_groups_table "mw:Manual:User groups table") | [MediaWiki database tables](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") |

Data dumps
----------

WMF releases [data dumps](https://meta.wikimedia.org/wiki/Data_dumps "Data dumps") of Wikipedia, Wikidata, and all WMF projects on a regular basis, as well as dumps of other Wikimedia-related data such as search indices and short URL mappings.

### Content

#### XML/SQL dumps

*   Text of current and/or all revisions of all pages, in XML format [(schema)](https://www.mediawiki.org/xml/)
*   Metadata for current and/or all revisions of all pages, in XML format [(schema)](https://www.mediawiki.org/xml/)
*   Most database tables as SQL files
    *   Page-to-page link lists (`pagelinks`, `categorylinks`, `imagelinks`, `templatelinks` tables)
    *   Lists of pages with links outside of the project (`externallinks`, `iwlinks`, `langlinks` tables)
    *   Media metadata (`image`, `oldimage` tables)
    *   Info about each page (`page`, `page_props`, `page_restrictions` tables)
    *   Titles of all pages in the main namespace, i.e. all articles (`*-all-titles-in-ns0.gz`)
    *   List of all pages that are redirects and their targets (`redirect` table)
    *   Log data, including blocks, protection, deletion, uploads (`logging` table)
    *   Misc bits (`interwiki`, `site_stats`, `user_groups` tables)
*   Stub-prefixed dumps for some projects which only have header info for pages and revisions without actual content

[See a more comprehensive list of what is available for download.](https://meta.wikimedia.org/wiki/Data_dumps/What%27s_available_for_download "Data dumps/What's available for download")

#### Other dumps

Dumps.wikimedia.org offers [various other database dumps and datasets](https://dumps.wikimedia.org/other/), including

*   [Adds/changes dumps](https://dumps.wikimedia.org/other/incr/) (includes no moves or deletes, plus some other limitations) ([documentation](https://wikitech.wikimedia.org/wiki/Dumps/Adds-changes_dumps "wikitech:Dumps/Adds-changes dumps"))
*   [Wikidata entity dumps](https://dumps.wikimedia.org/other/wikibase/wikidatawiki/) – see [Wikidata:Data access](https://www.wikidata.org/wiki/Wikidata:Data_access#Dumps "wikidata:Wikidata:Data access") for more information
*   Various analytics datasets (described [below](#Analytics_Datasets))

### Download

You can [download the latest dumps for the last year](https://dumps.wikimedia.org/) ([dumps.wikimedia.org/enwiki/](https://dumps.wikimedia.org/enwiki/) for English Wikipedia, [dumps.wikimedia.org/dewiki/](https://dumps.wikimedia.org/dewiki/) for German Wikipedia, etc). [Download mirrors](https://meta.wikimedia.org/wiki/Mirroring_Wikimedia_project_XML_dumps#Current_Mirrors "Mirroring Wikimedia project XML dumps") offer an alternative to the download page.

Due to large file sizes, using a [download tool](https://meta.wikimedia.org/wiki/Data_dumps/Download_tools "Data dumps/Download tools") is recommended.

There are also [archives](https://dumps.wikimedia.org/archive/). Many older dumps can also be found at the [Internet Archive](https://archive.org/details/wikimedia-mediatar?&sort=-downloads).

### Data format

XML dumps are in the wrapper format described at [Export format](https://www.mediawiki.org/wiki/Help:Export#Export_format "mw:Help:Export") ([schema](https://www.mediawiki.org/xml/export-0.10.xsd)). Files are compressed in gzip (.gz), bzip2/lbzip2 (.bz2) and .7z formats.

SQL dumps are provided as dumps of entire tables, using mysqldump.

Some older dumps exist in [various formats](https://meta.wikimedia.org/wiki/Data_dumps/Dump_format "Data dumps/Dump format").

### How to and examples

See [examples of importing dumps in a MySQL database with step-by-step instructions](https://meta.wikimedia.org/wiki/Data_dumps/Import_examples "Data dumps/Import examples").

### Existing tools

Some tools are listed on the following pages, but these tools are mostly outdated and non-functional:

*   [Tools for importing](https://meta.wikimedia.org/wiki/Data_dumps/Tools_for_importing "Data dumps/Tools for importing")
*   [Other tools](https://meta.wikimedia.org/wiki/Data_dumps/Other_tools "Data dumps/Other tools")

### License

All text content is multi-licensed under the [Creative Commons Attribution-ShareAlike 3.0 License (CC-BY-SA)](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License "en:Wikipedia:Text of Creative Commons Attribution-ShareAlike 3.0 Unported License") and the [GNU Free Documentation License (GFDL)](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License "en:Wikipedia:Text of the GNU Free Documentation License"). Images and other files are available under [different terms](https://en.wikipedia.org/wiki/Wikipedia:File_copyright_tags "en:Wikipedia:File copyright tags"), as detailed on their description pages.

### Support

*   Mailing list: [xmldatadumps-l](https://lists.wikimedia.org/postorius/lists/xmldatadumps-l.lists.wikimedia.org/ "mail:xmldatadumps-l")
*   Bug reports: [Dumps Generation](https://phabricator.wikimedia.org/project/board/1519/query/all/ "phab:project/board/1519/query/all/") project in [Phabricator](https://www.mediawiki.org/wiki/Phabricator "mw:Phabricator")
*   Design work on Dumps 2.0 replacement: [Dumps Rewrite](https://phabricator.wikimedia.org/project/view/1729/ "phab:project/view/1729/") project in [Phabricator](https://www.mediawiki.org/wiki/Phabricator "mw:Phabricator")

  

MediaWiki API
-------------

The MediaWiki API provides direct, high-level access to the data contained in MediaWiki databases. Client programs can log in to a wiki, get data, and post changes automatically by making HTTP requests.

### Content

*   [Meta information](https://www.mediawiki.org/wiki/API:Meta "mw:API:Meta") about the wiki and the logged-in user
*   [Properties](https://www.mediawiki.org/wiki/API:Properties "mw:API:Properties") of pages, including page revisions and content, external links, categories, templates,etc.
*   [Lists of pages](https://www.mediawiki.org/wiki/API:Lists "mw:API:Lists") that match certain criteria
*   See the [full list of available information](https://www.mediawiki.org/wiki/API "mw:API")
    *   See also [additional information for Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access#MediaWiki_Action_API "wikidata:Wikidata:Data access") and Wikidata's [SPARQL query endpoint](https://www.wikidata.org/wiki/Wikidata:Data_access#Wikidata_Query_Service "wikidata:Wikidata:Data access")

### Endpoint

To query the database you send a HTTP GET request to the desired [endpoint](https://www.mediawiki.org/wiki/API:Main_page#Endpoint "mw:API:Main page") (example [https://en.wikipedia.org/w/api.php](https://en.wikipedia.org/w/api.php) for English Wikipedia) setting the action parameter to `query` and defining the [query](https://www.mediawiki.org/wiki/API:Query "mw:API:Query") details the URL.

### How to and examples

*   [API Tutorial](https://www.mediawiki.org/wiki/API:Tutorial "mw:API:Tutorial")
*   Example: `[https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xml&titles=Main%20Page](https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xml&titles=Main%20Page)` fetches (`action=query`) the content (`rvprop=content`) of the most recent revision of Main Page (`titles=Main%20Page`) of English Wikipedia (`[https://en.wikipedia.org/w/api.php](https://en.wikipedia.org/w/api.php)?`) in XML format (`format=xml`). You can paste the URL in a browser to see the output.
*   [More examples](https://www.mediawiki.org/wiki/API:Query "mw:API:Query")

### Existing tools

To try out the API interactively on English Wikipedia, use the [API Sandbox](https://en.wikipedia.org/wiki/en:Special:ApiSandbox "w:en:Special:ApiSandbox").

### Access

To use the API, your application or client might need to [log in](https://www.mediawiki.org/wiki/API:Login "mw:API:Login").

Before you start, learn about the [API etiquette](https://www.mediawiki.org/wiki/API:Etiquette "mw:API:Etiquette").

Researchers could be given [Special access rights](https://meta.wikimedia.org/wiki/Research:FAQ#How_do_I_get_special_API_privileges_for_my_research? "Research:FAQ") on case-to-case bases.

### License

All text content is multi-licensed under the [Creative Commons Attribution-ShareAlike 3.0 License (CC-BY-SA)](https://en.wikipedia.org/wiki/en:Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License "w:en:Wikipedia:Text of Creative Commons Attribution-ShareAlike 3.0 Unported License") and the [GNU Free Documentation License (GFDL)](https://en.wikipedia.org/wiki/en:Wikipedia:Text_of_the_GNU_Free_Documentation_License "w:en:Wikipedia:Text of the GNU Free Documentation License").

### Support

*   [Frequently asked questions (FAQ)](https://www.mediawiki.org/wiki/API:FAQ "mw:API:FAQ")
*   [mediawiki-api](https://lists.wikimedia.org/postorius/lists/mediawiki-api.lists.wikimedia.org/ "mail:mediawiki-api") mailing list

Wiki Replicas
-------------

The [Wiki Replicas](https://wikitech.wikimedia.org/wiki/Help:Wiki_Replicas "wikitech:Help:Wiki Replicas") (part of WMCS [wikitech:Portal:Data Services](https://wikitech.wikimedia.org/wiki/Portal:Data_Services "wikitech:Portal:Data Services")) host sanitized versions of Wikimedia production MediaWiki databases.

### Content

Users of various [Wikimedia Cloud Services](https://wikitech.wikimedia.org/wiki/Help:Cloud_Services_introduction "wikitech:Help:Cloud Services introduction") products can access the wiki Wiki Replicas databases that host sanitized copies of the databases of all Wikimedia projects including Commons.

### Data format

Explore the [database schema](https://www.mediawiki.org/wiki/Manual:Database_layout "mw:Manual:Database layout") of the MediaWiki software.

### How to

See the [Wiki Replicas](https://wikitech.wikimedia.org/wiki/Help:Wiki_Replicas "wikitech:Help:Wiki Replicas") page on Wikitech on how to access the Wiki Replicas.

### Support

See [wikitech:Help:Cloud Services introduction#Communication and support](https://wikitech.wikimedia.org/wiki/Help:Cloud_Services_introduction#Communication_and_support "wikitech:Help:Cloud Services introduction")

Recent changes stream
---------------------

See [EventStreams](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams "wikitech:Event Platform/EventStreams") to subscribe to [Recent changes](https://www.mediawiki.org/wiki/Help:Recent_changes "mw:Help:Recent changes") on all Wikimedia wikis. This broadcasts edits and other changes as they happen.

### Existing tools

See [wikitech:Event Platform/EventStreams/Powered By](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams/Powered_By "wikitech:Event Platform/EventStreams/Powered By")

Analytics Datasets
------------------

[Analytics Datasets](https://dumps.wikimedia.org/other/analytics/) on dumps.wikimedia.org offers stable and continuous datasets about web request statistics (including page views, mediacounts, unique devices), page revision history, data by country, and Wikidata QRanks.

### Pageview statistics

[Pageview statistics](https://dumps.wikimedia.org/other/pageview_complete/) are one example. Each request of a page reaches one of Wikimedia's [Varnish](https://wikitech.wikimedia.org/wiki/Varnish "wikitech:Varnish") caching hosts. The project name and the title of the page requested are logged and aggregated hourly.

Files starting with "project" contain total hits per project per hour statistics.

Per-country pageviews data is also available, sanitized for privacy reasons. See [this announcement post](https://diff.wikimedia.org/2023/06/21/new-dataset-uncovers-wikipedia-browsing-habits-while-protecting-users/) (June 2023).

See the [README](https://dumps.wikimedia.org/other/pageview_complete/readme.html) for details on the format.

You can interactively browse the page view statistics at [https://pageviews.toolforge.org](https://pageviews.toolforge.org/). More [documentation on the Pageviews Analysis tool is available](https://meta.wikimedia.org/wiki/Pageviews_Analysis "Pageviews Analysis").

### Clickstream data

The [Wikipedia clickstream](https://meta.wikimedia.org/wiki/Research:Wikipedia_clickstream "Research:Wikipedia clickstream") dataset contains counts of `(referrer, resource)`pairs extracted from the request logs of Wikipedia.

### Geoeditors

The [public "Geoeditors" dataset](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Edits/Geoeditors/Public "wikitech:Data Platform/Data Lake/Edits/Geoeditors/Public") contains information about the monthly number of active editors from a particular country on a particular Wikipedia language edition (bucketed and redacted for privacy reasons). For some earlier years, similar data is available at [\[1\]](https://stats.wikimedia.org/wikimedia/squids/SquidReportPageEditsPerLanguageBreakdown.htm)/[\[2\]](https://stats.wikimedia.org/wikimedia/squids/SquidReportPageEditsPerCountryBreakdown.htm), see also [Edits by project and country of origin](https://meta.wikimedia.org/wiki/Edits_by_project_and_country_of_origin "Edits by project and country of origin").

### Misc datasets

Additional datasets (mostly irregular or discontinued ones) are published at [https://analytics.wikimedia.org/datasets/](https://analytics.wikimedia.org/datasets/). These include [Caching research data](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Traffic/Caching "wikitech:Data Platform/Data Lake/Traffic/Caching"), and [AS Performance Report](https://performance.wikimedia.org/asreport/).

WikiStats
---------

[Wikistats](https://stats.wikimedia.org/) is an informal but widely recognized name for a set of reports which provide monthly trend information for all Wikimedia projects and wikis.

### Content

Many dashboards that display trends about reading, contributing, and content broken down by different projects such as:

*   unique visitors
*   page views (overall and mobile only)
*   editor activity
*   article count

### Data format

Data is presented as charts with the option to download the underlying data.

### Support

For more details on Wikistats, see [wikitech:Data Platform/Systems/Wikistats 2](https://wikitech.wikimedia.org/wiki/Data_Platform/Systems/Wikistats_2 "wikitech:Data Platform/Systems/Wikistats 2").

DBpedia
-------

[DBpedia.org](https://dbpedia.org/) is a community effort to extract structured information from Wikipedia and to make this information available on the Web. DBpedia allows you to ask sophisticated queries against Wikipedia and to link other datasets on the Web to Wikipedia data.

### Content

The English version of the DBpedia knowledge base describes millions of things, and the majority of items are classified in a consistent ontology (persons, places, creative works like music albums, films and video games, organizations like companies and educational institutions, species, diseases, etc.). Localized versions of DBpedia in more than hundred languages describe millions of things.

The data set also features:

*   about 2 billion pieces of information (RDF triples)
*   labels and abstracts for >10 million unique things in up to 111 different languages
*   millions of links to images, links to external web pages, data links into external RDF datasets, links to Wikipedia categories, YAGO categories
*   [https://www.dbpedia.org/resources/](https://www.dbpedia.org/resources/) has download links for all the data sets, different formats and languages.

### Data format

*   RDF/XML
*   Turtle
*   N-Triplets
*   SPARQL endpoint

### Access

*   [https://dbpedia.org/sparql](https://dbpedia.org/sparql) is DBpedia's SPARQL endpoint.

### License

*   DBpedia data from version 3.4 on is licensed under the terms of the [Creative Commons Attribution-ShareAlike 3.0 License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License "en:Wikipedia:Text of Creative Commons Attribution-ShareAlike 3.0 Unported License") and the [GNU Free Documentation License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License "en:Wikipedia:Text of the GNU Free Documentation License").

### Support

*   Mailing list: [DBpedia Discuss](https://lists.sourceforge.net/lists/listinfo/dbpedia-discussion)
*   Forum: [https://forum.dbpedia.org/](https://forum.dbpedia.org/)
*   [DBpedia related publications, blog posts and projects](https://www.dbpedia.org/community/publications/)

DataHub
-------

The [Wikimedia organization](https://old.datahub.io/organization/wikimedia) on the [Open Knowledge Foundation's](https://en.wikipedia.org/wiki/Open_Knowledge_Foundation "w:Open Knowledge Foundation") DataHub was established by the Wikimedia Foundation around 2013, and contains a collection of datasets about Wikipedia and other projects which mostly date from around 2013-2016.

[Wikivoyage](https://wikivoyage.org/) also maintains data on [its own DataHub](https://old.datahub.io/organization/wikivoyage):

*   Hotels/restaurants/attractions data as CSV/OSM/OBF
*   Tourism guide for offline use

Differential privacy
--------------------

The [WMF privacy engineering team](https://www.mediawiki.org/wiki/Wikimedia_Security_Team "mw:Wikimedia Security Team") uses [differential privacy](https://en.wikipedia.org/wiki/Differential_privacy "en:Differential privacy") to release data that would otherwise be too sensitive to release. This data currently only includes pageview statistics; in the future, it will include statistics about editors, centralnotice impressions and views, search, and more.

### Content

*   Pageview data (currently only available as daily TSVs)
    *   6 February 2023 – present: [README](https://analytics.wikimedia.org/published/datasets/country_project_page/00_README.html) / [raw data](https://analytics.wikimedia.org/published/datasets/country_project_page/)
    *   9 February 2017 – 5 February 2023: [README](https://analytics.wikimedia.org/published/datasets/country_project_page_historical/00_README.html) / [raw data](https://analytics.wikimedia.org/published/datasets/country_project_page_historical/)
    *   1 July 2015 – 8 February 2017: [README](https://analytics.wikimedia.org/published/datasets/country_project_page_historical_pre_2017/00_README.html) / [raw data](https://analytics.wikimedia.org/published/datasets/country_project_page_historical_pre_2017/)

### Data format

Differentially-private data is currently available in static TSV form at [https://analytics.wikimedia.org/published/datasets/](https://analytics.wikimedia.org/published/datasets/). Work to make this data available via API is ongoing.

### License

Differentially-private data and code is available under a [Creative Commons Zero](https://en.wikipedia.org/wiki/Creative_Commons_license#Zero_/_public_domain "en:Creative Commons license") license.

### Support

*   [Differential privacy at WMF homepage](https://meta.wikimedia.org/wiki/Differential_privacy "Differential privacy")
*   [DP experimentation repo](https://gitlab.wikimedia.org/htriedman/stat-spark3)
*   DP production repos:
    *   [Production DP aggregations](https://gitlab.wikimedia.org/repos/security/differential-privacy)
    *   [Production DP automation](https://gitlab.wikimedia.org/repos/data-engineering/airflow-dags)

![](https://meta.wikimedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)