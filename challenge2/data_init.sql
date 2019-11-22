--- USING POSTGRESQL 9.6.15

CREATE TABLE public.Events(
    "Id" INT PRIMARY KEY, "EventName" TEXT, "timestamp" TIMESTAMP, "CustomField_1" TEXT, "CustomField_2" TEXT, 
    "CustomField_PageNum" INT, "CustomField_PublicationId" INT);

INSERT INTO public.Events VALUES (1, 'EventRead', '10-11-2019T10:00:00', NULL, NULL, 1, 1);
INSERT INTO public.Events VALUES (2, 'EventRead', '10-11-2019T10:02:00', NULL, NULL, 2, 1);
INSERT INTO public.Events VALUES (3, 'OtherEvent', '10-11-2019T10:03:00', NULL, NULL, 2, 1);

CREATE TABLE public.Publication_Id_Read_Time("Id" SERIAL PRIMARY KEY, "CustomField_PublicationId" INT, "CustomField_PageNum" TEXT, "ReadTime_sec" INT);

--- DROP TABLE public.Events
--- DROP TABLE public.Publication_Id_Read_Time
