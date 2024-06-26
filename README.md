
"Register and view restaurants on a map. This Django-based web application allows users to register new restaurants, specifying their names, opening times, and locations via latitude and longitude. The map interface visually displays all registered restaurants, providing a convenient overview of their geographical distribution."

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd csv_analysis_project
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python restaurants_project/manage.py makemigrations
    python restaurants_project/manage.py migrate
    ```

5. Start the development server:
    ```sh
    python restaurants_project/manage.py runserver
    ```

6. Open a web browser and navigate to `http://127.0.0.1:8000/' to Register and View Restaurants

Admin Panel:
    Username = 'admin'
    password = 'admin'

Or You Can use Docker also

    Docker Setup
    Alternatively, you can use Docker for simplified setup:

    1.Build and run the Docker containers:
    
        docker-compose up --build   #Run this command 

    2.Open a web browser and navigate to `http://127.0.0.1:8000/' to Register and View Restaurants

