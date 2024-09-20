from db import session
from models import Trip, Booking

def create_trip():
    destination = input("Enter trip destination: ")
    date = input("Enter trip date (YYYY-MM-DD): ")
    duration = int(input("Enter trip duration (days): "))
    price = float(input("Enter trip price: "))
    
    new_trip = Trip(destination=destination, date=date, duration=duration, price=price)
    session.add(new_trip)
    session.commit()
    print("Trip created successfully.")

def book_trip():
    trip_id = int(input("Enter trip ID to book: "))
    customer_name = input("Enter your name: ")
    
    new_booking = Booking(trip_id=trip_id, customer_name=customer_name)
    session.add(new_booking)
    session.commit()
    print("Trip booked successfully.")

def view_trips():
    trips = session.query(Trip).all()
    for trip in trips:
        print(f"{trip.id}: {trip.destination} on {trip.date}, Duration: {trip.duration} days, Price: {trip.price}")

def search_trips():
    destination = input("Enter destination to search: ")
    trips = session.query(Trip).filter(Trip.destination.ilike(f"%{destination}%")).all()
    for trip in trips:
        print(f"{trip.id}: {trip.destination} on {trip.date}, Duration: {trip.duration} days, Price: {trip.price}")

def view_bookings():
    bookings = session.query(Booking).all()
    for booking in bookings:
        print(f"Booking ID: {booking.id}, Trip ID: {booking.trip_id}, Customer: {booking.customer_name}")

def edit_trip():
    trip_id = int(input("Enter trip ID to edit: "))
    trip = session.query(Trip).filter(Trip.id == trip_id).first()
    
    if trip:
        destination = input(f"New destination (leave blank to keep '{trip.destination}'): ")
        if destination: trip.destination = destination
        
        date = input(f"New date (leave blank to keep '{trip.date}'): ")
        if date: trip.date = date
        
        duration = input(f"New duration (leave blank to keep '{trip.duration}'): ")
        if duration: trip.duration = int(duration)
        
        price = input(f"New price (leave blank to keep '{trip.price}'): ")
        if price: trip.price = float(price)
        
        session.commit()
        print("Trip updated successfully.")
    else:
        print("Trip not found.")

def delete_trip():
    trip_id = int(input("Enter trip ID to delete: "))
    trip = session.query(Trip).filter(Trip.id == trip_id).first()
    
    if trip:
        session.delete(trip)
        session.commit()
        print("Trip deleted successfully.")
    else:
        print("Trip not found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Create Trip")
        print("2. Book Trip")
        print("3. View Trips")
        print("4. Search Trips")
        print("5. View Bookings")
        print("6. Edit Trip")
        print("7. Delete Trip")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            create_trip()
        elif choice == '2':
            book_trip()
        elif choice == '3':
            view_trips()
        elif choice == '4':
            search_trips()
        elif choice == '5':
            view_bookings()
        elif choice == '6':
            edit_trip()
        elif choice == '7':
            delete_trip()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
