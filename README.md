# AirBnB Clone v2

![AirBnB Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Airbnb_Logo_B%C3%A9lo.svg/1200px-Airbnb_Logo_B%C3%A9lo.svg.png)

## 📋 Table of Contents
- [Description](#description)
- [Environment](#environment)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
- [Storage](#storage)
- [Console Commands](#console-commands)
- [Web Framework](#web-framework)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Authors](#authors)
- [License](#license)

## 📖 Description

AirBnB Clone v2 is a complete web application that mimics the functionality of the popular vacation rental platform AirBnB. This project is part of a comprehensive software engineering curriculum and demonstrates the implementation of a full-stack web application using Python, Flask, SQLAlchemy, and other modern web technologies.

The project follows a modular approach with multiple phases:
- **Phase 1**: Command-line interface and data modeling
- **Phase 2**: Database integration and web framework
- **Phase 3**: RESTful API development
- **Phase 4**: Frontend interface

## 🌍 Environment

This project is developed and tested on Ubuntu 20.04 LTS using:
- Python 3.8+
- MySQL 8.0+
- Flask 2.0+
- SQLAlchemy 1.4+

## ✨ Features

### Core Features
- **User Management**: Registration, authentication, and profile management
- **Property Listings**: Create, read, update, and delete property listings
- **Booking System**: Make reservations and manage bookings
- **Review System**: Leave and read reviews for properties and hosts
- **Search & Filter**: Advanced search functionality with multiple filters
- **Payment Integration**: Secure payment processing (simulation)
- **Messaging**: Host-guest communication system

### Technical Features
- **Multiple Storage Engines**: File storage and MySQL database support
- **RESTful API**: Complete API for all CRUD operations
- **Web Interface**: Dynamic HTML pages with Jinja2 templating
- **Command Line Interface**: Interactive console for data manipulation
- **Unit Testing**: Comprehensive test suite
- **Data Validation**: Input validation and error handling

## 🚀 Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package installer)
- git

### Step 1: Clone the Repository
```bash
git clone https://github.com/Sirius1616/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

### Step 2: Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# For MySQL setup
mysql -u root -p
CREATE DATABASE hbnb_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### Step 5: Environment Variables
Create a `.env` file in the root directory:
```bash
# Database Configuration
HBNB_MYSQL_USER=hbnb_dev
HBNB_MYSQL_PWD=hbnb_dev_pwd
HBNB_MYSQL_HOST=localhost
HBNB_MYSQL_DB=hbnb_dev_db

# Storage Type (file or db)
HBNB_TYPE_STORAGE=db

# Environment
HBNB_ENV=dev
```

## 💻 Usage

### Starting the Console
```bash
./console.py
```

### Basic Console Commands
```bash
# Create a new user
(hbnb) create User email="user@example.com" password="password" first_name="John" last_name="Doe"

# Show all instances of a class
(hbnb) all User

# Show specific instance
(hbnb) show User <user_id>

# Update instance
(hbnb) update User <user_id> first_name "Jane"

# Delete instance
(hbnb) destroy User <user_id>
```

### Starting the Web Application
```bash
# Development server
python3 -m web_flask.0-hello_route

# Or with specific configuration
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.app
```

### API Usage
```bash
# Get all states
curl -X GET http://localhost:5000/api/v1/states

# Create a new state
curl -X POST http://localhost:5000/api/v1/states -H "Content-Type: application/json" -d '{"name": "California"}'

# Get specific state
curl -X GET http://localhost:5000/api/v1/states/<state_id>
```

## 📁 Project Structure

```
AirBnB_clone_v2/
├── console.py              # Command line interpreter
├── models/                 # Data models
│   ├── __init__.py
│   ├── base_model.py      # Base class for all models
│   ├── user.py            # User model
│   ├── place.py           # Place model
│   ├── state.py           # State model
│   ├── city.py            # City model
│   ├── amenity.py         # Amenity model
│   ├── review.py          # Review model
│   └── engine/            # Storage engines
│       ├── file_storage.py
│       └── db_storage.py
├── web_flask/             # Flask web application
│   ├── __init__.py
│   ├── 0-hello_route.py
│   ├── templates/         # HTML templates
│   └── static/           # CSS, JS, images
├── api/                   # RESTful API
│   └── v1/
│       ├── app.py
│       └── views/
├── tests/                 # Unit tests
│   ├── test_models/
│   └── test_engine/
├── setup_mysql_dev.sql    # Database setup script
├── setup_mysql_test.sql   # Test database setup
└── requirements.txt       # Python dependencies
```

## 🗃️ Models

### Core Models

#### BaseModel
- Base class for all models
- Handles serialization/deserialization
- Manages timestamps (created_at, updated_at)
- Provides save() and delete() methods

#### User
- Represents application users
- Attributes: email, password, first_name, last_name

#### State
- Represents geographical states
- Attributes: name
- Relationships: cities (one-to-many)

#### City
- Represents cities within states
- Attributes: name, state_id
- Relationships: state (many-to-one), places (one-to-many)

#### Place
- Represents rental properties
- Attributes: city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude
- Relationships: city, user, reviews, amenities

#### Amenity
- Represents property amenities
- Attributes: name
- Relationships: places (many-to-many)

#### Review
- Represents user reviews
- Attributes: place_id, user_id, text
- Relationships: place, user

## 💾 Storage

### File Storage
- JSON-based storage system
- Default storage method
- Data persisted in `file.json`

### Database Storage
- MySQL backend using SQLAlchemy ORM
- Supports relationships between models
- Configurable through environment variables

### Storage Interface
```python
# Switch between storage types
from models import storage

# Works with both file and database storage
all_users = storage.all(User)
new_user = User(email="test@example.com")
storage.new(new_user)
storage.save()
```

## 🖥️ Console Commands

The console supports the following commands:

| Command | Description | Example |
|---------|-------------|---------|
| `create` | Create new instance | `create User email="test@test.com"` |
| `show` | Display instance | `show User 1234-5678-9012` |
| `all` | Show all instances | `all` or `all User` |
| `update` | Update instance | `update User 1234-5678-9012 name "New Name"` |
| `destroy` | Delete instance | `destroy User 1234-5678-9012` |
| `count` | Count instances | `User.count()` |
| `quit` | Exit console | `quit` |
| `help` | Show help | `help` or `help create` |

### Advanced Console Usage
```bash
# Alternative syntax
(hbnb) User.all()
(hbnb) User.count()
(hbnb) User.show("1234-5678-9012")
(hbnb) User.destroy("1234-5678-9012")
(hbnb) User.update("1234-5678-9012", "name", "New Name")
(hbnb) User.update("1234-5678-9012", {"name": "New Name", "age": 25})
```

## 🌐 Web Framework

The web application is built with Flask and includes:

### Routes
- `/` - Homepage
- `/states` - List all states
- `/states/<id>` - Show specific state with cities
- `/cities_by_states` - States and their cities
- `/hbnb` - Main application interface

### Templates
- Jinja2 templating engine
- Responsive design
- Dynamic content rendering
- Template inheritance

### Static Files
- CSS stylesheets
- JavaScript functionality
- Images and icons
- Responsive layout

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python3 -m unittest discover tests

# Run specific test file
python3 -m unittest tests.test_models.test_user

# Run tests with verbose output
python3 -m unittest discover tests -v

# Test coverage
python3 -m pytest --cov=models tests/
```

### Test Structure
```
tests/
├── test_models/
│   ├── test_base_model.py
│   ├── test_user.py
│   ├── test_place.py
│   └── ...
├── test_engine/
│   ├── test_file_storage.py
│   └── test_db_storage.py
└── test_console.py
```

### Writing Tests
```python
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(email="test@test.com", password="password")
        self.assertEqual(user.email, "test@test.com")
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
```

## 🛠️ Technologies Used

### Backend
- **Python 3.8+** - Core programming language
- **Flask 2.0+** - Web framework
- **SQLAlchemy 1.4+** - ORM for database operations
- **MySQL 8.0+** - Relational database
- **Jinja2** - Templating engine

### Frontend
- **HTML5** - Markup language
- **CSS3** - Styling
- **JavaScript** - Client-side scripting
- **Bootstrap** - CSS framework (optional)

### Development Tools
- **unittest** - Python testing framework
- **pytest** - Advanced testing framework
- **pylint** - Code linting
- **autopep8** - Code formatting
- **Git** - Version control

### Deployment
- **Gunicorn** - WSGI HTTP Server
- **Nginx** - Web server and reverse proxy
- **Docker** - Containerization (optional)
- **AWS/Digital Ocean** - Cloud hosting platforms

## 👥 Authors

- **[Sirius1616](https://github.com/Sirius1616)** - Project Creator and Maintainer

### Contributors
We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📞 Contact

- **GitHub**: [@Sirius1616](https://github.com/Sirius1616)
- **Project Link**: [https://github.com/Sirius1616/AirBnB_clone_v2](https://github.com/Sirius1616/AirBnB_clone_v2)

## 🙏 Acknowledgments

- **Holberton School** - For the project inspiration and curriculum
- **AirBnB** - For the original platform concept
- **Flask Community** - For the excellent web framework
- **SQLAlchemy Team** - For the powerful ORM

---

*This project is for educational purposes and is not affiliated with, endorsed by, or connected to Airbnb, Inc.*