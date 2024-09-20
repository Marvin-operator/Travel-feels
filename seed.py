from db import session
from models import Trip, Booking

def seed_data():
    # Sample data
    trips = [
        Trip(destination='Paris', date='2024-10-01', duration=5, price=1500.0),
        Trip(destination='London', date='2024-10-10', duration=4, price=1200.0),
    ]
    
    session.bulk_save_objects(trips)
    session.commit()
    print("Sample data seeded.")

if __name__ == "__main__":
    seed_data()
