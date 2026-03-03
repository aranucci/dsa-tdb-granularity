 Toggle the table of contents

Legal:Wikimedia Foundation EU Compliance/DSA Article 40(4) Data Catalogue
=========================================================================

From Wikimedia Foundation Governance Wiki

< [Legal:Wikimedia Foundation EU Compliance](https://foundation.wikimedia.org/wiki/Legal:Wikimedia_Foundation_EU_Compliance "Legal:Wikimedia Foundation EU Compliance")

About
-----

This page is the Data Catalogue relating to Wikipedia, for the purposes of [EU DSA Article 40(4)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R2065#art_40) and Article 6(4) of the [EU Delegated Act on Research Access, C(2025)4340](https://digital-strategy.ec.europa.eu/en/library/delegated-act-data-access-under-digital-services-act-dsa) (“DARA”).  These provisions govern access by vetted researchers to nonpublic data for the sole purpose of conducting research that contributes to the detection, identification and understanding of systemic risks in the EU/EEA and how the adequacy, efficiency and impacts of those risks’ mitigations, for Wikipedia.

Contact details for the Wikimedia Foundation’s designated point of contact for these purposes is eu-dsa-art-40-4-contact![@](//upload.wikimedia.org/wikipedia/commons/thumb/8/88/At_sign.svg/20px-At_sign.svg.png)wikimedia![.](//upload.wikimedia.org/wikipedia/commons/thumb/4/48/Dot.svg/20px-Dot.svg.png)org.  The EU’s Data Access Portal and help pages can be found at [https://data-access.dsa.ec.europa.eu/home](https://data-access.dsa.ec.europa.eu/home) .

**The Wikimedia Foundation prides itself on the very high degree of open data and tooling already available for researchers, and we also welcome voluntary collaborations with our own Research team for more advanced projects.**

**Therefore before researchers go through the process set up by the DSA and DARA, we would strongly encourage you to examine the publicly available [data](https://meta.wikimedia.org/wiki/Research:Data "metawiki:Research:Data"), or [contact](https://research.wikimedia.org/contact.html) the Wikimedia Foundation’s Research team.  If your research concerns artificial intelligence or machine learning models, we are pleased to say that at the time of writing, WMF has made all training datasets that are available to the organization publicly available. The datasets are linked from the corresponding [model cards](https://meta.wikimedia.org/wiki/Machine_learning_models#Production_models "metawiki:Machine learning models").**

**If you do make a data access request through the DSA Art. 40(4)/DARA procedure, please ensure that it is Wikipedia- and EU- specific. We further ask that you limit your requests to support research questions into systemic risks, as envisaged by DSA Art. 40(4).**

**We further encourage the following:**

1.  **Create a Meta:Research page about your project, as described here: [https://meta.wikimedia.org/wiki/Research:Projects](https://meta.wikimedia.org/wiki/Research:Projects) ;**
2.  **Upon completion of your research project, we encourage you to publish your output as described in [https://foundation.wikimedia.org/wiki/Policy:Wikimedia\_Foundation\_Open\_Access\_Policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_Open_Access_Policy)**
3.  **Familiarize yourselves with our guidance around Research and Privacy on Wikipedia: [https://osf.io/preprints/osf/uyxnf\_v1](https://osf.io/preprints/osf/uyxnf_v1)**
4.  **Join the public Wikimedia research mailing list: [https://lists.wikimedia.org/postorius/lists/wiki-research-l.lists.wikimedia.org/](https://lists.wikimedia.org/postorius/lists/wiki-research-l.lists.wikimedia.org/)**

Data Catalogue
--------------

### MediaWiki Content History

When a MediaWiki page is edited (for example, on Wikipedia), the previous version(s) of that page (its “revisions”) can normally still be viewed, allowing the page’s evolution (e.g., its moderation) to be publicly audited over time. Under special circumstances, according to policies often [documented](https://www.wikidata.org/wiki/Q4656800 "wikidata:Q4656800") for the specific Wikipedia language, Wikipedia communities may disable access to (i.e., “remove”; sometimes - depending on the circumstances - also called “revdel”, “oversight” or “suppress”) specific revisions in the page history.  This ensures that neither the current version of the page _nor_ the Page History function are publicly disseminating inappropriate content. For example, if a young person recklessly posts their own telephone number to a page, it would be conventional for other users to not only remove it from the page, but then also remove the older page revisions that contain it . The Wikimedia Foundation, as the website host/platform operator, may also do this, pursuant to our Office Actions policy.

The functionality allowing this is called [RevisionDelete](https://www.mediawiki.org/wiki/Help:RevisionDelete "mw:Help:RevisionDelete"). Once a revision is removed, it is neither generally visible on Wikipedia, nor included in subsequent (post-removal) public Wikipedia content history XML [dumps](https://dumps.wikimedia.org/).

However, the private copy of [MediaWiki Content History](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Content/Mediawiki_content_history_v1 "wikitech:Data Platform/Data Lake/Content/Mediawiki content history v1") includes the majority of the removed information. This includes the removed revision, together with the  corresponding editor username and the edit summary they provided when originally posting the edit which created that revision.

#### Data structure and metadata

Please refer to the [public documentation](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Content/Mediawiki_content_history_v1 "wikitech:Data Platform/Data Lake/Content/Mediawiki content history v1") for the schema.

#### Suggested access modalities

For privacy and confidentiality reasons, direct researcher access might not be possible. We request researchers, so far as possible, to supply the exact query to be run.

#### Additional remarks

1.  MediaWiki Content History data is not guaranteed to contain all removed revisions. It is generated from an event-based, [eventually consistent system](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Content/Mediawiki_content_history_v1#Pipeline "wikitech:Data Platform/Data Lake/Content/Mediawiki content history v1") that retrieves revision information from the public [Wikipedia APIs](https://www.mediawiki.org/wiki/API:Action_API "mw:API:Action API") after a revision has been created. Depending on nondeterministic factors such as event ordering or transient infrastructure errors, a revision may be processed before or after it has been removed, and in the latter case, its contents will not be preserved in the MediaWiki Content History private data.
2.  MediaWiki Content History includes a large amount of data that is already publicly available. Researchers are invited to rely as far as possible on that public data, and should not request access to it using the DSA Article 40(4) mechanism.

### Editors Daily

The location from which an edit to Wikipedia was made, whether exact or approximate, is not publicly available. [Editors Daily](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Edits/Geoeditors#Editors_daily "wikitech:Data Platform/Data Lake/Edits/Geoeditors") is an internal dataset, updated monthly, that contains this more sensitive individual information. The location in this dataset is estimated via IP-based geolocation.

#### Data structure and metadata

Please see the [public documentation](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Edits/Geoeditors#Editors_daily "wikitech:Data Platform/Data Lake/Edits/Geoeditors") for the schema. In line with our data retention policy, Editors Daily may only contain information for the past two months, as historical information is continuously removed.

#### Suggested access modalities

For privacy and confidentiality reasons, direct researcher access might not be possible. We request researchers, so far as possible, to supply the exact query to be run.

#### Additional remarks

1.  The [Geoeditors](https://dumps.wikimedia.org/other/geoeditors/readme.html) public data dump offers monthly aggregate editor activity per country.
2.  Historical editor activity information, not including geolocation, is available in the [MediaWiki History](https://wikitech.wikimedia.org/wiki/Data_Platform/Data_Lake/Edits/MediaWiki_history_dumps "wikitech:Data Platform/Data Lake/Edits/MediaWiki history dumps") public dataset.

### Zendesk Support Ticket data

People contact us for help (e.g. to report illegal content under DSA Article 16), and authorities contact us (for DSA Article 9 and 10 purposes), by emailing us. We use the Zendesk Support ticketing system to handle these emails; each new email chain is created as a “ticket” on our system where it can be triaged, handled and tagged. Data about these tickets is used to compile our periodic Transparency Reports.

#### Data structure and metadata

Please refer to [https://support.zendesk.com/hc/en-us/articles/4408827693594-Metrics-and-attributes-for-Zendesk-Support](https://support.zendesk.com/hc/en-us/articles/4408827693594-Metrics-and-attributes-for-Zendesk-Support)

As noted above, we have different reporting channels for different types of matters; see in particular those mentioned [on this page](https://foundation.wikimedia.org/wiki/Legal:Wikimedia_Foundation_EU_Compliance#Contacting_the_Wikimedia_Foundation_with_legal_complaints_and_questions "Legal:Wikimedia Foundation EU Compliance").

Tickets may also have custom fields (which vary according to reporting channel/ticket purpose, and may evolve over time); please enquire in order to confirm what relevant ticket fields may be available for your research.

#### Suggested access modalities

It is possible to run queries and export aggregate statistics using the Zendesk Explore tool, through the creation of custom “reports”.  

The documentation here explains what the Explore tool can do: [https://support.zendesk.com/hc/en-us/search?content\_tags=01H41B6Y9VDNEGDFSDQZGESE9F&amp%3Butf8=%E2%9C%93](https://support.zendesk.com/hc/en-us/search?content_tags=01H41B6Y9VDNEGDFSDQZGESE9F&amp%3Butf8=%E2%9C%93) .

For privacy/confidentiality and licensing limitation reasons, direct researcher access to the Zendesk Explore tool might not be possible. Where reasonable, and subject to confirmation, the Wikimedia Foundation may instead be able to generate Zendesk Explore reports (i.e., run Explore queries) on researchers’ behalf. Researchers should so far as possible supply the exact query to be run; see [https://support.zendesk.com/hc/en-us/articles/4408845804314-Formula-writing-resources](https://support.zendesk.com/hc/en-us/articles/4408845804314-Formula-writing-resources)

#### Additional remarks

1.  The Wikimedia Foundation already produces detailed 6-monthly reports containing these sorts of statistics: see [https://wikimediafoundation.org/who-we-are/transparency/](https://wikimediafoundation.org/who-we-are/transparency/) . Their production includes a manual review/cleanup exercise to ensure tickets handled during the relevant reporting period (the previous 6 months) are appropriately tagged/classified and therefore reported accordingly. Tickets that have not yet been through that exercise may have less reliable tagging. Researchers are encouraged to confine their analysis to tickets that have been through this review process. For example, if at the time of your research, our most recent published Transparency Report was for the January-June 2025 period, we advise you to limit your research to tickets that were handled up to June 30, 2025.
2.  Please do not request access to sensitive data e.g. (i) the content of freetext fields (including the content of tickets themselves), or (ii) data identifying the correspondents and handlers of a ticket (e.g., who submitted it, and which WMF staff members handled it).
3.  To achieve EU specificity, we recommend limiting analysis to tickets that have an EU Member State listed as the relevant country (if we have been able to determine/estimate this).

Disclaimer
==========

The Wikimedia Foundation does not warrant the constant availability or correctness of data listed on this page or of the good functioning of its access modalities, nor does the Foundation make any representations concerning the lawfulness of third parties’ access to it as a matter of applicable laws around the world. The [Wikimedia Foundation Terms of Use](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use "Policy:Terms of Use") apply. Please note, in particular (but without limitation), the ToU’s "Disclaimers" and "Limitation of Liability” sections. The Wikimedia Foundation is a non-profit organization. All costs of access (such as the purchasing of additional licenses to use non-free tools) are to be borne by those demanding the access.

![](https://foundation.wikimedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

Retrieved from "[https://foundation.wikimedia.org/w/index.php?title=Legal:Wikimedia\_Foundation\_EU\_Compliance/DSA\_Article\_40(4)\_Data\_Catalogue&oldid=530404](https://foundation.wikimedia.org/w/index.php?title=Legal:Wikimedia_Foundation_EU_Compliance/DSA_Article_40\(4\)_Data_Catalogue&oldid=530404)"