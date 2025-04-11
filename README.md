# University Review Platform API

A RESTful API that allows students to share honest reviews about universities. The platform helps prospective students make more informed decisions about their education by accessing authentic reviews from current and former students.

## Features

- **User Authentication System**
  - User registration and login
  - Token-based authentication
  - Different user types (student, alumni, staff, public)

- **University Database**
  - List of universities with basic information
  - Search universities by name or country
  - University details with aggregate ratings

- **Review System**
  - Create, read, update, and delete reviews
  - Star rating system (1-5 stars)
  - Text reviews with date tracking

- **Search and Filter Functionality**
  - Find universities by name or country
  - Filter reviews by rating
  - Sort reviews by date or rating

## API Endpoints

### Authentication

- `POST /api/users/auth/register/` - Register a new user
- `POST /api/users/auth/login/` - Login and receive authentication token

### Universities

- `GET /api/universities/` - List all universities
- `GET /api/universities/{id}/` - Get university details
- `GET /api/universities/{id}/reviews/` - Get reviews for a university

### Reviews

- `POST /api/reviews/` - Create a new review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update a review
- `DELETE /api/reviews/{id}/` - Delete a review
- `GET /api/reviews/search/` - Search for reviews

### User Management

- `GET /api/users/profile/` - Get current user profile
- `PUT /api/users/profile/` - Update user profile
- `GET /api/users/reviews/` - Get reviews by current user

## Installation and Setup

1. Clone the repository:
git clone https://github.com/damitheswitch/university-review-platform-api.git
cd university-review-platform-api

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Navigate to the project directory:
cd university_review_api

5. Run migrations:
python manage.py migrate

6. Import university data:
python manage.py import_universities

7. Create a superuser (admin):
python manage.py createsuperuser

8. Run the development server:
python manage.py runserver

The API will be available at `http://127.0.0.1:8000/api/`.

## Testing with Postman

You can use Postman to test the API endpoints. Import the provided Postman collection file to get started.

## Technologies Used

- Django
- Django REST Framework
- SQLite (development) / PostgreSQL (production)
- Token Authentication

## License

This project is licensed under the MIT License - see the LICENSE file for details.