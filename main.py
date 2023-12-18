from pymongo import MongoClient
from datetime import datetime
import pprint
from bson import ObjectId

connection_string = "mongodb://localhost:27017"
client = MongoClient(connection_string)
database = client["Tribal_Management"]

login = database["login"]
admin_data = database["Admin"]
locality = database["Locality"]
project = database["Project"]
sponser = database["Sponser"]
budget_alloc = database["Budget_alloc"]

# admins = [
#     {
#         "admin_id": 105,
#         "admin_name": "Shrish",
#         "mobile_number": "1111111111",
#     },
#     {
#         "admin_id": 106,
#         "admin_name": "Admin6",
#         "mobile_number": "2222222222",
#     },
#     {
#         "admin_id": 107,
#         "admin_name": "Admin7",
#         "mobile_number": "3333333333",
#     },
#     {
#         "admin_id": 108,
#         "admin_name": "Admin8",
#         "mobile_number": "4444444444",
#     },
#     {
#         "admin_id": 109,
#         "admin_name": "Admin9",
#         "mobile_number": "5555555555",
#     },
#     {
#         "admin_id": 110,
#         "admin_name": "Admin10",
#         "mobile_number": "6666666666",
#     },
#     {
#         "admin_id": 111,
#         "admin_name": "Admin11",
#         "mobile_number": "7777777777",
#     },
#     {
#         "admin_id": 112,
#         "admin_name": "Admin12",
#         "mobile_number": "8888888888",
#     },
#     {
#         "admin_id": 113,
#         "admin_name": "Admin13",
#         "mobile_number": "9999999999",
#     },
#     {
#         "admin_id": 114,
#         "admin_name": "Admin14",
#         "mobile_number": "1234567890",
#     },
# ]
#
# admin_data.insert_many(admins)
#
# localities = [
#     {
#         "locality_id": 5,
#         "locality_name": "City5",
#         "state": "State2",
#         "population": 400000,
#         "locality_area": 90.2,
#         "total_rate": 9.8,
#         "male_rate": 47.5,
#         "female_rate": 52.5,
#     },
#     {
#         "locality_id": 6,
#         "locality_name": "City6",
#         "state": "State3",
#         "population": 600000,
#         "locality_area": 120.5,
#         "total_rate": 12.5,
#         "male_rate": 50.0,
#         "female_rate": 50.0,
#     },
#     {
#         "locality_id": 7,
#         "locality_name": "City7",
#         "state": "State1",
#         "population": 800000,
#         "locality_area": 180.0,
#         "total_rate": 18.0,
#         "male_rate": 48.2,
#         "female_rate": 51.8,
#     },
#     {
#         "locality_id": 8,
#         "locality_name": "City8",
#         "state": "State4",
#         "population": 250000,
#         "locality_area": 60.0,
#         "total_rate": 6.0,
#         "male_rate": 51.0,
#         "female_rate": 49.0,
#     },
#     {
#         "locality_id": 9,
#         "locality_name": "City9",
#         "state": "State2",
#         "population": 350000,
#         "locality_area": 75.5,
#         "total_rate": 7.5,
#         "male_rate": 49.8,
#         "female_rate": 50.2,
#     },
#     {
#         "locality_id": 10,
#         "locality_name": "City10",
#         "state": "State3",
#         "population": 550000,
#         "locality_area": 110.0,
#         "total_rate": 11.0,
#         "male_rate": 50.5,
#         "female_rate": 49.5,
#     },
#     {
#         "locality_id": 11,
#         "locality_name": "City11",
#         "state": "State1",
#         "population": 950000,
#         "locality_area": 220.5,
#         "total_rate": 22.5,
#         "male_rate": 49.2,
#         "female_rate": 50.8,
#     },
#     {
#         "locality_id": 12,
#         "locality_name": "City12",
#         "state": "State4",
#         "population": 200000,
#         "locality_area": 50.0,
#         "total_rate": 5.0,
#         "male_rate": 52.5,
#         "female_rate": 47.5,
#     },
#     {
#         "locality_id": 13,
#         "locality_name": "City13",
#         "state": "State2",
#         "population": 300000,
#         "locality_area": 70.5,
#         "total_rate": 7.0,
#         "male_rate": 48.0,
#         "female_rate": 52.0,
#     },
#     {
#         "locality_id": 14,
#         "locality_name": "City14",
#         "state": "State3",
#         "population": 450000,
#         "locality_area": 100.0,
#         "total_rate": 10.0,
#         "male_rate": 50.2,
#         "female_rate": 49.8,
#     },
# ]
#
# # Insert data into MongoDB collection
# locality.insert_many(localities)
#
# project_data = [
#     {
#         "project_id": 501,
#         "locality_id": 5,
#         "project_name": "ProjectE",
#         "admin_id": 105,
#         "sponsor_id": 205,
#     },
#     {
#         "project_id": 502,
#         "locality_id": 6,
#         "project_name": "ProjectF",
#         "admin_id": 106,
#         "sponsor_id": 206,
#     },
#     {
#         "project_id": 503,
#         "locality_id": 7,
#         "project_name": "ProjectG",
#         "admin_id": 107,
#         "sponsor_id": 207,
#     },
#     {
#         "project_id": 504,
#         "locality_id": 8,
#         "project_name": "ProjectH",
#         "admin_id": 108,
#         "sponsor_id": 208,
#     },
#     {
#         "project_id": 505,
#         "locality_id": 9,
#         "project_name": "ProjectI",
#         "admin_id": 109,
#         "sponsor_id": 209,
#     },
#     {
#         "project_id": 506,
#         "locality_id": 10,
#         "project_name": "ProjectJ",
#         "admin_id": 110,
#         "sponsor_id": 210,
#     },
#     {
#         "project_id": 507,
#         "locality_id": 11,
#         "project_name": "ProjectK",
#         "admin_id": 111,
#         "sponsor_id": 211,
#     },
#     {
#         "project_id": 508,
#         "locality_id": 12,
#         "project_name": "ProjectL",
#         "admin_id": 112,
#         "sponsor_id": 212,
#     },
#     {
#         "project_id": 509,
#         "locality_id": 13,
#         "project_name": "ProjectM",
#         "admin_id": 113,
#         "sponsor_id": 213,
#     },
#     {
#         "project_id": 510,
#         "locality_id": 14,
#         "project_name": "ProjectN",
#         "admin_id": 114,
#         "sponsor_id": 214,
#     },
# ]
#
# project.insert_many(project_data)
#
# budgets = [
#     {
#         "budget_id": 305,
#         "budget": 4000000,
#         "allot_date": datetime.strptime('2023-05-05', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 306,
#         "budget": 6000000,
#         "allot_date": datetime.strptime('2023-06-10', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 307,
#         "budget": 8000000,
#         "allot_date": datetime.strptime('2023-07-15', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 308,
#         "budget": 2500000,
#         "allot_date": datetime.strptime('2023-08-20', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 309,
#         "budget": 3500000,
#         "allot_date": datetime.strptime('2023-09-25', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 310,
#         "budget": 5500000,
#         "allot_date": datetime.strptime('2023-10-30', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 311,
#         "budget": 9500000,
#         "allot_date": datetime.strptime('2023-11-05', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 312,
#         "budget": 2000000,
#         "allot_date": datetime.strptime('2023-12-10', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 313,
#         "budget": 3000000,
#         "allot_date": datetime.strptime('2024-01-15', '%Y-%m-%d'),
#     },
#     {
#         "budget_id": 314,
#         "budget": 4500000,
#         "allot_date": datetime.strptime('2024-02-20', '%Y-%m-%d'),
#     },
# ]
#
# budget_alloc.insert_many(budgets)
#
# sponsors = [
#     {
#         "sponsor_id": 205,
#         "sponsor_name": "Sponsor5",
#         "sponsor_mobile": "9876543210",
#         "budget_id": 305,
#     },
#     {
#         "sponsor_id": 206,
#         "sponsor_name": "Sponsor6",
#         "sponsor_mobile": "8765432109",
#         "budget_id": 306,
#     },
#     {
#         "sponsor_id": 207,
#         "sponsor_name": "Sponsor7",
#         "sponsor_mobile": "7654321098",
#         "budget_id": 307,
#     },
#     {
#         "sponsor_id": 208,
#         "sponsor_name": "Sponsor8",
#         "sponsor_mobile": "6543210987",
#         "budget_id": 308,
#     },
#     {
#         "sponsor_id": 209,
#         "sponsor_name": "Sponsor9",
#         "sponsor_mobile": "5432109876",
#         "budget_id": 309,
#     },
#     {
#         "sponsor_id": 210,
#         "sponsor_name": "Sponsor10",
#         "sponsor_mobile": "4321098765",
#         "budget_id": 310,
#     },
#     {
#         "sponsor_id": 211,
#         "sponsor_name": "Sponsor11",
#         "sponsor_mobile": "3210987654",
#         "budget_id": 311,
#     },
#     {
#         "sponsor_id": 212,
#         "sponsor_name": "Sponsor12",
#         "sponsor_mobile": "2109876543",
#         "budget_id": 312,
#     },
#     {
#         "sponsor_id": 213,
#         "sponsor_name": "Sponsor13",
#         "sponsor_mobile": "1098765432",
#         "budget_id": 313,
#     },
#     {
#         "sponsor_id": 214,
#         "sponsor_name": "Sponsor14",
#         "sponsor_mobile": "9876543210",
#         "budget_id": 314,
#     },
# ]
#
# sponser.insert_many(sponsors)
#
# login.insert_one({"id":"shrish","password":"12345"})
#
# tribal_memb.drop()
# locality.drop()
# project.drop()
# sponser.drop()
# budget_alloc.drop()
# admin_data.drop()
# login.drop()
