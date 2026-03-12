# RoadSense AI Architecture Specification


## System Architecture

RoadSense follows layered architecture.

Frontend layer

Backend API layer

Integration layer

Service layer

Cloud layer



## Layers


Frontend:

React UI

Upload form

Dashboard

Map display



Backend:

FastAPI server

Routes

Validation

Response formatting



Integration Layer:

integration_service.py

Connects routes to services.

Prevents direct dependency.



Service Layer:

aws_service.py

ai_service.py

location_service.py

traffic_service.py



Cloud Layer:

AWS S3

AWS DynamoDB

AWS Bedrock



## Flow

User uploads image

Route receives request

Integration service processes

AI analyzes image

AWS stores image

Record built

Response returned



## Design Rules

Routes must not call AWS directly.

Routes must not call AI directly.

Only integration service connects services.

Config must be centralized.

Responses must use utils/response.py.



## Backend Structure

backend/

app.py → entrypoint

config.py → settings

routes/ → API endpoints

services/ → business logic

models/ → data models

utils/ → helpers



## Deployment Ready Features

Health endpoint exists.

CORS enabled.

Config driven.

Modular services.

Swagger documentation.



## Future Improvements

Authentication layer

Caching layer

Queue system

Event processing

Lambda triggers



## Current Architecture Stage

Phase:

Foundation complete.

Next:

AWS integration.

AI integration.

Frontend connection.



## Architecture Goal

Goal:

Clean integration without route changes.

Services replace mocks without breaking API.

Stable demo backend.