# SARB AI API

This is the AI backend service for the SARB (Saudi Arabia Ride Booking) car sharing platform. It provides various AI-powered endpoints to enhance the car sharing experience.

## Features

- **Data APIs**: Endpoints to access car, user, booking, event, and market data
- **AI Services**: Predictive analytics and recommendation systems
- **External Data Integration**: Connects to the main SARB API for real car, user, and market price data
- **Dummy Data**: Auto-generated realistic data for development and testing when external API is unavailable
- **RESTful API**: Built with FastAPI for high performance and easy integration

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **For deployment environments (to avoid compilation issues)**:
   ```bash
   pip install -r requirements.txt -c constraints.txt
   ```

3. **Run the server**:
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API docs**:
   - Interactive API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

### Data APIs

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cars` | GET | Get all available cars (from external SARB API) |
| `/api/users` | GET | Get all users (from external SARB API) |
| `/api/bookings` | GET | Get all bookings (from external SARB API) |
| `/api/events` | GET | Get upcoming events |
| `/api/market/average-prices` | GET | Get average market prices by car type (from external SARB API) |
| `/api/mapview` | GET | Get map view data with car availability |

### AI Services

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/ai/forecast-demand/{area_id}` | GET | Forecast car demand for an area |
| `/api/ai/recommend-price/{car_id}` | GET | Get price recommendation for a car |
| `/api/ai/map-insights/{area_id}` | GET | Get insights for a specific area |
| `/api/ai/can-cancel/{booking_id}` | GET | Check if a booking can be cancelled |
| `/api/ai/recommend-cars/{user_id}` | GET | Get car recommendations for a user |
| `/api/ai/recommend-areas/{user_id}` | GET | Get area recommendations for a user |
| `/api/ai/hotspot-prediction` | GET | Predict demand hotspots across all areas |
| `/api/ai/recommend-initial-price` | GET | Recommend initial pricing for new car listings |
| `/api/ai/host-notifications/{host_id}` | GET | Send smart notifications to hosts about high-demand periods |

## Data Models

### Car
```json
{
  "id": 1,
  "type": "Sedan",
  "model": "Camry",
  "year": 2022,
  "price_per_day": 199.99,
  "location": "Riyadh",
  "availability": true
}
```

### User
```json
{
  "id": 1,
  "name": "Ahmed Al-Saud"
}
```

### Booking
```json
{
  "id": 1,
  "car_id": 5,
  "user_id": 3,
  "start_date": "2023-06-15",
  "end_date": "2023-06-18",
  "price_paid": 599.97,
  "status": "confirmed"
}
```

### MarketPrice
```json
{
  "car_type": "Sedan",
  "average_price": 120.26
}
```

## External API Integration

This service integrates with the main SARB API to fetch real data:
- **Car Endpoint**: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car`
- **User Endpoint**: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/user`
- **Market Prices Endpoint**: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car/average-price`
- **Booking Endpoint**: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/booking`
- **Authentication**: Bearer token authentication
- **Data Transformation**: External data is transformed to match our internal models

## Development

- The application uses FastAPI with Pydantic for data validation
- Dummy data is generated on startup and persisted to `dummy_data.json`
- The API follows RESTful principles and returns JSON responses

## Deployment

For production deployment, consider using:
- Gunicorn with Uvicorn workers
- Environment variables for configuration
- A proper database (PostgreSQL recommended)
- Caching layer (Redis)

## License

This project is licensed under the MIT License.