Problem Statement : Data Engineer Assessment.pdf
Solution file : Solution.py
Database file : UserDatabase.db
Users data file : users.txt
To open and visualize .db file : https://github.com/goutam-awadhiya/dbBrowserForSqlite.git
Input, workflow, output : README.txt

Input Data format:

|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active
|D|Alex|123457|2010-10-12|2012-10-13|MVD|Paul|SA|USA|1987-06-03|A
|D|John|123458|2010-10-12|2012-10-13|MVD|Paul|TN|IND|1987-06-03|A
|D|Mathew|123459|2010-10-12|2012-10-13|MVD|Paul|WAS|PHIL|1987-06-03|A
|D|Matt|12345|2010-10-12|2012-10-13|MVD|Paul|BOS|NYC|1987-06-03|A
|D|Kapil|123457|2010-10-12|2012-10-13|MVD|Paul|LA|USA|1987-06-03|A
|D|Jacob|1256|2010-10-12|2012-10-13|MVD|Paul|VIC|AU|1987-06-03|A
|D|Goutam|2345|2014-09-12|2014-10-13|MVD|Hari|UP|IND|1998-02-19|A
|D|Sean|2345|2014-09-12|2014-10-13|MVD|Hari|SAN|AU|1998-02-19|A
|D|Kajal|123459|2010-10-12|2012-10-13|MVD|Paul|MP|IND|1987-06-03|A


WorkFlow :

Step 1 : Read users.txt file
Step 2 : Check if 'AllUsers' table exists. If not create.
Step 3 : Insert data into AllUsers table.
Step 4 : Read data from AllUsers table.
Step 5 : for all the rows, check the country_name, check if Table_country_name exists.
Step 6 : create the Table_country name if doesn't exist and insert data into table.
Step 7 : Show the data across all the table.

Output :

-------------------------------------------------------- Table : AllUsers -------------------------------------------------------
 Customer_Name   Customer_Id    Open_Date   Last_Consulted_Date    Vaccination_Id   Dr_Name   State  Country    DOB     Is_Active
      Alex          123457     2010-10-12        2012-10-13             MVD           Paul      SA     USA   1987-06-03     A
      John          123458     2010-10-12        2012-10-13             MVD           Paul      TN     IND   1987-06-03     A
     Mathew         123459     2010-10-12        2012-10-13             MVD           Paul     WAS     PHIL  1987-06-03     A
      Matt          12345      2010-10-12        2012-10-13             MVD           Paul     BOS     NYC   1987-06-03     A
     Kapil          123457     2010-10-12        2012-10-13             MVD           Paul      LA     USA   1987-06-03     A
     Jacob           1256      2010-10-12        2012-10-13             MVD           Paul     VIC      AU   1987-06-03     A
     Goutam          2345      2014-09-12        2014-10-13             MVD           Hari      UP     IND   1998-02-19     A
      Sean           2345      2014-09-12        2014-10-13             MVD           Hari     SAN      AU   1998-02-19     A
     Kajal          123459     2010-10-12        2012-10-13             MVD           Paul      MP     IND   1987-06-03     A
----------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------- Table : Table_USA -------------------------------------------------------
 Customer_Name   Customer_Id    Open_Date   Last_Consulted_Date    Vaccination_Id   Dr_Name   State  Country    DOB     Is_Active
      Alex          123457     2010-10-12        2012-10-13             MVD           Paul      SA     USA   1987-06-03     A
     Kapil          123457     2010-10-12        2012-10-13             MVD           Paul      LA     USA   1987-06-03     A
----------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------- Table : Table_IND -------------------------------------------------------
 Customer_Name   Customer_Id    Open_Date   Last_Consulted_Date    Vaccination_Id   Dr_Name   State  Country    DOB     Is_Active
      John          123458     2010-10-12        2012-10-13             MVD           Paul      TN     IND   1987-06-03     A
     Goutam          2345      2014-09-12        2014-10-13             MVD           Hari      UP     IND   1998-02-19     A
     Kajal          123459     2010-10-12        2012-10-13             MVD           Paul      MP     IND   1987-06-03     A
----------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------- Table : Table_PHIL -------------------------------------------------------
 Customer_Name   Customer_Id    Open_Date   Last_Consulted_Date    Vaccination_Id   Dr_Name   State  Country    DOB     Is_Active
     Mathew         123459     2010-10-12        2012-10-13             MVD           Paul     WAS     PHIL  1987-06-03     A
----------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------- Table : Table_NYC -------------------------------------------------------
 Customer_Name   Customer_Id    Open_Date   Last_Consulted_Date    Vaccination_Id   Dr_Name   State  Country    DOB     Is_Active
      Matt          12345      2010-10-12        2012-10-13             MVD           Paul     BOS     NYC   1987-06-03     A
----------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------- Table : Table_AU -------------------------------------------------------
 Customer_Name   Customer_Id    Open_Date   Last_Consulted_Date    Vaccination_Id   Dr_Name   State  Country    DOB     Is_Active
     Jacob           1256      2010-10-12        2012-10-13             MVD           Paul     VIC      AU   1987-06-03     A
      Sean           2345      2014-09-12        2014-10-13             MVD           Hari     SAN      AU   1998-02-19     A
----------------------------------------------------------------------------------------------------------------------------------





