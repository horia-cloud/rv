# rv
Task:

Design and code a simple app that exposes the following HTTP based APIs

a)Saves/updates the given user's name and date of birth in the database:
Request: PUT /hello/John{"dateOfBirth":"2001-01-01"
Response: 204 No Content

b)Returns a hello/birthday message for given user:
Request: GET /hello/John
Response: 200 OK

-when John's birthday is in 5 days:
{"message": "Hello, John! Your birthday is in 5 days"}

-when John's birthday is today:
{"message": "Hello,John! Happy birthday!"}

#############################################################################################################
