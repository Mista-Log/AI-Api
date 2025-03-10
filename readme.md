# AI-Api

## Project Setup

Follow these instructions to set up the project on your local machine.

### Prerequisites

- Python (v3.8 or higher)
- pip
- Git

### Installation

1. Clone the repository:
    ```sh
    git clone git@github.com:Mista-Log/AI-Api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd AI-Api
    ```
3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `.env` file in the root directory and add your environment variables:
    ```sh
    cp .env.example .env
    ```
2. Update the `.env` file with your configuration settings.

### Running the Project

1. Apply the migrations:
    ```sh
    python manage.py migrate
    ```
2. Start the development server:
    ```sh
    python manage.py runserver
    ```
3. The server will start on `http://localhost:8000`.

## Using the API

### Endpoints

- **GET /api/chat/**
    - Description: Sends and Get response from the AI.
    - Response: 
        ```json

        {
            "response": "Hello, how can I helpyou today?"
        }

        ```

- **POST /api/chat/**
    - Description: Creates a new resource.
    - Request Body:
        ```json
        {
            "user_input": " "
        }
        ```
### Error Handling

- **400 Bad Request**: The request could not be understood or was missing required parameters.
- **404 Not Found**: Resource was not found.
- **500 Internal Server Error**: An error occurred on the server.

