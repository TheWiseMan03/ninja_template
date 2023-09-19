# Project Structure


This file contains a hierarchical representation of the project's repositories and files, making it easy to navigate through its structure and understand what tasks are included in the project and how they relate to each other.

## Project Tree

- :file_folder: ddd 
- :file_folder: docs 
- :file_folder: lib 
- :file_folder: logs 
- :file_folder: src 


 ### ddd

- :open_file_folder: ddd
    - `__init__.py`
    - `asgi.py`
    - `settings.py`
    - `urls.py`
    - `wsgi.py`

This is the directory containing configuration files and project settings

### docs

**docs** used to store project documentation. Within this directory are files and resources designed to document various aspects of the project.

### lib

- :open_file_folder: lib
    - `__init__.py`
    - `controller.py`
    - `crud.py`
    - `error.py`
    - `import_folder.py`
    - `jwt.py`
    - `logger.py`
    - `paginator.py`
    - `renderer.py`
    - `schema.py`

The **lib** directory contains the components needed to make the application work. Inside "lib" are utilities and helper functions intended for use in various parts of the project. This organization makes it easier to manage and maintain code because the central location of such functional elements makes them accessible and reusable across different parts of the application.

### logs

**logs** is used to record and store logs. Logs are records or messages that are generated when various operations are performed in an application. They contain information about events, errors, warnings, and other debugging and informational messages.

### src

- :open_file_folder: src
    - :file_folder: api
    - :file_folder: aps
        
The **src** directory is used to store source codes. This directory contains files that contain the program code necessary to develop the application.


- :open_file_folder: api
    - :open_file_folder: candidate
        - `create.py`
        - `delete.py`
        - `get.py`
        - `list.py`
        - `patch.py`
    - :open_file_folder: user
        - `login.py`
        - `logout.py`

The `api` directory contains business logic for the `user`, `candidate` application


- :open_file_folder: apps
    - :open_file_folder: candidate
        - :open_file_folder: filters
            -   `candidate.py`
        - :file_folder: migrations
        - :open_file_folder: models
            - `candidate.py`
        - :open_file_folder: schemas
            - `candidate.py`
        - :open_file_folder: services
            - `crud.py`
        - `__init__.py`
        - `admin.py`
        - `apps.py`
    - :open_file_folder: user
        - :file_folder: migrations
        - :open_file_folder: schemas
            - `candidate.py`
        - `__init__.py`
        - `admin.py`
        - `apps.py`
        - `models.py`


The `apps` directory represents individual applications within our project
