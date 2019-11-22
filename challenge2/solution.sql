--- USING POSTGRESQL 9.6.15

INSERT INTO public.Publication_Id_Read_Time (
    SELECT final."CustomField_PublicationId", final."CustomField_PageNum", 
                    ((DATE_PART('day', end_ts - init_ts) * 24 + 
                    DATE_PART('hour', end_ts- init_ts)) * 60 +
                    DATE_PART('minute', end_ts - init_ts)) * 60 +
                    DATE_PART('second', end_ts - init_ts) AS "ReadTime_sec"
    FROM(
        SELECT t1."EventName", t1."CustomField_PublicationId", t1."CustomField_PageNum", t1."timestamp" as init_ts, t2."timestamp" as end_ts
        FROM (
            SELECT "EventName", "CustomField_PublicationId", "CustomField_PageNum", "timestamp",
            ROW_NUMBER() OVER(order by "timestamp" DESC) as row_num
            FROM public.events
            ) as t1
        INNER JOIN (
            SELECT "CustomField_PublicationId", "CustomField_PageNum", "timestamp",
            ROW_NUMBER() OVER(order by "timestamp" DESC) as row_num
            FROM public.events) as t2 
        ON t1.row_num = t2.row_num+1
        WHERE t1."EventName" = 'EventRead'
    ) as final
)

