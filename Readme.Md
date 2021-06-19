# Threaded-Comments-API
Comment Thread API using Django and DRF

## Work To Be Done
```bash
Codingal Backend Assessment

As part of our interview process, in this assessment, you work on creating an API server using Django and DRF for a threaded comments application. The API should have the following capabilities:
1.	Get a list of all comments made on a page with a given URL.
2.	Add a new comment on a page with a given URL.
3.	Add a new sub-comment on an already existing comment as a reply.
4.	Edit an existing comment.
5.	Delete a single comment or an entire comment thread using the comment's identifier.
Keep in mind that there are no ‘right answers.’ This project is deliberately kept open-ended and designed to gauge your skills and give us an idea of how you approach tasks relevant to the role. Emphasis will be on good model design, following REST best practices, code quality, and documentation.It would be great if you could add the project on GitHub and send the link over to us within 2 days. Please do not hesitate to reply to this email if you have any questions.Best of luck with the project!
```

## Functionalities
* Get all the comments and their respective replies on a page
* Add a comment or a reply (sub comment)
* Edit a comment or a reply
* Delete a comment or the whole thread. (The whole thread gets deleted if the parent comment is deleted)
## Technologies used
* Language : Python
* Framework: Django
* Rest API: Django Rest Framework
* database: sqlite3

## Commands
* Setting up this project in you system:\
First Clone it using:
```bash
git clone https://github.com/alam-mahtab/Comments.git
```
* Then run the following commands to start the server

```python
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver 
```
* Dont Forget to change the database in settings.py
## Endpoint for different functionalities
#### Get all comments: http://127.0.0.1:8000 or http://127.0.0.1:8000/get

#### Create a new comment: http://127.0.0.1:8000/add/
* Create a new comment:

```bash
# input

{ 
    "comment_body": "This Is A Comment",
    "is_sub_comment": 0,  # Boolean (Only True when comment is a reply)
    "parent_id": -1    # if the comment itself is the parent, set parent_id = -1

}
```
* Add a reply:
```bash
# input
{ 
    "comment_body": "Testing Comment",
    "is_sub_comment": 1,
    "parent_id": 3  # the ID of the parent comment

}
```
* Edit a comment: http://localhost:8000/put/

```bash
# input
{
 "comment_id": 3,
 "comment_body": "Comments to be tested",
}
```
* Delete a comment: http://localhost:8000/delete/
```bash
# input
{
  "comment_id": 6
}
```
