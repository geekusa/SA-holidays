#!/opt/splunk/bin/python

import sys
import re
import time
import holidays

from datetime import datetime, timedelta
from time import mktime,strftime
from splunk import setupSplunkLogger
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators


#@Configuration(local=True)
@Configuration()
class MakeHolidays(StreamingCommand):
    """ 
    A wrapper for python-holidays providing holidays, business days, and business holidays when presented a _time (or specified) field.

    ##Syntax

    .. code-block::
       * | holidays [timefield=<field>] [country=<string>] [province=<string>] [state=<string>] [business_days=<comma_sep_int>] [custom_holiday=<date>]

    ##Description

    A wrapper for for the python library python-holidays (https://github.com/dr-prodigy/python-holidays) 
    to enrich existing data with timestamps to know if the given timestamp is a holiday, business day,
    or business holiday (a holiday that occurs on a normal business day). Default settings: country is 
    set to US and timestamp is expected in the `_time` field.

    ##Example

    .. code-block::
        * | holidays
    """

    timefield = Option(
        default='_time',
        doc='''
        **Syntax:** **timefield=***<fieldname>*
        **Description:** The field containing the timestamp in unix epoch, normally this is `_time` which is the default if not set.''',
        validate=validators.Fieldname())

    country = Option(
        default='US',
        doc='''
        **Syntax:** **country=***<string>*
        **Description:** Country code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to US''',
        )

    subdiv = Option(
        default=None,
        doc='''
        **Syntax:** **subdiv=***<string>*
        **Description:** Subdivision code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to None''',
        )

    province = Option(
        default=None,
        doc='''
        **Syntax:** **province=***<string>*
        **Description:** Deprecated--Subdivision code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to None''',
        )

    state = Option(
        default=None,
        doc='''
        **Syntax:** **state=***<string>*
        **Description:** Deprecated--Subdivision code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to None''',
        )

    business_days = Option(
        default=None,
        doc='''
        **Syntax:** **business_days=***<comma-sep-int>*
        **Description:** Defaults to Monday-Friday (1-5) but if different days are business days they can be specified using numbers (Saturday and Sunday are 6 and 7 respectively) ''',
        )

    custom_holiday = Option(
        default=None,
        doc='''
        **Syntax:** **custom_holiday=***<date>*
        **Description:** Ability to supply a date for a non-standard holiday.''',
        )

    language = Option(
        default=None,
        doc='''
        **Syntax:** **language=***<string>*
        **Description:** Language code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to None''',
        )
  
    market = Option(
        default=None,
        doc='''
        **Syntax:** **market=***<string>*
        **Description:** Financial market code string from https://github.com/vacanza/holidays/blob/dev/README.rst, defaults to None''',
        )
  
    def subdiv_option(self):
        if self.subdiv:
            return self.subdiv
        elif self.state:
            return self.state
        elif self.province:
            return self.province
        else:
            return None
      

    def stream(self, records):
        if self.market:
            holiday_list = holidays.financial_holidays(
                 self.market,
            )
        else:
            holiday_list = holidays.country_holidays(
                 self.country,
                 subdiv=self.subdiv_option(),
                 language=self.language
            )
        if self.custom_holiday:
             holiday_list.append([self.custom_holiday])

        if self.business_days:
            if re.search(r'(\d+,?)+',self.business_days):
                working_days = [ int(i) for i in self.business_days.split(',')]
        else:
            working_days = [1,2,3,4,5]
        
        for record in records:
            converted_time = time.localtime(float(record[self.timefield]))
            converted_date = datetime.fromtimestamp(mktime(converted_time))
            record['is_holiday'] = converted_date in holiday_list
            record['holiday_name'] = holiday_list.get(converted_date)
            record['is_business_day'] = int(strftime('%u',converted_time)) in working_days
            record['is_business_holiday'] = int(strftime('%u',converted_time)) in working_days and converted_date in holiday_list

            yield record

dispatch(MakeHolidays, sys.argv, sys.stdin, sys.stdout, __name__)
