# Ishan Best Delivery Route Planner

## Overview

This project helps a delivery executive determine the best route to deliver orders in the shortest possible time. It uses the Haversine formula to calculate distances between geo-locations and considers preparation times at restaurants.

## File Structure

- `main.py`: Main execution flow with sample input.
- `models/`: Contains the core classes for geo-locations, orders, and route planning.
- `utils.py`: Utility functions like calculating haversine distance.
- `exceptions.py`: Custom Exceptions.
- `constants.py`: contains all constants used or assumed.
- `tests/`: Unit tests.

## How to Run

1. Run Main File
   ```python3 main.py

2. Run unit tests
   ```python3 -m unittest discover -s tests
