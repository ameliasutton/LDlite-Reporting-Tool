# LDlite Single Select

An Interface for running simple sql queries without a SQL IDE

## Requirements


* Python 3.x
* json
* tkinter
* sys
* psycopg2
* os
* datetime

## Optional Requirements
* pyinstaller
  

## __Instructions:__

### Setup:
* Create json config file in the following format:
>{\
    "dbname": " ",\
    "user": " ",\
    "host": " ",\
    "password": " ",\
    "query_filepath" : " ",\
    "output_filepath" : " ",\
    "generate_log": [Boolean],\
    "log_file_output_filepath": " "\
}

* **query_filepath,**  **output_filepath,** and **log_file_output_filepath** should point to existing folders that you have read/write permissons for.
  
* To generate an excecutable you will need pyinstaller installed. Run **generate_excecutable.bat**. After running you should have an excecutable called **LDliteSingleSelect.exe**
### Usage:
* Run the program either by launching **LDliteSingleSelect.exe**, running **LDliteSingleSelect.bat**, or by running **LDliteSingleSelect.py** through the command line.
  
* Using the dropdown select the **Query Name** for the .sql file you wish to excecute.
  
* If desired modify the **Output File Name**.
  
* Select **Run Query**
  
* When finished use **File>Exit** to close the program
  
## Notes
* It is recommended that you use PyInstaller to generate an executable version of LDliteSingleSelect.py to run instead 
of running it through LDliteSingleSelect.bat

* See https://github.com/5-C-Folio/LDlite-Queries for a collection of pre-created .sql files

## Contributors


* Amelia Sutton


## Version History

* 0.1
    * Initial Release
* 1.0
    * Full Release
    * Removed **query_file** parameter from the config file in favor of checking for query options in the folder specified by **query_filepath** simplifying the process of adding new queries and removing the need for additional config files.
    * Added **output_filepath** parameter to config
* 1.1
    * Added option to enable a simple logging function
    * Config file now contains two new fields **generate_log,** (Boolean) and **log_file_output_filepath** (String)
    
## Known Issues
* 
## Planned Features
*

