--- USING POSTGRESQL 9.6.15

CREATE TABLE public.Publication_Id_Read_Time("CustomField_PublicationId" INT PRIMARY KEY, "CustomField_PageNum" TEXT, "ReadTime_sec" INT);

CREATE TABLE public.Publication_Article_Rel("Id" SERIAL PRIMARY KEY, "PublicationID" INT, "PageID" INT, "ArticleID" INT);

CREATE TABLE public.Article_dim("ArticleID" INT PRIMARY KEY, "ArticleName" TEXT);

--- DROP TABLE public.Events
--- DROP TABLE public.Publication_Id_Read_Time
