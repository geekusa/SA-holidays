## SA-holidays

This supporting add-on provides one command -- `holidays`. A wrapper for python-holidays (https://github.com/dr-prodigy/python-holidays) providing holidays, business days, and business holidays when presented a \_time (or specified) field.

Version: 1.0

Command reference:

# holidays

## Description

A wrapper for for the python library python-holidays (https://github.com/dr-prodigy/python-holidays) to enrich existing data with timestamps to know if the given timestamp is a holiday, business day, or business holiday (a holiday that occurs on a normal business day). Default settings: country is set to US and timestamp is expected in the `_time` field. This can be helpful for a number of reasons but often for predictions or forecasts as those days usually will mean a difference in the model, especially those holidays that land on a business day. 

Supported country, state, and province codes can be found listed on https://github.com/dr-prodigy/python-holidays/blob/master/README.rst

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
   	**Description:** Country code string from https://github.com/dr-prodigy/python-holidays/blob/master/README.rst, defaults to US
   	**Usage:** i.e. country=DE
   	**Default:** US

  **state**  
   	**Syntax:** state="\<string\>"  
   	**Description:** State code string from https://github.com/dr-prodigy/python-holidays/blob/master/README.rst, defaults to none
   	**Usage:** i.e. state=CA
   	**Default:** None

  **province**  
   	**Syntax:** province="\<string\>"  
   	**Description:** Province code string from https://github.com/dr-prodigy/python-holidays/blob/master/README.rst, defaults to none
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

##Examples

###**1: Enrich existing \_time field with US holidays**###

`* | holidays`

###**2: Enrich existing \_time field with US holidays in California**###

`* | holidays state=CA`

###**3: Add custom holiday**###

`* | holidays custom_holiday="Jan 16,2020"`

###**4: Hong Kong holidays**###

`* | holidays country=HK`

###**5: Baden-Württemberg province in Germany holidays**###

`* | holidays country=DE province=BW`
