# SARB AI Services Guide

This document provides a comprehensive overview of all AI services available in the SARB car sharing platform, explaining how each service works and how to use them.

## Table of Contents
1. [AI Demand Forecasting](#ai-demand-forecasting)
2. [AI Pricing Optimization](#ai-pricing-optimization)
3. [AI Notifications](#ai-notifications)
4. [Algorithm 1: Initial Pricing Recommendation](#algorithm-1-initial-pricing-recommendation)
5. [Algorithm 2: Cancellation Policy](#algorithm-2-cancellation-policy)
6. [Additional AI Services](#additional-ai-services)

## AI Demand Forecasting

### Endpoint
```
GET /api/ai/forecast-demand/{area_id}
```

### Purpose
Analyzes historical data to predict periods of high car demand and the impact of events and seasons.

### Data Analysis
- **Historical Booking Data**: Analyzes past booking patterns
- **Seasonal Trends**: Identifies seasonal demand patterns
- **User Behaviors**: Tracks user booking preferences and patterns

### How It Works
The system uses current booking data and map view information to calculate demand factors for specific areas. It identifies peak dates when demand is expected to be high.

### Usage Example
```bash
curl "http://localhost:8000/api/ai/forecast-demand/1"
```

### Response
```json
{
  "area_id": 1,
  "expected_demand": 0.75,
  "peak_dates": ["2025-10-15", "2025-10-16", "2025-10-20"]
}
```

### Application Integration
- Display demand forecasts on the map interface
- Highlight high-demand periods in the booking calendar
- Send proactive notifications to hosts about upcoming busy periods

## AI Pricing Optimization

### Endpoint
```
GET /api/ai/recommend-price/{car_id}
```

### Purpose
Suggests optimal prices for hosts based on market comparisons and booking performance.

### Data Analysis
- **Similar Cars Comparison**: Compares with similar cars in the same area
- **Booking Performance**: Analyzes booking rates of other cars
- **Forecasted Demand**: Factors in expected demand levels

### How It Works
The system fetches current car data, market prices, and booking information to calculate an optimal price that helps hosts stay competitive while maximizing profits.

### Usage Example
```bash
curl "http://localhost:8000/api/ai/recommend-price/38"
```

### Response
```json
{
  "car_id": 38,
  "current_price": 3000.0,
  "recommended_price": 3300.0,
  "reason": "Based on 2 recent bookings"
}
```

### Application Integration
- Show price recommendations in the host dashboard
- Provide pricing suggestions when hosts update their car listings
- Display comparison with market average prices

## AI Notifications

### Endpoint
```
GET /api/ai/host-notifications/{host_id}
```

### Purpose
Sends alerts to hosts about upcoming high-demand periods to encourage car availability.

### Data Analysis
- **Demand Forecasting**: Uses hotspot prediction data
- **Seasonal Patterns**: Identifies seasonal opportunities
- **Host Car Utilization**: Analyzes current car booking rates

### How It Works
The system analyzes demand forecasts and seasonal trends to identify periods when hosts should make their cars available for maximum bookings and profits.

### Usage Example
```bash
curl "http://localhost:8000/api/ai/host-notifications/15"
```

### Response
```json
{
  "host_id": 15,
  "demand_notifications": [
    {
      "date": "2025-10-15",
      "message": "High demand expected on 2025-10-15. Consider making your cars available for better profits.",
      "utilization_rate": 0.3,
      "potential_revenue_increase": "50% potential increase"
    }
  ],
  "seasonal_notifications": [
    {
      "period": "Summer Season",
      "message": "Summer is peak season for car rentals. Consider adjusting prices upward.",
      "recommendation": "Increase prices by 10-20% during peak summer months"
    }
  ],
  "total_cars": 5
}
```

### Application Integration
- Send push notifications to host mobile apps
- Display notifications in the host dashboard
- Email alerts about high-demand periods

## Algorithm 1: Initial Pricing Recommendation

### Endpoint
```
GET /api/ai/recommend-initial-price?car_type={type}&location={location}
```

### Purpose
Recommends initial pricing when listing a new car by comparing similar vehicles in the same area.

### Data Analysis
- **Similar Cars Comparison**: Analyzes cars of the same type in the same location
- **Booking Rates**: Examines booking performance of comparable vehicles
- **Market Averages**: Considers overall market pricing for car types

### How It Works
When a host lists a new car, the system compares it with similar cars in the area and market averages to suggest an optimal initial price.

### Usage Example
```bash
curl "http://localhost:8000/api/ai/recommend-initial-price?car_type=Sedan&location=Riyadh"
```

### Response
```json
{
  "car_type": "Sedan",
  "location": "Riyadh",
  "market_average_price": 150.0,
  "similar_cars_count": 3,
  "recommended_initial_price": 142.5,
  "reason": "Based on market average of 150.0 and 3 similar cars in the area"
}
```

### Application Integration
- Provide pricing suggestions during car listing creation
- Show comparison with similar cars in the area
- Display market average pricing information

## Algorithm 2: Cancellation Policy

### Endpoint
```
GET /api/ai/can-cancel/{booking_id}
```

### Purpose
Applies a clear 24-hour cancellation policy to ensure transparent terms.

### Data Analysis
- **Booking Time**: Calculates time until booking start
- **Policy Rules**: Enforces 24-hour cancellation window

### How It Works
The system checks if a booking can be cancelled based on the 24-hour policy before the booking start time.

### Usage Example
```bash
curl "http://localhost:8000/api/ai/can-cancel/52"
```

### Response
```json
{
  "booking_id": 52,
  "can_cancel": true,
  "reason": "Can cancel up to 24 hours before the booking starts"
}
```

### Application Integration
- Display cancellation eligibility in user booking details
- Prevent cancellations that violate the policy
- Show clear cancellation terms during booking

## Additional AI Services

### Car Recommendations
```
GET /api/ai/recommend-cars/{user_id}
```
Provides personalized car recommendations for users based on preferences.

### Area Recommendations
```
GET /api/ai/recommend-areas/{user_id}
```
Suggests optimal areas for users based on availability and pricing.

### Map Insights
```
GET /api/ai/map-insights/{area_id}
```
Provides detailed insights for specific map areas including utilization rates.

### Hotspot Prediction
```
GET /api/ai/hotspot-prediction
```
Identifies demand hotspots across all areas for strategic planning.

## Integration Guidelines

### Real-time Data
All AI services fetch real-time data from external APIs to ensure accuracy:
- Cars data from: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car`
- Users data from: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/user`
- Bookings data from: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/booking`
- Market prices from: `https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car/average-price`

### Authentication
All external API calls use Bearer token authentication:
```
Authorization: Bearer 28|KKyjTwdNzLQBjb44Iw8ZCabGjr9zWVIiMfIXQVQS36aa992f
```

### Error Handling
Services include proper error handling for:
- Missing data
- API connectivity issues
- Invalid parameters
- Resource not found scenarios

## Best Practices for Implementation

1. **Cache Results**: Cache AI service responses to reduce API calls
2. **Handle Errors Gracefully**: Implement fallback mechanisms for service failures
3. **Update UI in Real-time**: Refresh recommendations when underlying data changes
4. **Provide Context**: Show users why recommendations are made
5. **Respect User Privacy**: Only use data necessary for AI calculations

## Testing

All services can be tested using the provided test scripts:
- `test_new_ai_services.py` - Tests new AI services
- `complete_ai_test.py` - Comprehensive test of all AI services
- Individual curl commands as shown in the examples above