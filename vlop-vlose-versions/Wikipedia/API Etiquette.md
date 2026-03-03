This page contains the best practices that should be followed when using the Action API.

Behaviour
---------

### Request limit

There is no hard speed limit on read requests, but be considerate and try not to take a site down. Most system administrators reserve the right to unceremoniously block you if you do endanger the stability of their site.

Making your requests in series rather than in parallel, by waiting for one request to finish before sending a new request, should result in a safe request rate. It is also recommended that you ask for multiple items in one request by:

*   Using the pipe character (`|`) whenever possible e.g. `titles=PageA|PageB|PageC`, instead of making a new request for each title.
*   Using a [generator](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Query#Generators "Special:MyLanguage/API:Query") [](https://www.mediawiki.org/wiki/API:Query#Generators "API:Query")instead of making a request for each result from another request.

*   Use GZip compression when making API calls by setting `Accept-Encoding: gzip` to reduce bandwidth usage.

Requests which make edits, modify state or otherwise are not read-only requests, _are_ subject to [rate limiting](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Rate_limits "Special:MyLanguage/Manual:Rate limits") [](https://www.mediawiki.org/wiki/Manual:Rate_limits "Manual:Rate limits"). The exact rate limit being applied might depend on the type of action, your user rights and the configuration of the website you are making the request to. The limits that apply to you can be determined by accessing the action=query&meta=userinfo&uiprop=ratelimits API endpoint.

**[api.php?action=query&format=json&meta=userinfo&uiprop=ratelimits](https://en.wikipedia.org/w/api.php?action=query&format=json&meta=userinfo&uiprop=ratelimits)** [\[try in ApiSandbox\]](https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&format=json&meta=userinfo&uiprop=ratelimits)

When you hit the request rate limit you will receive a [API error response](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Errors_and_warnings "Special:MyLanguage/API:Errors and warnings") [](https://www.mediawiki.org/wiki/API:Errors_and_warnings "API:Errors and warnings")with the error code `ratelimited`. When you encounter this error, you may retry that request, however you should increase the time between subsequent requests. A common strategy for this is [Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff "w:Exponential backoff").

### Parsing of revisions

While it is possible to query for results from a specific revision number using the `revid` parameter, this is an expensive operation for the servers. To retrieve a specific revision use the `oldid` parameter. For example:

**[api.php?action=parse&format=json&prop=images&oldid=254862759](https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=images&oldid=254862759)** [\[try in ApiSandbox\]](https://en.wikipedia.org/wiki/Special:ApiSandbox#action=parse&format=json&prop=images&oldid=254862759)

### The maxlag parameter

If your task is not interactive, i.e. a user is not waiting for the result, you should use the `maxlag` parameter. The value of the `maxlag` parameter should be an integer number of seconds. For example:

**[api.php?action=query&format=json&titles=Main%20Page&maxlag=1](https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Main%20Page&maxlag=1)** [\[try in ApiSandbox\]](https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&format=json&titles=Main%20Page&maxlag=1)

This will prevent your task from running when the load on the servers is high. Higher values mean more aggressive behaviour, lower values are nicer.

See [Manual:Maxlag parameter](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Maxlag_parameter "Special:MyLanguage/Manual:Maxlag parameter") [](https://www.mediawiki.org/wiki/Manual:Maxlag_parameter "Manual:Maxlag parameter")for more details.

### The User-Agent header

It is best practice to set a descriptive User-Agent header. To do so, use `User-Agent: clientname/version (contact information e.g. username, email) framework/version...`. For example in PHP:

ini\_set('user\_agent', 'MyCoolTool/1.1 (https://example.org/MyCoolTool/; MyCoolTool@example.org) UsedBaseLibrary/1.4');

Do not simply copy the user-agent of a popular web browser. This ensures that if a problem does arise it is easy to track down where it originates.

If you are calling the API from browser-based JavaScript, you may not be able to influence the `User-Agent` header, depending on the browser. To work around this, use the `Api-User-Agent` header.

### Data formats

All new API users [should use JSON](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Data_formats#Output "Special:MyLanguage/API:Data formats") [](https://www.mediawiki.org/wiki/API:Data_formats#Output "API:Data formats"). See [API:Data formats](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Data_formats "Special:MyLanguage/API:Data formats") [](https://www.mediawiki.org/wiki/API:Data_formats "API:Data formats")for more details.

### Caching

If your requests obtain data that can be cached for a while, you should take steps to cache it, so you don't request the same data over and over again. Some clients may be able to cache data themselves, but for others (particularly JavaScript clients), this is not possible.

### POST requests

Whenever you're reading data from the web service API, you should try to use GET requests if possible, not POST, as the latter are not cacheable and, in [multi-datacenter](https://wikitech.wikimedia.org/wiki/Performance/Multi-DC_MediaWiki "wikitech:Performance/Multi-DC MediaWiki") configurations (including Wikimedia sites), may go to a farther data center.

In exceptional cases where you really need to use POST for a read request, such as calling `[action=parse](https://www.mediawiki.org/wiki/Special:MyLanguage/API:Parsing_wikitext "Special:MyLanguage/API:Parsing wikitext") [](https://www.mediawiki.org/wiki/API:Parsing_wikitext "API:Parsing wikitext")` with a long string of wikitext, consider setting the `Promise-Non-Write-API-Action: true` header. This helps ensure that your POST request is processed by an application server in the closest data center, if appropriate. There is no need to set this header for GET requests, and neither should it be set when making [cross-wiki requests](https://www.mediawiki.org/wiki/Special:MyLanguage/Extension:CentralAuth/API "Special:MyLanguage/Extension:CentralAuth/API") [](https://www.mediawiki.org/wiki/Extension:CentralAuth/API "Extension:CentralAuth/API")within a wiki family using CentralAuth; see [T91820](https://phabricator.wikimedia.org/T91820 "phabricator:T91820").

Guidelines for Wikimedia wikis
------------------------------

In addition to the best practices described above, the following guidelines apply to using the Action API to access Wikimedia wikis. See also [the official guidelines about API usage](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Wikimedia_Foundation_API_Usage_Guidelines "foundation:Special:MyLanguage/Policy:Wikimedia Foundation API Usage Guidelines") on Wikimedia Foundation Governance wiki.

### User-Agent policy

API requests to Wikimedia wikis must include a meaningful User-Agent header. See [User-Agent policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:User-Agent_policy "foundation:Special:MyLanguage/Policy:User-Agent policy") for more details.

### Rate limits

In addition to [rate limits](https://www.mediawiki.org/wiki/Special:MyLanguage/Manual:Rate_limits "Special:MyLanguage/Manual:Rate limits") [](https://www.mediawiki.org/wiki/Manual:Rate_limits "Manual:Rate limits")based on user actions, API requests to Wikimedia wiki are subject to [API rate limits](https://www.mediawiki.org/wiki/Special:MyLanguage/Wikimedia_APIs/Rate_limits "Special:MyLanguage/Wikimedia APIs/Rate limits") [](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits "Wikimedia APIs/Rate limits").

### Performance

Downloading data in bulk is not always extremely efficient using the Action API. On Wikimedia wikis, there are faster ways to get data in bulk, see [m:Research:Data](https://meta.wikimedia.org/wiki/Research:Data "m:Research:Data") and [wikitech:Portal:Data Services](https://wikitech.wikimedia.org/wiki/Portal:Data_Services "wikitech:Portal:Data Services") for more details.