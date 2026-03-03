As an Operator of **a program automatically consuming the content of the wikis** (robot), certain rules apply which depend on the type of content you’re accessing and how you access it. Bots that don't follow these guidelines may be rate-limited and informed of the reason, and pointed to ways to request higher quotas or exemptions.

Please note: while the guidelines apply to any bot that connects to our environment, rate limiting is not enforced on bots in Toolforge.

Bots that repeatedly try to get around these guidelines or rate limits, and/or threaten the stability of the sites may be blocked.

The following rules are an evolution of the previous version of this policy which was originally published in 2009. The updates include coverage of more systems, better defined limits, and clarifications to help any Bot Operator who acts in good faith to limit their impact on our systems.

Generally applicable rules
--------------------------

The following rules apply to any activity on our websites; rules in the following sections will be specific to sites/URLs instead.

1.  **Consider if dumps are more efficient than live requests.** Check if you can use [Wikimedia Dumps](https://meta.wikimedia.org/wiki/Data_dumps "meta:Data dumps") or other forms of offline collection of our data instead of making live requests. If dumps are a viable option for your use case it will reduce the strain on our very limited resources and make your life easier.
2.  **Accurately identify your User-Agent.** Always identify your bot clearly via its User-Agent HTTP header by following the [Wikimedia Foundation User-Agent Policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy "foundation:Policy:Wikimedia Foundation User-Agent Policy").
3.  When you are making a significant number of requests **avoid user-agent impersonation** and possible collateral damage blocks by either:
    1.  **Provide a URL** where we can download a JSON formatted list of [CIDRs](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing "w:Classless Inter-Domain Routing") from which your requests will originate. See the "[what to do if the limits are too strict for me](#What_to_do_if_these_limits_are_too_strict_for_me?)" section.
    2.  **Authenticate your requests** using an on-wiki account when you are making API requests. An [OAuth 2.0 access token](https://www.mediawiki.org/wiki/OAuth/For_Developers#OAuth_2 "mw:OAuth/For Developers") is the preferred authentication method, but session cookies are also supported.
4.  **Honor Robots.txt.** Honor every directive in our [robots.txt](https://en.wikipedia.org/wiki/Robots.txt "w:Robots.txt") file.
5.  **Default to gzip.** Always request content with an `Accept-Encoding: gzip` HTTP header to reduce bandwidth usage. This is not necessary when you are directly requesting media files (_i.e._ images or video) which are already in a compressed format.
6.  **Respect our HTTP status codes.** When we reply with a [429 Too Many Requests](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#429 "w:List of HTTP status codes") status code respect the delay specified by the [Retry-After](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Response_fields "w:List of HTTP header fields") header sent with the response.
7.  **Cached interfaces are preferred and more efficient.** If you need the HTML content of pages use either the `/wiki/Article_name` URL or the corresponding [Wikimedia REST API](https://www.mediawiki.org/wiki/Wikimedia_REST_API "mw:Wikimedia REST API") `/api/rest_v1/page/html/Article_name` endpoint. These requests will be cheaper for us and faster for you because they can be cached in our [content delivery network](https://wikitech.wikimedia.org/wiki/CDN "CDN"). More information about these request methods can be found below.

Website rules
-------------

_i.e._ https://en.wikipedia.org/wiki/Main\_Page

1.  Always crawl the website via the `/wiki/Article_name` URLs, with **no query parameters**. This will ensure that if the content is CDN-cached, you’ll get a faster response allowing you to crawl the site faster and more efficiently.
2.  If you're making read requests, do not emulate a browser - do not store cookies or execute javascript, unless you're not crawling the sites at high volume (so, more than 5 requests per second).
3.  Assuming you are following all of our best practices ideally, still ensure that the maximum concurrent number of requests is fewer than 10 overall, and keep the average requests per second below 20.
4.  Avoid accessing content that is not current, or via non-canonical URLs: do not crawl the site using the `oldId` or `curid` parameters, and only use the `/wiki/Title` format URLs.

API rules
---------

All activity is subject to cross-API rate limiting that is global for all Wikimedia sites. See the [documentation on rate limits](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits "mw:Wikimedia APIs/Rate limits") for full details and best practices. In summary:

1.  API rate limits take into account client identity to determine the level of access.
2.  Stronger forms of identification result in a higher limit, such running in Wikimedia Cloud Services (WMCS) or authenticating requests.
3.  The highest limits require running in WMCS, community bot approval, or being well-known to the Wikimedia Foundation.
4.  Further limits or additional best practices may apply to specific APIs.

### REST API rules

_i.e._ https://en.wikipedia.org/api/…

1.  You can use [this interface](https://wikitech.wikimedia.org/api/rest_v1/#/Page%20content) to fetch the HTML content of the pages, or their summary.
2.  If unauthenticated, keep the concurrency of your requests to 3 at a time, and below 5 requests per second overall.
3.  If authenticated, you can raise the number of requests per second to 10.
4.  Avoid accessing content that is not current, so avoid requesting a specific revision in your URL.

### Action API rules

_i.e._ https://en.wikipedia.org/w/api.php?…

1.  Avoid using the action API for HTML content of pages. Use the website and/or the REST API instead.
2.  If unauthenticated, keep the concurrency of your requests to 1 at a time, and below 5 requests per second overall.
3.  If authenticated, you can raise the concurrency to 3 overall, and the number of requests per second to 10.
4.  Avoid using expensive API endpoints: if your request takes more than 1 second to serve, please wait 5 seconds before making another request.
5.  Where supported, use batch requests.

### Media API rules

_i.e._ https://upload.wikimedia.org/…

1.  Always keep a total concurrency of at most 2, and limit your total download speed to 25 Mbps (as measured over 10 second intervals).
2.  Only use originals or one of our standard thumbnail sizes, which you can see in [mediawiki.org](https://www.mediawiki.org/wiki/Common_thumbnail_sizes "mw:Common thumbnail sizes").
3.  Prefer thumbnails to downloading of originals if possible.

Rules for other resources
-------------------------

_i.e._ Gerrit, GitLab, Phabricator, and other wikimedia.org services.

1.  Always keep a total concurrency of at most 1, and use a delay between requests of at least 1 second.
2.  Pause crawling for at least 15 minutes if you receive a 5xx status code.

What to do if these limits are too strict for me?
-------------------------------------------------

These limits are not per-domain but global for all Wikimedia properties, with an exception for community projects of the kind which would be eligible to run in Wikimedia Foundation’s hosted infrastructure (Wikimedia Cloud Services offerings).

Specifically, bots running in Toolforge and in any other Wikimedia Cloud Services offering are explicitly exempted from such limits. We will still reserve the right to temporarily rate-limit or block individual bots that might be compromising the stability of the websites.

Community bots that need a higher volume of API requests should run in WMCS or authenticate and request the bot flag from your local wiki community. Community-approved bots get higher rate limits.

If you are an external entity and you need a higher volume of requests, you should use [Wikimedia Enterprise APIs](https://meta.wikimedia.org/wiki/Wikimedia_Enterprise#Access "metawiki:Wikimedia Enterprise") instead. This is the preferred choice for commercial, high-volume users of the APIs.

Bot operators who are unsure how to get the access they need can contact the Wikimedia Foundation at [bot-traffic@wikimedia.org](mailto:bot-traffic@wikimedia.org).