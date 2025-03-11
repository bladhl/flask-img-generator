# Flask CRUD + OpenAI Image Generation API

## Overview

This is a microservice built with **Flask**, following best practices for a structured and scalable architecture. It includes:

- **User Management (CRUD)**: Create, read, update, and delete users using SQLite.
- **Image Generation**: Uses **OpenAI's DALL·E API** to generate images based on a text prompt.
- **RESTful API**: Well-structured endpoints for easy integration.
- **Modular Architecture**: Organized into routes, services, and models.
- **Flask-Migrate**: Supports database migrations.

## Tech Stack

- **Flask** (Micro web framework)
- **SQLite** (Database)
- **SQLAlchemy** (ORM)
- **Flask-Migrate** (Database migrations)
- **OpenAI API** (Image generation)
- **Python 3.x**

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/flask-img-generator.git
cd flask-img-generator
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add:

```
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=supersecretkey
SQLALCHEMY_DATABASE_URI=sqlite:///database.db
OPENAI_API_KEY=your_openai_api_key
```

### 5. Initialize and Apply Database Migrations

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the Application

```sh
flask run
```

## API Endpoints

### User Management (CRUD)

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/users/`     | Get all users       |
| GET    | `/users/<id>` | Get user by ID      |
| POST   | `/users/`     | Create a new user   |
| PUT    | `/users/<id>` | Update user details |
| DELETE | `/users/<id>` | Delete a user       |

### Image Generation

| Method | Endpoint           | Description                          |
| ------ | ------------------ | ------------------------------------ |
| POST   | `/generate-image/` | Generate an image from a text prompt |

#### Example Request (Image Generation)

```sh
curl -X POST http://127.0.0.1:5000/generate-image/ -H "Content-Type: application/json" -d '{"prompt": "A futuristic cityscape"}'
```

#### Example Response

```json
{
  "image_url": "https://openai.com/generated-image-url.jpg"
}
```

## Contributing

Feel free to fork this repository and submit pull requests. Ensure that all changes are well-documented and tested.

## License

This project is licensed under the MIT License.

