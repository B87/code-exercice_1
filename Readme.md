# Code exercice 1

## Challenge 1

We use a third party application whose logs we would like to download regularly for further analysis

We can get data from this API for a particular hour (HH) with a curl statement like the following:

`curl –i https://api.localytics.com/v1/exports/analytics/logs/YYYY/MM/DD/HH`

We asume the curl always returns a 302 response with a redirect url.The redirect url points to a file in json format.

We need a Python program that should accept a date and extract the 24 files corresponding to that date data. The program should output 1 csv file (‘export.csv’) with all the data for the day.

The program should be able to parse into this csv any kind of json.

## Challenge 2

We have a table with the following fields:

`EventName | timestamp | CustomField_1 | CustomField_2 | CustomField_PageNum | CustomField_PublicationId`

Every time a user accesses a page an event with EventName = ‘EventRead’ is generated.

The time spent reading a page is the time between the event that identifies the access to this page and whatever the next event is.
We want to calculate the time spent reading each page of each publication from the information found in the above table. We would like to see a solution in plain SQL  and a solution in Python. The output should be the following table:

`CustomField_PublicationId | CustomField_PageNum  | ReadTime_sec`

For the SQL version consider you have the information in a table called ’Events’ and in Python consider you have it in a csv called ‘Events.csv’. In Python the result should be a csv called ‘results.csv’

## Challenge 3

The following table contains the reading times per page with the following fields:

`PublicationID | PageID | ReadTime_sec`

The following table contains the Article Ids contained in each page. One page contains only one article, but an article can span several pages.

`PublicationID | PageID | ArticleID`

The following table contains the article name for each Article ID

`ArticleID | ArticleName`

Provide the SQL query to obtain the Reading time for each Article name:

`PublicationID | ArticleName | ReadingTime_sec`
