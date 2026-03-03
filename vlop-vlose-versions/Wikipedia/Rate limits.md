Manual:Rate limits
==================

MediaWiki applies **rate limits** to some user actions, particularly ones that modify content or require a lot of resources.

Configuration
-------------

A rate limit can be applied for any [user right](https://www.mediawiki.org/wiki/Help:User_rights_and_groups "Help:User rights and groups"). The actual values of the rate limits can vary per wiki configuration via these parameters:

*   [$wgRateLimits](https://www.mediawiki.org/wiki/Manual:$wgRateLimits "Manual:$wgRateLimits")
*   [$wgAccountCreationThrottle](https://www.mediawiki.org/wiki/Manual:$wgAccountCreationThrottle "Manual:$wgAccountCreationThrottle")
*   [$wgPasswordAttemptThrottle](https://www.mediawiki.org/wiki/Manual:$wgPasswordAttemptThrottle "Manual:$wgPasswordAttemptThrottle")

If an account has the [noratelimit right](https://www.mediawiki.org/wiki/Manual:User_rights#noratelimit "Manual:User rights") (such as an account in the Bot or Admin group), these rate limits don't apply. To see the limits that apply to you, use the [user info API module](https://www.mediawiki.org/wiki/API:Userinfo "API:Userinfo"), for example:

Bots using OAuth
----------------

To bypass configured rate limits using the noratelimit right, a bot that uses [OAuth](https://www.mediawiki.org/wiki/OAuth/For_Developers "OAuth/For Developers") must ensure that its OAuth client includes the highvolume grant.

Concurrency limits
------------------

Some actions also have a maximum number of requests that can happen at the same time. These concurrency limits are controlled by [$wgPoolCounterConf](https://www.mediawiki.org/wiki/Manual:$wgPoolCounterConf "Manual:$wgPoolCounterConf") and are disabled by default.

Limits
------

Limits apply only to actions that users are allowed to perform based on their user rights. Here are some examples of limits on common actions and how they are applied on Wikimedia wikis. For a complete list of default limits in MediaWiki, see [$wgRateLimits](https://www.mediawiki.org/wiki/Manual:$wgRateLimits#Default_value "Manual:$wgRateLimits").

| Action | Minimal user right | MediaWiki default ratelimits | Wikimedia wikis with custom ratelimits[\[1\]](#cite_note-1) |
| --- | --- | --- | --- |
| edit | `*` (all) | 8 per minute | *   Turkish Wikipedia: lower limit for new and logged-out users<br>*   Wikimedia Commons: higher limits for all users, including extra high limits for trusted user groups |
| `autoconfirmed` | 90 per minute |
| move | `*` (all) | 2 per 2 minutes | *   Higher limits for trusted groups: Wikimedia Commons, Arabic Wikipedia, English Wikipedia, English Wikibooks, Korea Wikipedia, and Ukrainian Wikipedia |
| `autoconfirmed` | 8 per minute |
| upload | `*` (all) | 8 per minute | *   Wikimedia Commons: higher limits for trusted user groups |
| rollback | `*` (all) | 5 per 2 minutes | None |
| `autoconfirmed` | 10 per minute | *   All Wikimedia wikis: 100 per minute |

### Wikimedia Commons

The following rate limits apply to file uploads on Wikimedia Commons:

|     |     |     |
| --- | --- | --- |
| Group | Minimal condition | Ratelimit |
| Uploads rights |
| `*` (all) | Anonymous IP | 0   |
| `user` | Have an account | 380 per 4320 sec. |
| `[autoconfirmed](https://commons.wikimedia.org/wiki/Autoconfirmed_users "commons:Autoconfirmed users")` | 4+ days old account | 380 per 4320 sec. |
| `autopatrolled` | [On request](https://commons.wikimedia.org/wiki/Commons:Requests_for_rights "commons:Commons:Requests for rights") | 999 per 1 sec. |
| `patroller` | On request | 999 per 1 sec. |
| `image-reviewer` | On request | 999 per 1 sec. |
| 4320 sec. = 72 mins. |     |     |

See also
--------

*   [Rate limits for Wikimedia APIs](https://www.mediawiki.org/wiki/Wikimedia_APIs/Rate_limits "Wikimedia APIs/Rate limits")
*   [Best practices for using the Action API on Wikimedia wikis](https://www.mediawiki.org/wiki/API:Etiquette "API:Etiquette")
*   [Technical overview of rate limiting in Wikimedia infrastructure](https://wikitech.wikimedia.org/wiki/External_request_limits "wikitech:External request limits")

References
----------

1.  [↑](#cite_ref-1) See `wgRateLimits` in [InitialiseSettings.php](https://gerrit.wikimedia.org/r/plugins/gitiles/operations/mediawiki-config/%2B/master/wmf-config/InitialiseSettings.php "gerrit:plugins/gitiles/operations/mediawiki-config/+/master/wmf-config/InitialiseSettings.php")

![](https://www.mediawiki.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)