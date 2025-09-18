<p align="center">
  <img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="AirBnB Clone Logo" width="200">
</p>

<h1 align="center">AirBnB Clone - Version 2</h1>
<p align="center">An enhanced web application that replicates the core functionality of AirBnB</p>

---

## 📋 Table of Contents

- [Description](#description)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Console Commands](#console-commands)
- [Testing](#testing)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## 📖 Description

AirBnB Clone V2 is a comprehensive web application that replicates the core functionalities of AirBnB. This version builds upon the foundation of the original console-based project, introducing enhanced features including:

- Database integration with SQLAlchemy ORM
- Web framework implementation using Flask
- RESTful API endpoints
- Enhanced data models and relationships
- File and database storage engines
- Web static content serving
- Template rendering with Jinja2

The project serves as a learning platform for full-stack web development, covering backend logic, database management, API design, and frontend integration.

## ✨ Features

### Version 2 Enhancements:
- **Database Integration**: MySQL support with SQLAlchemy ORM
- **Web Framework**: Flask-based web server
- **RESTful API**: Complete API with CRUD operations
- **Multiple Storage Engines**: FileStorage and DBStorage
- **Web Interface**: HTML/CSS frontend with dynamic content
- **Template Engine**: Jinja2 templating
- **State Management**: Advanced state and city relationships
- **User Authentication**: Enhanced user management system
- **Search & Filter**: Advanced search capabilities
- **Responsive Design**: Mobile-friendly interface

### Core Functionality:
- User registration and authentication
- Property listings (Places) with detailed information
- City and State management
- Amenity categorization
- Review and rating system
- Booking management
- Advanced search and filtering

## 🛠 Technology Stack

- **Backend**: Python 3.x
- **Web Framework**: Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Template Engine**: Jinja2
- **Frontend**: HTML5, CSS3, JavaScript
- **Storage**: JSON File Storage & MySQL Database
- **Testing**: Python unittest
- **Version Control**: Git

## 📁 Project Structure

```
AirBnB_clone_v2/
├── models/                 # Data models and storage engines
│   ├── engine/            # Storage engines (FileStorage, DBStorage)
│   ├── base_model.py      # Base class for all models
│   ├── user.py            # User model
│   ├── state.py           # State model
│   ├── city.py            # City model
│   ├── amenity.py         # Amenity model
│   ├── place.py           # Place model
│   └── review.py          # Review model
├── web_flask/             # Flask web application
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # Jinja2 templates
│   └── *.py               # Flask route handlers
├── api/                   # RESTful API
│   └── v1/                # API version 1
├── tests/                 # Unit tests
├── console.py             # Command-line interface
├── setup_mysql_dev.sql    # MySQL development setup
├── setup_mysql_test.sql   # MySQL testing setup
└── README.md              # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.4+
- MySQL 5.7+
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone https://github.com/Sirius1616/AirBnB_clone_v2.git
cd AirBnB_clone_v2
```

### 2. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Database Setup
```bash
# Start MySQL service
sudo service mysql start

# Create databases and user
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
```

### 4. Environment Configuration
```bash
# For FileStorage (default)
export HBNB_TYPE_STORAGE=file

# For Database Storage
export HBNB_TYPE_STORAGE=db
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
```

## 💻 Usage

### Console Interface
Launch the interactive console:
```bash
./console.py
```

### Web Application
Start the Flask web server:
```bash
python3 -m web_flask.0-hello_route
```
Visit `http://localhost:5000` in your browser.

### API Server
Start the RESTful API server:
```bash
python3 -m api.v1.app
```
Access API endpoints at `http://localhost:5000/api/v1/`

## 🎮 Console Commands

The console supports the following commands for object management:

### Basic Commands
- `help` - Display available commands
- `quit` or `EOF` - Exit the console

### Object Operations
- `create <class>` - Create a new instance
- `show <class> <id>` - Display an instance
- `destroy <class> <id>` - Delete an instance
- `all [class]` - Show all instances
- `update <class> <id> <attribute> <value>` - Update an instance
- `count <class>` - Count instances of a class

### Usage Examples
```bash
(hbnb) create User
4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3

(hbnb) show User 4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3
[User] (4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3) {'id': '4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3', ...}

(hbnb) update User 4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3 email "user@example.com"

(hbnb) User.all()
[User] (4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3) {'email': 'user@example.com', ...}

(hbnb) destroy User 4f32d2c8-a7ac-4e20-8f87-7b12b7d7e8c3

(hbnb) quit
```

## 🧪 Testing

### Run All Tests
```bash
python3 -m unittest discover tests
```

### Run Specific Test Modules
```bash
# Test models
python3 -m unittest tests.test_models.test_base_model

# Test console
python3 -m unittest tests.test_console

# Test web framework
python3 -m unittest tests.test_web_flask
```

### Test with Different Storage Engines
```bash
# Test with FileStorage
HBNB_TYPE_STORAGE=file python3 -m unittest discover tests

# Test with DBStorage
HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

## 🤝 Contributing

We welcome contributions to improve the AirBnB Clone V2 project!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 style guidelines
- Include docstrings for all classes and methods
- Write unit tests for new features
- Ensure all tests pass before submitting

## 👥 Authors

* **Sirius1616** - *Initial work and project development* - [Sirius1616](https://github.com/Sirius1616)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Holberton School for the project framework and learning objectives
- The AirBnB platform for inspiration
- The open-source community for tools and libraries used

---

<p align="center">
  Made with ❤️ for learning and educational purposes
</p>