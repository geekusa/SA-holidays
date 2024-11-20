## SA-holidays

This supporting add-on provides one command -- `holidays`. A wrapper for python-holidays providing holidays, business days, and business holidays when presented a \_time (or specified) field.

Version: 1.3.0

Command reference:

# holidays

## Description

A wrapper for for the python library holidays (https://github.com/vacanza/holidays) to enrich existing data with timestamps to know if the given timestamp is a holiday, business day, or business holiday (a holiday that occurs on a normal business day). Default settings: country is set to US and timestamp is expected in the `_time` field.

Supported country, state, province, and market codes can be found listed on https://github.com/vacanza/holidays/blob/dev/README.rst 

Currently supports 154 countries and 4 financial markets.

## Syntax

 * | holidays [timefield=<field>] [country=<string>] [province=<string>] [state=<string>] [business\_days=<comma\_sep\_int>] [custom_holiday=<date>]


###Optional arguments

  **timefield**  
   	**Syntax:** timefield="\<field\>"  
   	**Description:** The field containing the timestamp in unix epoch, normally this is `_time` which is the default if not set.
   	**Usage:** i.e. timefield=timestamp
   	**Default:** \_time

  **country**  
   	**Syntax:** country="\<string\>"  
   	**Description:** Country code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to US
   	**Usage:** i.e. country=DE
   	**Default:** US

  **subdiv**  
   	**Syntax:** subdiv="\<string\>"  
   	**Description:** Subdivision code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to none
   	**Usage:** i.e. country=US subdiv=PR
   	**Default:** None

  **state**  
   	**Syntax:** state="\<string\>"  
   	**Description:** Deprecated--Subdivision code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to none
   	**Usage:** i.e. state=CA
   	**Default:** None

  **province**  
   	**Syntax:** province="\<string\>"  
   	**Description:** Deprecated--Subdivision code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to none
   	**Usage:** i.e. country=DE province=BW
   	**Default:** None

  **business\_days**  
   	**Syntax:** business\_days="\<comma-sep-int\>"  
   	**Description:** Defaults to Monday-Friday (1-5) but if different days are business days they can be specified using numbers (Saturday and Sunday are 6 and 7 respectively)
   	**Usage:** i.e. business\_days="2,3,4,5,6,7"
   	**Default:** 1,2,3,4,5

  **custom\_holiday**  
   	**Syntax:** custom\_holiday="\<date\>"  
   	**Description:** Ability to supply a date string for a non-standard holiday.
   	**Usage:** i.e. custom\_holiday="2020-01-16"
   	**Default:** None

  **language**  
   	**Syntax:** language="\<string\>"  
   	**Description:** Language code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to none
   	**Usage:** i.e. country=MX language=es
   	**Default:** None

  **market**  
   	**Syntax:** market="\<string\>"  
   	**Description:** Financial Markets code string https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to none
   	**Usage:** i.e. market=ECB
   	**Default:** None

##Examples

###**1: Enrich existing \_time field with US holidays**###

`* | holidays`

###**2: Enrich existing \_time field with US holidays in California**###

`* | holidays subdiv=CA`

###**3: Add custom holiday**###

`* | holidays custom_holiday="Jan 16, 2020"`

###**4: Hong Kong holidays**###

`* | holidays country=HK`

###**5: Baden-Württemberg province in Germany holidays**###

`* | holidays country=DE subdiv=BW`

###**6: Cuban holidays in Spanish**###

`* | holidays country=CU language=es`

###**7: NYSE market holidays**###

`* | holidays market=NYSE`

### Release Notes
Updated splunklib from 1.7.3 to 2.0.2. Updated python-holidays from 0.21.13 to migrated holidays 0.61. Added new market option to find financial market holidays.
