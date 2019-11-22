--- USING POSTGRESQL 9.6.15

CREATE TABLE public.Publication_Id_Read_Time("Id" SERIAL PRIMARY KEY, "CustomField_PublicationId" INT, "CustomField_PageNum" TEXT, "ReadTime_sec" INT);
INSERT INTO public.Publication_Id_Read_Time VALUES (1, 1, 1, 60);
INSERT INTO public.Publication_Id_Read_Time VALUES (2, 1, 2, 120);
INSERT INTO public.Publication_Id_Read_Time VALUES (3, 1, 3, 100);
INSERT INTO public.Publication_Id_Read_Time VALUES (4, 1, 4, 200);

CREATE TABLE public.Publication_Article_Rel("Id" SERIAL PRIMARY KEY, "PublicationID" INT, "PageID" INT, "ArticleID" INT);
INSERT INTO public.Publication_Article_Rel VALUES (1, 1, 1, 1);
INSERT INTO public.Publication_Article_Rel VALUES (2, 1, 2, 1);
INSERT INTO public.Publication_Article_Rel VALUES (3, 1, 3, 2);
INSERT INTO public.Publication_Article_Rel VALUES (4, 1, 4, 2);

CREATE TABLE public.Article_dim("ArticleID" INT PRIMARY KEY, "ArticleName" TEXT);
INSERT INTO public.Article_dim VALUES (1, 'The best article ever');
INSERT INTO public.Article_dim VALUES (2, 'This one is not that good');

--- DROP TABLE public.Publication_Id_Read_Time
--- DROP TABLE public.Publication_Article_Rel
--- DROP TABLE public.Article_dim