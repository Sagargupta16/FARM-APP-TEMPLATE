# FARM Stack Template

A simple and clean template for building full-stack applications using the FARM stack:
- **F**astAPI (Python backend)
- **R**eact (Frontend)
- **M**ongoDB (Database)

## ✨ Features

- 🚀 FastAPI backend with automatic API documentation
- ⚛️ React frontend with modern hooks
- 🍃 MongoDB integration with Motor (async driver)
- 🐳 Docker and Docker Compose support
- 📝 Example CRUD operations
- 🎨 Clean and simple UI
- 🔧 Easy development setup

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 16+
- MongoDB (or use Docker)
- Git

### Method 1: Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd FARM-APP-TEMPLATE
   ```

2. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

3. **Access the application**
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Frontend: Build and serve (see below)

### Method 2: Manual Setup

1. **Clone and setup backend**
   ```bash
   git clone <your-repo-url>
   cd FARM-APP-TEMPLATE
   
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Start MongoDB (locally or update config/secrets.yml)
   
   # Run the backend
   uvicorn main:app --reload
   ```

2. **Setup frontend**
   ```bash
   cd client
   npm install
   npm start  # For development
   # OR
   npm run build  # For production (builds to ../client_build)
   ```

## 📁 Project Structure

```
FARM-APP-TEMPLATE/
├── main.py                 # FastAPI main application
├── requirements.txt        # Python dependencies
├── docker-compose.yml      # Docker services configuration
├── Dockerfile             # Backend container configuration
├── .env.example           # Environment variables template
│
├── config/
│   ├── secrets.yml        # Configuration file
│   └── secrets_parser.py  # Configuration parser
│
├── models/
│   └── abc_models.py      # Pydantic models
│
├── routes/
│   └── abc_routes.py      # API route handlers
│
├── services/
│   └── abc_services.py    # Business logic layer
│
├── client/                # React frontend
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js         # Main React component
│       ├── App.css        # Styling
│       └── ...
│
└── tests/
    └── abc_test.py        # Test files
```

## 🔧 Configuration

### Database Configuration

Edit `config/secrets.yml`:

```yaml
mongodb:
  host: localhost
  port: 27017
  database: farm_template
  # Optional authentication:
  # username: your_username
  # password: your_password
```

### Environment Variables

Copy `.env.example` to `.env` and modify as needed:

```bash
cp .env.example .env
```

## 📚 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Example API Endpoints

- `GET /api/v1/users` - Get all users
- `POST /api/v1/users` - Create a new user
- `GET /api/v1/users/{user_id}` - Get user by ID
- `DELETE /api/v1/users/{user_id}` - Delete user
- `GET /health` - Health check

## 🧪 Development

### Adding New Features

1. **Add a new model** in `models/` (e.g., `product_model.py`)
2. **Create service logic** in `services/` (e.g., `product_service.py`)
3. **Add API routes** in `routes/` (e.g., `product_routes.py`)
4. **Include router** in `main.py`
5. **Update frontend** in `client/src/`

### Running Tests

```bash
# Backend tests
python -m pytest tests/

# Frontend tests
cd client
npm test
```

## 🐳 Docker Commands

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild and start
docker-compose up --build
```

## 📝 Common Tasks

### Install New Python Packages

```bash
pip install package_name
pip freeze > requirements.txt
```

### Install New React Packages

```bash
cd client
npm install package_name
```

### Database Operations

The template includes basic CRUD operations. Check `services/abc_services.py` for examples.

## 🔍 Troubleshooting

### Backend Issues

- **Import errors**: Make sure all dependencies are installed (`pip install -r requirements.txt`)
- **Database connection**: Check MongoDB is running and config/secrets.yml is correct
- **Port conflicts**: Change port in docker-compose.yml or when running uvicorn

### Frontend Issues

- **API connection**: Ensure backend is running on http://localhost:8000
- **Build issues**: Delete `node_modules` and run `npm install` again
- **CORS errors**: Check CORS configuration in main.py

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🚀 Deployment

### Production Considerations

- Use environment variables for sensitive data
- Set up proper logging
- Configure reverse proxy (nginx)
- Use production MongoDB instance
- Build React app for production
- Set up monitoring and health checks

---

**Happy coding!** 🎉

For questions or issues, please open an issue in the repository.
