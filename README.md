# GamerTalk Backend

<img src="/public\GamerTalkWideLogo.png" alt="Header" title="Header" width="1200">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) ![GitHub last updated (branch)](https://img.shields.io/github/last-commit/GamerTalk/Backend/main) ![GitHub issues](https://img.shields.io/github/issues/GamerTalk/Backend) 

## Description

This is the backend server of the project GamerTalk. You can find the frontend server [here](https://github.com/GamerTalk/Frontend).

GamerTalk is an application that allows gamers to connect with each other with the goal of building connections and offering language exchange opportunities. 

Deployment: https://gamertalk.onrender.com/

## Table of Contents

- [Tech Stack - Backend](#tech-stack---backend)
- [Installation](#installation)
  - [Docker container](#docker-container)
  - [Run locally](#run-locally)
- [Usage](#usage)
- [API Documentation](#api-documentation)
  - User
    - [POST api/new-user](#post-apinew-user)
    - [PATCH api/edit-user](#patch-apiedit-user)
    - [GET api/filter-users](#get-apifilter-users)
    - [GET api/user-info](#get-apiuser-info)
    - [DELETE api/delete-user](#delete-apidelete-user)
  - Posts
    - [POST api/new-post](#post-apinew-post)
    - [GET api/get-posts](#get-apiget-posts)
  - Flashcards
    - [POST api/new-flashcard](#post-apinew-flashcard)
    - [GET api/get-flashcards](#get-apiget-flashcards)
    - [DELETE api/delete-flashcard](#delete-apidelete-flashcard)
- [Contributing](#contributing)
- [License](#license)

## Tech Stack - Backend

| Task | Tech |
| ---------- | ----------|
| Language | ![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white) |
| Framework | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) |
| Database | ![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) |
| Container |![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)|
<!-- | Testing Framwork | to be completed | -->

Click [here](https://github.com/GamerTalk/Frontend#tech-stack---frontend) for the Frontend Tech Stack.

## Installation

1. Clone the repository or create your own fork of the project:

   ```bash
   git clone https://github.com/GamerTalk/Backend.git

   ```

If you forked the project, you will need to get the link for your own fork.

Next, chose to either run the backend in a docker container or locally on your own machine

### Docker container

2. Copy the contents of the `.envexample` file into a `.env` file. 

3. Run the following command from your application root directory

```
docker-compose build
```

```
docker-compose up
```
or (run as deamon)
```
docker-compose up -d
```

If you need to rebuild the container:
```
docker-compose up --build
```

Migrate Django database:
```
docker-compose exec app python manage.py migrate
```

To import test database:
```
docker-compose exec app python manage.py loaddata fixtures/testusers.json
```

### Run locally

Optional but recommended: create a virtual dev environment at the root level.
2. Install dependencies:
    
    ```bash
    
    pip install -r requirements.txt

    ```

3.  Create a `.env` file at the root level of the project. Use the `.env.example` file for what environment variables are required. 
    
4. Set up the database. This command with create a db.sqlite3 file in the config folder.
    
    ```bash
    
    python manage.py migrate
    
    ```

5. Optional, load test users to database

    ```bash
    python manage.py loaddata fixtures/testusers.json 
    ```
    

## **Usage**

1. (Not necessary for Docker) Start the development server:
    
    ```bash
    
    python manage.py runserver
    
    ```
    
2. Open your browser and go to **`http://localhost:8000/`** to access the application.

## **API Documentation**

### `POST api/new-user`

 **Description:** Creates the user information entry into the database.
  
- **Body Parameters:**
  
    ```json
    {
        "uid": "string",
        "username": "string",
        "about_me": "string",
        "fluent": ["string", "string"],
        "learning": [{"language":"string", "level": 1}, ...],
        "date_of_birth": "1999-01-01",
        "systems": ["string","string"],
        "genre": ["string", "string"],
        "currently_playing": "string",
        "region": "string"
        "profile_picture_url": "urlstring"
    }
    ```
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    
    ```json
    {
        "uid": "uid",
        "username": "username",
        "about_me": "about_me",
        "fluent": "array",
        "learning": "array of object",
        "date_of_birth": "date_of_birth",
        "languages_column": "JSON",
        "systems": "user_systems",
        "genre": "genre",
        "region": "region"
    }
    ```

### `PATCH api/edit-user`

**Description:** Updates the user information entry into the database.

- **Body Parameters:**
  
    ```json
    {
        "uid": "string",
        "username": "string",
        "about_me": "string",
        "fluent": ["string", "string"],
        "learning": [{"language":"string", "level": 1}, ...],
        "date_of_birth": "1999-01-01",
        "systems": ["string","string"],
        "genre": ["string", "string"],
        "currently_playing": "string",
        "region": "string"
        "profile_picture_url": "urlstring"
    }
    ```
- **Response:**
  
  - **Status Code**: 200 (OK)
  - **Response Body**:
    
    ```json
    {
        "uid": "uid",
        "username": "username",
        "about_me": "about_me",
        "fluent": "array",
        "learning": "array of object",
        "date_of_birth": "date_of_birth",
        "languages_column": "JSON",
        "systems": "user_systems",
        "genre": "genre",
        "region": "region"
    }
    ```

### `GET api/filter-users`

**Description:** Takes in the filter parameters in the header and returns an array of users that fit said parameters

- **Header Parameters:**
    ```json
    {
        "systems":["playstation", "switch"],
        "genre":["shooters", "rpg"],
        "language": "japanese",
        "regions": ["north america"] 
    }
    ```
    
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    
    ```json
    [
        {
            "uid": "uid",
            "username": "username",
            "about_me": "about_me",
            "fluent": "array",
            "learning": "array of object",
            "date_of_birth": "date_of_birth",
            "languages_column": "JSON",
            "systems": "user_systems",
            "genre": "genre",
            "region": "region"
        },
        ...
    ]
    ```

### `GET api/user-info`

**Description:** Takes in the users uid parameter in the header and returns the user object

- **Header Parameters:**
    ```json
    {
        "uid":"string"
    }
    ```
    
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    
    ```json
    {
        "uid": "uid",
        "username": "username",
        "about_me": "about_me",
        "fluent": "array",
        "learning": "array of object",
        "date_of_birth": "date_of_birth",
        "languages_column": "JSON",
        "systems": "user_systems",
        "genre": "genre",
        "region": "region"
    },
    ```

### `DELETE api/delete-user`

 **Description:** Takes in the users uid parameter in the body with a confirmation code, and returns the user object
 
- **Body Parameters:**
    ```json
    {
        "uid": "user uid",
        "secretCode": "unique code"
    }
    ```
- **Response:**
  - **Status Code**: 200 (OK) || 400 (user doesn't exist)
  - **Response Body**:"success or failure string"
   

### `POST api/new-post`

 **Description:** Takes in the users post in the body and stores it in the database.
 
- **Body Parameters:**
    ```json
    {
        "uid": "uid",
        "message":"message",
        "time_of_message": "2015-03-25T12:00:00Z" 
    }
    ```
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    {
        "uid": "uid",
        "message":"message",
        "time_of_message": "2015-03-25T12:00:00Z" 
    }
    ```

### `GET api/get-posts`

**Description:** Returns an array of all public users post.

- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    [
        {
            "uid": "uid",
            "message":"message",
            "time_of_message": "2015-03-25T12:00:00Z" 
        },
        ...
    ]
    ```

###  `POST api/new-flashcard`

**Description:** Takes in the new flashcard information in the body and stores it in the flashcard database.

- **Body Parameters:**
    ```json
    {
        "uid": "uid",
        "front":"language1",
        "back": "language2" 
    }
    ```
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    {
        "user_uid": "uid",
        "front":"language1",
        "back": "language2" 
    }
    ```

### `GET api/get-flashcards`

 **Description:** Takes in the users uid in the header, and returns all users flashcards as an array.
 
- **Header Parameters:**
    ```json
    {
        "uid": "uid"
    }
    ```
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    [
        {
            "user_uid": "uid",
            "front":"language1",
            "back": "language2" 
        },
        ...
    ]
    ```

### `DELETE api/delete-flashcard`

 **Description:** Takes in the users uid and the cards id, and deletes it from the database.
 
- **Header Parameters:**
    ```json
    {
        "uid": "uid",
        "card_id": "Card id number"
    }
    ```
- **Response:**
  - **Status Code**: 200 (OK)
  - **Response Body**:
    ```json
    True
    ```


## **Contributing**

Contributions are welcome! Please follow these steps to contribute to the project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request with a clear description of your changes.

## **License**
MIT License

Copyright © 2023 GamerTalk

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
