Ads transparency
----------------

For transparency information and requests for X Political Ads, please see the [X Political Content Policy](https://business.twitter.com/en/help/ads-policies/ads-content-policies/political-content.html).

X is also providing an archived version of Ads Transparency Center (ATC) data for all Political ads that ran between May 24, 2018 and November 22, 2019 and Issue ads that ran between August 08, 2018 and November 22, 2019.

###### **Political advertising:**

You can download an archive of political ads that ran from May 24, 2018 to November 22, 2019.

[Download .TXT](https://business.twitter.com/content/dam/business-twitter/help/ads-transparency-archive/political.txt)

###### **Issue advertising (US only):**

You can download an archive of issue ads that ran from August 08, 2018 to November 22, 2019. 

[Download .TXT](https://business.twitter.com/content/dam/business-twitter/help/ads-transparency-archive/issue.txt)  

Finally, if you’re interested in learning more about any and all ads being served to you, you can download this information by clicking on Your Account in the Settings & Privacy tab.

###### **DSA Ad Transparency:**

In 2023, X launched an [Ads Transparency Center](https://ads.twitter.com/ads-repository?ref=BTC) for the Digital Services Act (DSA)--the X Ads Repository. 

For ads served in the EU, this Ad Transparency center includes the following: Advertiser, Funding Entity, the Advertiser’s Main Targeting Parameters for the advertisement, Impression, and Reach of Ad to provide transparency around advertisements on the platform. The Repository also provides information related to ads halted from running on the platform.

To access the repository, search for a particular account, country, and date range using the user interface or the API (instructions below). The request will generate a .csv file containing the information about the applicable advertisement(s). If the CSV file is blank, that may indicate no ads were served by that advertiser in the relevant time period. Note: to balance the privacy interests of natural persons affiliated with our advertisers, you may request the name of the person paying for a particular advertisement via credit card [here](https://docs.google.com/forms/d/e/1FAIpQLSfJ-YzAh36gBkfA2zgU4RfGRpCgqzA_y8XBYo-aIKP6UkVdXA/viewform).

**Steps for API Access to X Ads Repository:**

1.  Create a X developer account at the [X Developer portal](https://developer.twitter.com/en)
2.  Once you have an account, create an app and get a bearer token
3.  Then you will be able to make a curl request like the one below, which will provide you with an exportId:

      `curl 'https://api.twitter.com/graphql/e9OJa7fJKHtHftkNzcRkzw/CreateExportReportMutation' \   -H 'authorization: Bearer myToken' \   -H 'content-type: application/json' \   --data-raw '{"variables":{"user":"$userIdOfHandle","geoLocation":"$GeoCode","deliveryRange":{"start_date":"YYYY-MM-DD","end_date":"YYYY-MM-DD"}}}' \   --compressed`
    

4\. To look up the status of your request, you can make a curl request like the one below:

      `curl --location --request GET 'https://api.twitter.com/graphql/0RTLTx4DunPS6rVj-1cLCg/GetExportReportStatusQuery' \ --header 'Content-Type: application/json' \ --header 'Authorization: myToken' \ --data '{"query":"e9OJa7fJKHtHftkNzcRkzw","variables":{"exportId":"$myExportId"}}'`