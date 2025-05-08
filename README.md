# RestAPI_withFlask_SQLite

# REST API with Flask and SQLite

This project demonstrates how to create a RESTful API using **Flask** and **SQLite**. The API supports basic CRUD operations (Create, Read, Update, Delete) for managing data stored in a SQLite database.

---

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on the database.
- **Flask Framework**: Leverages Flask for routing and handling HTTP requests.
- **SQLite Database**: Simple and lightweight database for storing persistent data.
- **JSON Responses**: Communicates data using JSON format.

---

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/olivicegodwin467/RestAPI_withFlask_SQLite.git
2. Navigate to the Project Directory
bash
Copy
Edit
cd RestAPI_withFlask_SQLite
3. Install Dependencies
Ensure you have Python 3.x installed, then install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the Application
Run the Flask application:

bash
Copy
Edit
python app.py
The application will start, and the API will be accessible at http://127.0.0.1:5000.

Endpoints
Here is a summary of the API endpoints:

1. Retrieve All Records
Endpoint: GET /items

Description: Retrieves all items from the database.

2. Retrieve a Single Record
Endpoint: GET /items/<id>

Description: Retrieves an item by its ID.

Example: GET /items/1

3. Create a New Record
Endpoint: POST /items

Description: Adds a new item to the database.

Body: JSON object containing the new item details.

Example:

json
Copy
Edit
{
    "name": "Example Item",
    "price": 12.99
}
4. Update an Existing Record
Endpoint: PUT /items/<id>

Description: Updates the details of an existing item.

Body: JSON object containing updated details.

Example:

json
Copy
Edit
{
    "name": "Updated Item",
    "price": 15.49
}
5. Delete a Record
Endpoint: DELETE /items/<id>

Description: Deletes an item by its ID.

File Structure
bash
Copy
Edit
RestAPI_withFlask_SQLite/
│
├── app.py              # Main Flask application
├── database.db         # SQLite database file
├── models.py           # Database models (if applicable)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
