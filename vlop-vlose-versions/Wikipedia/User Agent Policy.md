As of February 15, 2010, Wikimedia sites require a **HTTP [User-Agent](https://en.wikipedia.org/wiki/User-Agent "en:User-Agent") header** for all requests. This was an operative decision made by the technical staff and was announced and discussed on the technical mailing list.[\[1\]](#cite_note-1)[\[2\]](#cite_note-2) The rationale is, that clients that do not send a User-Agent string are mostly ill behaved scripts that cause a lot of load on the servers, without benefiting the projects. User-Agent strings that begin with non-descriptive default values, such as `python-requests/x`, may also be blocked from Wikimedia sites (or parts of a website, e.g. `api.php`).

Requests (e.g. from browsers or scripts) that do not send a descriptive User-Agent header, may encounter an error message like this:

_Scripts should use an informative User-Agent string with contact information, or they may be blocked without notice._

Requests from disallowed user agents may instead encounter a less helpful error message like this:

_Our servers are currently experiencing a technical problem. Please try again in a few minutes._

This change is most likely to affect scripts (bots) accessing Wikimedia websites such as Wikipedia automatically, via api.php or otherwise, and command line programs.[\[3\]](#cite_note-3) If you run a bot, please send a User-Agent header identifying the bot with an identifier that isn't going to be confused with many other bots, and supplying some way of contacting you (e.g. a userpage on the local wiki, a userpage on a related wiki using interwiki linking syntax, a URI for a relevant external website, or an email address), e.g.:

User-Agent: CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org) generic-library/0.0

The generic format is `<client name>/<version> (<contact information>) <library/framework name>/<version> [<library name>/<version> ...]`. Parts that are not applicable can be omitted.

If you run an automated agent, please consider following the Internet-wide convention of including the string "bot" in the User-Agent string, in any combination of lowercase or uppercase letters. This is recognized by Wikimedia's systems, and used to classify traffic and provide more accurate statistics.

Do not copy a browser's user agent for your bot, as bot-like behavior with a browser's user agent will be assumed malicious.[\[4\]](#cite_note-4) Do not use generic agents such as "curl", "lwp", "Python-urllib", and so on. For large frameworks like pywikibot, there are so many users that just "pywikibot" is likely to be somewhat vague. Including detail about the specific task/script/etc would be a good idea, even if that detail is opaque to anyone besides the operator.[\[5\]](#cite_note-5)

Web browsers generally send a User-Agent string automatically; if you encounter the above error, please refer to your browser's manual to find out how to set the User-Agent string. Note that some plugins or proxies for privacy enhancement may suppress this header. However, for anonymous surfing, it is recommended to send a generic User-Agent string, instead of suppressing it or sending an empty string. Note that other features are much more likely to identify you to a website — if you are interested in protecting your privacy, visit the [Cover Your Tracks project](https://coveryourtracks.eff.org/).

Browser-based applications written in JavaScript are typically forced to send the same User-Agent header as the browser that hosts them. This is not a violation of policy, however such applications are encouraged to include the `Api-User-Agent` header to supply an appropriate agent.

As of 2015, Wikimedia sites do not reject all page views and API requests from clients that do not set a User-Agent header. As such, the requirement is not automatically enforced. Rather, it may be enforced in specific cases as needed.[\[6\]](#cite_note-6)

Code examples
-------------

On Wikimedia wikis, if you don't supply a `User-Agent` header, or you supply an empty or generic one, your request will fail with an HTTP 403 error. Other MediaWiki installations may have similar policies.

### JavaScript

If you are calling the API from browser-based JavaScript, you won't be able to influence the `User-Agent` header: the browser will use its own. To work around this, use the `Api-User-Agent` header:

// Using XMLHttpRequest
xhr.setRequestHeader( 'Api-User-Agent', 'Example/1.0' );

// Using jQuery
$.ajax( {
    url: 'https://example/...',
    data: ...,
    dataType: 'json',
    type: 'GET',
    headers: { 'Api-User-Agent': 'Example/1.0' },
} ).then( function ( data )  {
    // ..
} );

// Using mw.Api
var api \= new mw.Api( {
    userAgent: 'Example/1.0'
} );
api.get( ... ).then( function ( data ) {
    // ...
});

// Using Fetch
fetch( 'https://example/...', {
    method: 'GET',
    headers: new Headers( {
        'Api-User-Agent': 'Example/1.0'
    } )
} ).then( function ( response ) {
    return response.json();
} ).then( function ( data ) {
    // ...
});

### PHP

In PHP, you can identify your user-agent with code such as this:

ini\_set( 'user\_agent', 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)' );

### cURL

Or if you use [cURL](https://en.wikipedia.org/wiki/cURL "en:cURL"):

curl\_setopt( $curl, CURLOPT\_USERAGENT, 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)' );

### Python

In Python, you can use the [Requests](https://en.wikipedia.org/wiki/Requests_\(software\) "en:Requests (software)") library to set a header:

import requests

url \= 'https://example/...'
headers \= {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}

response \= requests.get(url, headers\=headers)

Or, if you want to use [SPARQLWrapper](https://sparqlwrapper.readthedocs.io/) like in [https://people.wikimedia.org/~bearloga/notes/wdqs-python.html](https://people.wikimedia.org/~bearloga/notes/wdqs-python.html):

from SPARQLWrapper import SPARQLWrapper, JSON

url \= 'https://example/...'
user\_agent \= 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'

sparql \= SPARQLWrapper(url, agent \= user\_agent )
results \= sparql.query()

Notes
-----

1.  [↑](#cite_ref-1) [The Wikitech-l February 2010 Archive by subject](https://lists.wikimedia.org/pipermail/wikitech-l/2010-February/thread.html#46764 "mailarchive:wikitech-l/2010-February/thread.html")
2.  [↑](#cite_ref-2) [User-Agent: - Wikitech-l - lists.wikimedia.org](https://lists.wikimedia.org/hyperkitty/list/wikitech-l@lists.wikimedia.org/thread/R4RU7XTBM5J3BTS6GGQW77NYS2E4WGLI/ "listarchive:list/wikitech-l@lists.wikimedia.org/thread/R4RU7XTBM5J3BTS6GGQW77NYS2E4WGLI/")
3.  [↑](#cite_ref-3) [API:FAQ - MediaWiki](https://www.mediawiki.org/wiki/Special:MyLanguage/API:FAQ "mw:Special:MyLanguage/API:FAQ")
4.  [↑](#cite_ref-4) [\[Wikitech-l\] User-Agent:](https://lists.wikimedia.org/pipermail/wikitech-l/2010-February/046783.html "mailarchive:wikitech-l/2010-February/046783.html")
5.  [↑](#cite_ref-5) [Clarification on what is needed for "identifying the bot" in bot user-agent?](https://lists.wikimedia.org/pipermail/mediawiki-api/2014-July/003308.html "mailarchive:mediawiki-api/2014-July/003308.html")
6.  [↑](#cite_ref-6) gmane.science.linguistics.wikipedia.technical/83870 ([deadlink](https://thread.gmane.org/gmane.science.linguistics.wikipedia.technical/83870/))