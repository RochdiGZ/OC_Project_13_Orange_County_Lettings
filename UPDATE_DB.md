## Download SQLite tools
- You open the download page https://www.sqlite.org/download.html
- You download the zip file via https://www.sqlite.org/2023/sqlite-tools-win32-x86-3420000.zip

A bundle of command-line tools for managing SQLite database files, including :
- the command-line Shell program : `sqlite3.exe`
- the `sqldiff.exe` program
- the `sqlite3_analyzer.exe` program

## Open oc-lettings-site.sqlite3 database

```bash
.\sqlite3.exe
```
- #### sqlite> .open oc-lettings-site.sqlite3

## Insert the data to the 3 tables : lettings_address, lettings_letting and profiles_profile

- #### sqlite> INSERT INTO lettings_address SELECT * FROM oc_lettings_site_address;

- #### sqlite> INSERT INTO lettings_letting SELECT * FROM oc_lettings_site_letting;

- #### sqlite> INSERT INTO profiles_profile SELECT * FROM oc_lettings_site_profile;

## Drop the old tables : oc_lettings_site_address, oc_lettings_site_letting and oc_lettings_site_profile

- #### sqlite> DROP TABLE oc_lettings_site_address;

- #### sqlite> DROP TABLE oc_lettings_site_letting;

- #### sqlite> DROP TABLE oc_lettings_site_profile;

## Close oc-lettings-site.sqlite3 database

- #### sqlite> .quit