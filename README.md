FastAPI + MongoDB Bookstore


##############################
install 
##############################

python -m venv my_env

source my_env/bin/activate 


for windows my_env/Script/activate


pip install -r requirements.txt


fastapi dev main  # for start project

http://127.0.0.1:8000/docs ## or redoc



#################
register user
#################

curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "123456"}'


################
login user
################

curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=123456"


############
create book
###########

curl -X POST http://localhost:8000/books/add_books \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title": "Book Title", "author": "Author Name", "description": "Details"}'


############
get book
###########

curl -X GET "http://localhost:8000/books/get_books?author=author"


##############
edit book
#############

curl -X PUT http://localhost:8000/books/edit_books/ID book \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Title",
        "author": "author",
        "description": "description"
      }'




###############
delete book
###############


curl -X DELETE http://localhost:8000/books/delete_book/ID book \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

#################################################################################################################

FastAPI

MongoDB (Motor)

JWT (OAuth2)

Pydantic


