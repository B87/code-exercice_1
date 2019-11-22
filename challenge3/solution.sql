--- USING POSTGRESQL 9.6.15

SELECT t2."PublicationID" , t3."ArticleName", SUM(t1."ReadTime_sec") as "ReadingTime_sec"
FROM public.publication_id_read_time as t1
INNER JOIN public.publication_article_rel as t2 
ON t1."CustomField_PublicationId"  = t2."PublicationID" AND t1."CustomField_PageNum"::INT = t2."PageID"
INNER JOIN public.article_dim as t3
ON t2."ArticleID" = t3."ArticleID"
GROUP BY t2."PublicationID", t3."ArticleName"

--- RESULT USING data_init.sql tables
-- 1 | "The best article ever" | "180"
-- 1 | "This one is not that good" | "300"