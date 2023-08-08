# GamerTalk Backend

<img src="/public\GamerTalkWideLogo.png" alt="Header" title="Header" width="1200">

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This is the backend server of the project GamerTalk. GamerTalk is an application that allows gamers to connect with each other with the goal of building connections and offering language exchange opportunities. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/GamerTalk/Backend.git

   ```

2. Install dependencies:
    
    ```bash
    
    pip install -r requirements.txt
    
    ```

3. This application uses a local postgres database. Thus, you will have to create the database through postgres and then save the connection information to the database in a `.env` file. Use the `.env.example` file for what variables are required.
    
4. Set up the database.
    
    ```bash
    
    python manage.py migrate
    
    ```
    

## **Usage**

1. Start the development server:
    
    ```bash
    
    python manage.py runserver
    
    ```
    
2. Open your browser and go to **`http://localhost:8000/`** to access the application.

## **API Documentation**

### Endpoint 1

- **URL:** `/api/new-user/`
- **Method:** POST
- **Description:** Creates the user information entry into the database.
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
  - Status Code: 200 (OK)
  - Response Body:
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

### Endpoint 2

- **URL:** `/api/edit-user/`
- **Method:** PATCH
- **Description:** Updates the user information entry into the database.
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
  - Status Code: 200 (OK)
  - Response Body:
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

### Endpoint 3

- **URL:** `/api/filter-users/`
- **Method:** GET
- **Description:** Takes in the filter parameters in the header, and returns an array of users that fit said parameters
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
  - Status Code: 200 (OK)
  - Response Body:
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

### Endpoint 4

- **URL:** `/api/user-info/`
- **Method:** GET
- **Description:** Takes in the users uid parameter in the header, and returns the user object
- **Header Parameters:**
    ```json
    {
        "uid":"string"
    }
    ```
- **Response:**
  - Status Code: 200 (OK)
  - Response Body:
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

### Endpoint 5

- **URL:** `/api/new-post/`
- **Method:** POST
- **Description:** Takes in the users post in the body and stores it in the database.
- **Body Parameters:**
    ```json
    {
        "uid": "uid",
        "message":"message",
        "time_of_message": "2015-03-25T12:00:00Z" 
    }
    ```
- **Response:**
  - Status Code: 200 (OK)
  - Response Body:
    ```json
    {
        "uid": "uid",
        "message":"message",
        "time_of_message": "2015-03-25T12:00:00Z" 
    }
    ```

### Endpoint 6

- **URL:** `/api/get-posts/`
- **Method:** GET
- **Description:** Returns an array of all public users post.
- **Response:**
  - Status Code: 200 (OK)
  - Response Body:
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

### Endpoint 7

- **URL:** `/api/new-flashcard/`
- **Method:** POST
- **Description:** Takes in the new flashcard information in the body and stores it in the flashcard database.
- **Body Parameters:**
    ```json
    {
        "uid": "uid",
        "front":"language1",
        "back": "language2" 
    }
    ```
- **Response:**
  - Status Code: 200 (OK)
  - Response Body:
    ```json
    {
        "user_uid": "uid",
        "front":"language1",
        "back": "language2" 
    }
    ```

### Endpoint 8

- **URL:** `/api/get-flashcards/`
- **Method:** GET
- **Description:** Takes in the users uid in the header, and returns all users flashcards as an array.
- **Header Parameters:**
    ```json
    {
        "uid": "uid"
    }
    ```
- **Response:**
  - Status Code: 200 (OK)
  - Response Body:
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

### Endpoint 8

- **URL:** `/api/delete-flashcard/`
- **Method:** DELETE
- **Description:** Takes in the users uid and the cards id, and deletes it from the database.
- **Header Parameters:**
    ```json
    {
        "uid": "uid",
        "card_id": "Card id number"
    }
    ```
- **Response:**
  - Status Code: 200 (OK)
  - Response Body:
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

Include information about the license under which your project is distributed. You can replace **`LICENSE`** with the actual name of your license file.