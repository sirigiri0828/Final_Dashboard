from .data_base_connections import *

def get_no_affected():
    query = "SELECT SUM(NO_AFFECTED) AS NO_AFFECTED FROM `peak-essence-367304.MSHA.VIOLATIONS`"
    return get_mysql_data(query)["NO_AFFECTED"][0]

def get_penalty():
    query = "SELECT SUM(PROPOSED_PENALTY) AS PROPOSED_PENALTY FROM `peak-essence-367304.MSHA.VIOLATIONS`"
    return get_mysql_data(query)["PROPOSED_PENALTY"][0]

def get_insp_hours():
    query = "SELECT SUM(SUM_TOTAL_INSP_HOURS_) AS INSPECTION_HOURS FROM `peak-essence-367304.MSHA.INSPECTIONS`"
    return get_mysql_data(query)["INSPECTION_HOURS"][0]

def get_violations():
    query = "SELECT COUNT(EVENT_NO) AS NUMBER_OF_VIOLATIONS FROM `peak-essence-367304.MSHA.VIOLATIONS`"
    return get_mysql_data(query)["NUMBER_OF_VIOLATIONS"][0]
    
def get_table_data_of_year(columns,table_name,year):
    query = "SELECT {columns}  FROM `peak-essence-367304.MSHA.{table_name}` WHERE CAL_YR IN {year}".format(columns = columns,table_name = table_name,year = str(tuple(year)))
    return get_mysql_data(query)

def get_table_data_of_year_mines(columns,table_name):
    query = "SELECT {columns}  FROM `peak-essence-367304.MSHA.{table_name}`".format(columns = columns,table_name = table_name)
    return get_mysql_data(query)


