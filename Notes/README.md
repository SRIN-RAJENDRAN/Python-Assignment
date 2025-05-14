#INSTALL DEPENDENCIES
    =>FASTAPI 
        Syntax for pip insall fastapi
    =>UVICORN
        Syntax for pip insall uvicorn
    =>SQLALCHEMY
        Syntax for pip insall sqlalchemy
    =>PYDANTIC
        Syntax for pip insall pydantic

Run the Application 
    uvicorn main:api --reload
    uvicorn: This is a command-line tool. Uvicorn is a fast ASGI server. 
      
    main: The main application code is in a file named main.py.

    api: This is the name of the FastAPI application object within your Python file.

    --reload: This is an optional flag. If you modify and save any of your Python files, Uvicorn will automatically restart the server. 

Database (SQlite)
     creates a file name notesdatabase.db in the same directory.
 
Requirements 
    CRUD Functionality
          =>Create 
            POST API METHOD FOR CREATING A NEW NOTES 

          =>Read 
            GET API METHOD FOR READING A NEW NOTES 
                the

          =>Update
            PUT API METHOD FOR UPDATING A NEW NOTES 

          =>Delete
            DELETE API METHOD FOR DELETING A NEW NOTES 

Fast API url are  http://127.0.0.1:8000/
     By this url we have used for the CRUD Operation 
     
Api End points

    In the Api Tools are Postman
    GET 
        If you want retrieve list of the notes for endpoints are:(/notes/)
        If you want retrieve specific note by its ID endpoints are:(/notes/{note_id})

    POST
        If you want creating a notes for endpoints are:(/notes/)

    PUT
        If you want update specific note by its ID endpoints are:(/notes/{note_id})
       
    DELETE
        If you want delete specific note by its ID endpoints are:(/notes/{note_id})
 