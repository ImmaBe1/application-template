from os import environ as env

db_maps = {
    "my_db_key": {
        "user": env['CLOUDANT_USER'],
        "password": env['CLOUDANT_PASSWORD'],
        "url": env['CLOUDANT_URL'],
        "db_name": env['CLOUDANT_TEST_TBL']
    }
}
   