# This script get the list of profiles in a simplifier projet and return a csv with the versions and last updated dates.
# It is limited to 1000 resources for now (pagination not managed)

import requests
import json
import xlsxwriter

projectName = "CI-SIS"

workbook = xlsxwriter.Workbook(projectName + '.xlsx')


#############################
## Get StructureDefinition ##
#############################
worksheet = workbook.add_worksheet("StructureDefinition")

x = requests.get('https://fhir.simplifier.net/' + projectName + '/StructureDefinition?_count=1000')
entries = json.loads(x.text)["entry"]

row = 0
column_incr =0

worksheet.write(0, column_incr, "Name")
column_incr +=1
worksheet.write(0, column_incr, "Type")
column_incr +=1
worksheet.write(0, column_incr, "Project")
column_incr +=1
worksheet.write(0, column_incr, "Version")
column_incr +=1
worksheet.write(0, column_incr, "Status")
column_incr +=1
worksheet.write(0, column_incr, "Last updated")
column_incr +=1
worksheet.write(0, column_incr, "Version id")

for entry in entries:
    row += 1
    column_incr = 0
    worksheet.write(row, column_incr, entry["resource"]["name"])

    column_incr +=1
    worksheet.write(row, column_incr, entry["resource"]["type"])

    column_incr +=1
    tmp = entry["resource"]["name"].split('_')
    if len(tmp) > 1:
        worksheet.write(row, column_incr, tmp[0])

    column_incr +=1
    if "version" in entry["resource"]:
        worksheet.write(row, column_incr, entry["resource"]["version"])

    column_incr +=1
    if "status" in entry["resource"]:
        worksheet.write(row, column_incr, entry["resource"]["status"])

    column_incr +=1
    worksheet.write(row, column_incr, entry["resource"]["meta"]["lastUpdated"])

    column_incr +=1
    if "versionId" in entry["resource"]["meta"]:
        worksheet.write(row, column_incr, entry["resource"]["meta"]["versionId"])

#########################
## Get SearchParameter ##
#########################
worksheet = workbook.add_worksheet("SearchParameter")

x = requests.get('https://fhir.simplifier.net/' + projectName + '/SearchParameter?_count=1000')

entries = json.loads(x.text)["entry"]


row = 0
column_incr =0


worksheet.write(0, column_incr, "Name")
column_incr +=1
worksheet.write(0, column_incr, "Project")
column_incr +=1
worksheet.write(0, column_incr, "Version")
column_incr +=1
worksheet.write(0, column_incr, "Status")
column_incr +=1
worksheet.write(0, column_incr, "Last updated")
column_incr +=1
worksheet.write(0, column_incr, "Version id")

for entry in entries:
    row += 1
    column_incr =0

    worksheet.write(row, column_incr, entry["resource"]["name"])

    column_incr +=1
    tmp = entry["resource"]["name"].split('_')
    if len(tmp) > 1:
        worksheet.write(row, column_incr, tmp[0])

    column_incr +=1
    if "version" in entry["resource"]:
        worksheet.write(row, column_incr, entry["resource"]["version"])

    column_incr +=1
    if "status" in entry["resource"]:
        worksheet.write(row, column_incr, entry["resource"]["status"])

    column_incr +=1
    worksheet.write(row, column_incr, entry["resource"]["meta"]["lastUpdated"])

    column_incr +=1
    if "versionId" in entry["resource"]["meta"]:
        worksheet.write(row, column_incr, entry["resource"]["meta"]["versionId"])

workbook.close()