Policy:Wikimedia Foundation API Usage Guidelines
================================================

Version 1.0
-----------

Date: August 26, 2024

### API

The Wikimedia Foundation enforces limits on operators' use of certain APIs, including but not limited to the MediaWiki Action API, the MediaWiki REST API, and the RESTBase API. Some of these limits are described below. The limits in this policy exist to maintain the performance and stability of our APIs, to promote the fair allocation of server resources, and to ensure that community members can use the APIs to further the free knowledge movement. You can read [frequently asked questions (FAQ) about this policy on Meta-Wiki](https://meta.wikimedia.org/wiki/Special:MyLanguage/API_Policy_Update_2024 "m:Special:MyLanguage/API Policy Update 2024").

In this policy, an "operator" is defined as any person who deploys software that causes our APIs to be called. In other words, the operator controls how often the APIs will be called. For example, this includes people who write on-wiki "gadgets" (even if they do not run them), and people who run bots (even if they did not write them). If you are reading this and looking for useful tips on how to use Wikimedia APIs, then this is probably you. If limits are imposed on an operator's use, they may not circumvent these limits. For example, operators are required to follow all instructions to delay or reduce the rate of further requests they receive in a response from an API. The specific numerical limits on any endpoint may change from time to time (for example, as current and predicted future load changes).

When using Wikimedia APIs, an operator must:

1.  Follow the [User-Agent policy and otherwise correctly label user agents](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:User-Agent_policy "Special:MyLanguage/Policy:User-Agent policy");
2.  Follow rate limiting requests (e.g., throttling notification) you may receive;
3.  Follow the requirements of the content licenses when republishing downloaded or cached data; and
4.  Follow the [robot policy](https://wikitech.wikimedia.org/wiki/Robot_policy "wikitech:Robot policy") if your software is automatically consuming content at a large scale.

When using Wikimedia APIs, an operator must not:

1.  Send traffic via concurrent connections to Wikimedia APIs resulting in a degradation of service to others or endangering the stability of the site;
2.  Request data at a high rate, far beyond common use cases, such as in spikes or in a manner intentionally meant to circumvent this policy;
3.  Spread Wikimedia API requests over multiple user agents to hide excessive use by a single operator; or
4.  Send high traffic originating from a single source or targeting a specific wiki/resource that ends up blocking others from using or accessing that resource.

Operators should use our APIs within the guidelines described in this policy and other technical documentation for each API. For the avoidance of doubt, the existence of this policy does not require members of the Wikimedia community to get prior permission from the Wikimedia Foundation before using the APIs in a manner consistent with this policy. Rather, we want people to be aware of uses that could result in disruption of their API usage, so operators know how to use Wikimedia's shared resources properly.

If your use case might fall outside the bounds of the policy described here and you would like to receive an exception or clarification, please submit a request to legal![@](//upload.wikimedia.org/wikipedia/commons/thumb/8/88/At_sign.svg/20px-At_sign.svg.png)wikimedia.org.

In situations where a limit may affect an operator's use, the Foundation may contact the operator to discuss the nature of the limits and any exceptions that may be needed. This is only possible if the operator's scripts adhere to the User-Agent policy and include up-to-date contact information.

The Foundation reserves the right to enforce this policy through blocking API access, disabling a program, or any similar action. Any choice to take or not take an enforcement action in a given situation will not be a waiver of any future action under this policy. In situations when this policy is enforced, any action taken can be lifted at the Foundation's discretion if the requesting party takes action to reduce the harm or unfairness caused. For example:

*   Reducing the rate of the API requests being sent;
*   Implementing an exponential backoff, where a throttling notification is sent to the operator, and in response, they slow down their rate of requests automatically; or
*   Following User-Agent naming conventions, as required in the [User-Agent policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:User-Agent_policy "Special:MyLanguage/Policy:User-Agent policy"), such that you can be contacted if usage becomes problematic.

### Sub-licensing

Operators (or those acting on their behalf) may not sublicense, lease, assign, or guarantee the availability or functionality of a Wikimedia Foundation-managed API to any third party. It is not permissible to implement an API client that white labels in a manner that obscures the identity of the ultimate service provider of the APIs (the Wikimedia Foundation). For the avoidance of doubt, this term does nothing to limit the use and republication of Wikimedia content in accordance with the free licenses that content is licensed under.

### Retiring APIs

The Foundation may retire or modify APIs. Operators that use APIs beyond the announced end-of-service date should expect the API to become unavailable without further warning or to experience significant degradation in performance. It is expected that operators update to use appropriate alternatives in advance of the end-of-service date. The Foundation may provide notice regarding updates and deprecations of APIs to the contact information that is provided per the User Agent requirements.

### Modifications to this policy

This policy is a public summary of some of the current limitations that the Wikimedia Foundation imposes on operators regarding their use of the Wikimedia APIs. As such, the Wikimedia Foundation may modify the policy in its discretion to more fully describe current limits or reflect future changes.

See also
--------

*   The [discussion on Meta-Wiki](https://meta.wikimedia.org/wiki/Special:MyLanguage/API_Policy_Update_2024 "m:Special:MyLanguage/API Policy Update 2024") (August-September 2023)

![](https://foundation.wikimedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)