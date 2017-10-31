import psycopg2

def connectDB():
    try:
        conn = psycopg2.connect("dbname='CampusDirectory' user='postgres' host='localhost' password='pivot2017'")
    except:
        print ("I am unable to connect to the database")

    cur = conn.cursor()
    cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';""")
    rows = cur.fetchall()
    #all existing tables
    print ("\nShow me the databases:\n")
    for row in rows:
        print ("   ", row[0])

    cur.execute("""SELECT st_astext(geom) FROM public."centroids_buildings";""")
    rows = cur.fetchall()
    print ("\nShow me the CampusDirectory:\n")
    for row in rows:
        print ("   ", row)

    print("test")

connectDB()




'''
cur.execute("""SELECT * FROM public."CampusDirectory";""")
    rows = cur.fetchall()
    print ("\nShow me the CampusDirectory:\n")
    for row in rows:
        print ("   ", row)


DELETE FROM public."CampusDirectory";
UPDATE public."CampusDirectory" SET "adjAddress"=campus_address; (destination = source)

UPDATE public."CampusDirectory" SET campus_address = "adjAddress"




SELECT campus_address, building, building_room, "adjAddress"
	FROM public."CampusDirectory"
    WHERE campus_address LIKE '%Ford Hall%';


UPDATE public."CampusDirectory" SET
	building = substring("adjAddress", 1, strpos(',', "adjAddress")-1),
    building_room = substring("adjAddress", strpos(',', "adjAddress")+1)

1.
UPDATE public."CampusDirectory" SET
	building = "adjAddress",
    building_room=null
2.
COMMA SEPERATED - 'HALL, '
UPDATE public."CampusDirectory" SET
	building = substring("adjAddress", 0, position(',' in "adjAddress")),
    building_room = substring("adjAddress", position(',' in "adjAddress")+1, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Hall,%'
3.
NO COMMA SEP - 'HALL '
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Hall ' in "adjAddress")), ' Hall'),
    building_room = substring("adjAddress", position('Hall ' in "adjAddress")+5, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Hall %'
4. hall Annex - Stoddard Hall Annex, Level 1
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Hall Annex,' in "adjAddress")), ' Hall Annex'),
    building_room = substring("adjAddress", position('Hall Annex,' in "adjAddress")+11, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Hall Annex,%'
5. annex_= Tyler Annex 203
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Annex ' in "adjAddress")), ' Annex'),
    building_room = substring("adjAddress", position('Annex ' in "adjAddress")+5, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Annex %'
6.Green Street Classroom Annex, Rm 104A
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Classroom Annex,' in "adjAddress")), ' Classroom Annex'),
    building_room = substring("adjAddress", position('Classroom Annex,' in "adjAddress")+17, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Classroom Annex,%'

7.Tyler Annex, Rm 204
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Tyler Annex,' in "adjAddress")), ' Tyler Annex'),
    building_room = substring("adjAddress", position('Tyler Annex,' in "adjAddress")+12, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Tyler Annex,%'

8.18 Henshaw B3 203
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Henshaw ' in "adjAddress")), ' Henshaw'),
    building_room = substring("adjAddress", position('Henshaw ' in "adjAddress")+8, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Henshaw %'
9. 18 Henshaw, B3101
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Henshaw, ' in "adjAddress")), ' Henshaw'),
    building_room = substring("adjAddress", position('Henshaw, ' in "adjAddress")+9, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Henshaw, %'

10. Prospect Street, 105
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Street,' in "adjAddress")), ' Street'),
    building_room = substring("adjAddress", position('Street,' in "adjAddress")+7, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Street, %'

11. Young Library, YGB204
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Library,' in "adjAddress")), ' Library'),
    building_room = substring("adjAddress", position('Library,' in "adjAddress")+9, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Library,%'

12.Neilson Library 3/09
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Library ' in "adjAddress")), ' Library'),
    building_room = substring("adjAddress", position('Library ' in "adjAddress")+8, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Library %'

13. Alumnae Gym C/11
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Gym ' in "adjAddress")), ' Gym'),
    building_room = substring("adjAddress", position('Gym ' in "adjAddress")+4, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Gym %'
14.Campus Center 106
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Campus Center ' in "adjAddress")), ' Campus Center'),
    building_room = substring("adjAddress", position('Campus Center ' in "adjAddress")+13, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Campus Center %'

15.Campus Center, 106
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Campus Center,' in "adjAddress")), ' Campus Center'),
    building_room = substring("adjAddress", position('Campus Center,' in "adjAddress")+14, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Campus Center,%'

16. Mendenhall CPA T13A
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Mendenhall CPA ' in "adjAddress")), ' Mendenhall CPA'),
    building_room = substring("adjAddress", position('Mendenhall CPA ' in "adjAddress")+14, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Mendenhall CPA %'

    UPDATE public."CampusDirectory" SET
	building ='Mendenhall Center for Performing Arts',
    building_room = substring("adjAddress", position('Mendenhall CPA ' in "adjAddress")+16, length("adjAddress"))
    WHERE campus_address LIKE '%Mendenhall%'

17.
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Mendenhall CPA, ' in "adjAddress")), ' Mendenhall CPA'),
    building_room = substring("adjAddress", position('Mendenhall CPA, ' in "adjAddress")+15, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Mendenhall CPA, %'

18. Dewey Hall. Rm 302
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Dewey Hall.' in "adjAddress")), ' Dewey Hall'),
    building_room = substring("adjAddress", position('Dewey Hall.' in "adjAddress")+12, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Dewey Hall.%'
19.Dewey Hall 210
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Dewey House ' in "adjAddress")), ' Dewey House'),
    building_room = substring("adjAddress", position('Dewey House ' in "adjAddress")+11, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Dewey House %'
20. Dewey House, 305
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Dewey House, ' in "adjAddress")), ' Dewey House'),
    building_room = substring("adjAddress", position('Dewey House, ' in "adjAddress")+12, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Dewey House, %'

--hillyer w room numbers
UPDATE public."CampusDirectory" SET

    building_room = substring(campus_address, position(', Hillyer' in "adjAddress")+9, length(campus_address))
    WHERE campus_address LIKE '%, Hillyer%'



21. 8 College Lane, 201
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Lane, ' in "adjAddress")), ' Lane'),
    building_room = substring("adjAddress", position('Lane, ' in "adjAddress")+6, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Lane, %'

22. 47 Belmont Avenue, Rm 203
UPDATE public."CampusDirectory" SET
	building = CONCAT(substring("adjAddress", 0, position('Belmont Avenue, ' in "adjAddress")), ' Belmont Avenue'),
    building_room = substring("adjAddress", position('Belmont Avenue, ' in "adjAddress")+15, length("adjAddress"))
    WHERE "adjAddress" LIKE '%Belmont Avenue, %'

--Join campus directory & centroid geoms
SELECT geom, building_name, campus_address,display_name
FROM public.centroids_buildings as centroid LEFT JOIN public."CampusDirectory" as directory
ON centroid.building_name = directory.building;


SELECT DISTINCT node_indentifier, geom, display_name,campus_address, campus_extension, dept_agg, dept_url_agg, display_class_year, email, first_name, image_id, last_name, mailbox, person_type_agg, pref_first, title_dept, building, building_room
FROM public."CampusDirectory" as directory  LEFT JOIN public.centroids_buildings as centroid
ON centroid.building_name = directory.building
WHERE building LIKE '%Wright%'
;



SELECT  campus_address, building, geom, display_name
FROM public."CampusDirectory" as directory
LEFT OUTER JOIN public.centroids_buildings as centroids
ON directory.building = centroids.building_name
order by display_name
;





SELECT  campus_address, building, geom, display_name
FROM public."CampusDirectory" as directory
LEFT OUTER JOIN public.centroids_buildings as centroids
ON directory.building = centroids.building_name
order by building desc

SELECT  campus_address, building, building_room, geom, bldg_name, display_name
FROM public."CampusDirectory" as directory
LEFT OUTER JOIN public.centroids_buildings as centroids
ON directory.building = centroids.building_name
order by building desc

stoddard -> Stoddard Hall (and Annex)

check for extra spacings for wright hall, etc

//assigning building_id with gid
UPDATE  public."CampusDirectory" directory
SET     building_id = p.gid
FROM    (
        SELECT * FROM public."CampusDirectory" as directory
LEFT OUTER JOIN public.centroids_buildings as centroids
ON directory.building = centroids.building_name
        ) p
WHERE   directory.building = p.building_name



update public."CampusDirectory" directory
set building_id = p.gid
from(
SELECT * FROM public."CampusDirectory" as directory
LEFT OUTER JOIN public."CampusBuildings" as buildings
ON directory.building = buildings.building_name) p
where directory.building = p.building_name


update public."CampusBuildings" buildings
SET geom_center = p.geom
from(
select *
from public."CampusBuildings" as buildings left outer join public.centroids_buildings as centroids
on buildings.building_name = centroids.bldg_name) p
where buildings.building_name = p.bldg_name




SELECT   geom,gid, building_id, campus_address, building, building_room, bldg_name, display_name
FROM public."CampusDirectory" as directory
LEFT OUTER JOIN public.centroids_buildings as centroids
ON directory.building = centroids.building_name
ORDER BY building




delete from public."CampusBuildings"
where building_name is null

delete from public."CampusBuildings"
where geom_shape is null and building_name like '%Crew%'



select * from public."CampusBuildings"
where geom_shape is null and building_name like '%30 Belmont%'



select * from public."CampusBuildings"
order by building_name


ALTER TABLE public."CampusBuildings" ADD column id bigserial;

INSERT INTO public."CampusBuildings" (gid, building_name, geom_shape, building_area)
SELECT gid, bldg_name, geom, shape_area FROM public.campus_buildings


INSERT INTO public."CampusBuildings" (gid, building_name, geom_center, building_area)
SELECT 8888,name, geom, area FROM public."POI"



select campus_address, display_name, building, building_id,gid, building_name from
(select campus_address, display_name, building, building_room, building_id from public."CampusDirectory") as directory
left outer join public."CampusBuildings" as buildings
on directory.building = buildings.building_name

select campus_address, display_name, building, building_id,gid, building_name from
(select campus_address, display_name, building, building_room, building_id from public."CampusDirectory") as directory
left outer join public."CampusBuildings" as buildings
on directory.building = buildings.building_name
order by building desc



update public."CampusDirectory" as directory
set geom_center = p.geom_center
from
(select buildings.geom_center, buildings.building_name from
public."CampusDirectory" as directory
left outer join public."CampusBuildings" as buildings
on directory.building = buildings.building_name) p
where directory.building = p.building_name


??????
Green Street, Classroom Annex 208
21 Henshaw Ave vs Henshaw C2 204
138 Elm Street 2A (101)
76 Elm Street RM 302 v Green Street Classroom Annex, Rm 104A
Burton B015A -> TODO change to Burton Hall B015A...
Five College Library Annex v Neilson Library 3/09
College Hall 2014
Fort Hill, CECE

Dewey 101 v Dewey House 306/Dewey Hall. Rm 302

College Hall- 201
Sabin Reed 401
Burton B015A
Hatfield 308
138 Elm Street 2A (101)
Young 101
UPDATE public."CampusDirectory" SET
	building = 'Young Library',
    building_room = '101'

    where campus_address like '%Young 101%'


    campus buidling:
    Friedman Complex (A,B,C,D)
    Friedman Complex (A,B,C,D)
    Friedman Complex (A,B,C,D)
    Friedman Complex (A,B,C,D)

    Mendenhall Center for Performing Arts
    Mendenhall Center for Performing Arts
    Mendenhall Center for Performing Arts

    Parsons House
    Parsons House



    in directory, but not in buildings
    Mount Holyoke College
    Green Street Classroom Annex
    Five College Library
    Five College Annex
    Fine Arts Center, Tryon
    Fine Arts Center, Gallery
    Facilites Management
    Compliance and Risk Management
    Clark Science Center
    8 Paradise Road
    7 College Lane
    47 Belmont Avenue
    42 Green Street
    33 Elm Street
    21 Henshaw Ave
    18 Henshaw
    Henshaw



'''
