"use client";

import React, { useState } from 'react';
import axios from 'axios';
import styles from './page.module.css';

export default function Home() {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [budget, setBudget] = useState('');
  const [tripType, setTripType] = useState('');
  const [tripOptions, setTripOptions] = useState([]);
  const [selectedOption, setSelectedOption] = useState(null);
  const [step, setStep] = useState(1);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStep(2);
    try {
      const res = await axios.get('http://localhost:8000/possible-destinations', {
        params: {
          start_date: startDate,
          end_date: endDate,
          budget: parseInt(budget),
          trip_type: tripType,
        },
      });
      setTripOptions(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleOptionSelect = async (option) => {
    setSelectedOption(option);
    setStep(3);
    try {
      const res = await axios.get('http://localhost:8000/generate-itinerary-and-images', {
        params: {
          destination: option.destination,
          start_date: startDate,
          end_date: endDate,
          trip_type,
        },
      });
      setSelectedOption({ ...option, ...res.data });
    } catch (err) {
      console.error(err);
    }
  };

  const renderFlightDetails = (flight) => {
    console.log(flight);  // Print the flight parameter to the console
    const city = Object.keys(flight)[0];
    console.log('city:',city);  // Print the city to the console
    if (!flight || !flight[city].flights) {
      return <div>No flight details available.</div>;
  }
    
    const { flights, price } = flight[city];
    return (
      <div>
        {price && <h3>Total Price: ${price}</h3>}
        <table className={styles.flightTable}>
          <thead>
            <tr>
              <th>Flight Number</th>
              <th>Airline</th>
              <th>Departure Airport</th>
              <th>Departure Time</th>
              <th>Arrival Airport</th>
              <th>Arrival Time</th>
              <th>Duration (minutes)</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(flights).map(([flightNumber, details], index) => (
              <tr key={index}>
                <td>{flightNumber}</td>
                <td>{details.airline || 'N/A'}</td>
                <td>{details.departure_airport_name}</td>
                <td>{details.departure_time}</td>
                <td>{details.arrival_airport_name}</td>
                <td>{details.arrival_time}</td>
                <td>{details.duration}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
};


  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Trip Planner</h1>

      {step === 1 && (
        <form onSubmit={handleSubmit} className={styles.form}>
          <label>
            Start Date:
            <input
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              required
            />
          </label>
          <br />
          <label>
            End Date:
            <input
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              required
            />
          </label>
          <br />
          <label>
            Budget (USD):
            <input
              type="number"
              value={budget}
              onChange={(e) => setBudget(e.target.value)}
              required
            />
          </label>
          <br />
          <label>
            Trip Type:
            <select
              value={tripType}
              onChange={(e) => setTripType(e.target.value)}
              required
            >
              <option value="">Select trip type</option>
              <option value="ski">Ski</option>
              <option value="beach">Beach</option>
              <option value="city">City</option>
            </select>
          </label>
          <br />
          <button type="submit">Get Options</button>
        </form>
      )}

      {step === 2 && (
        <div className={styles.optionsContainer}>
          <h2 className={styles.subheading}>Select a Trip Option</h2>
          {tripOptions.map((option) => {
            console.log('option:',option);  // Print the option to the console
            // console.log('option.going_flight:',option.going_flight['Tokyo']);  // Print the going_flight to the console
            return (
              <div
                key={option.id}
                className={styles.optionCard}
              >
                <p>Destination: {option.destination}</p>
                <h3>Going Flight</h3>
                {renderFlightDetails(option.going_flight)}
                <h3>Returning Flight</h3>
                {renderFlightDetails(option.returning_flight)}
                <p>Hotel: {option.hotel}</p>
                <p>Hotel Price: ${option.hotel_price}</p>
                <p>Total Price: ${option.price}</p>
                <button onClick={() => handleOptionSelect(option)}>Choose this option</button>
              </div>
            );
          })}
        </div>
      )}


      {step === 3 && selectedOption && (
        <div className={styles.summaryContainer}>
          <h2>Trip Summary</h2>
          <div>
            <h3>Destination</h3>
            <p>Flight Price: {selectedOption.going_flight.price}</p>
            <p>{selectedOption.destination}</p>
          </div>
          <div>
            <h3>Flights</h3>
            <div>
              <h4>Going Flight</h4>
              {renderFlightDetails(selectedOption.going_flight)}
              <h4>Returning Flight</h4>
              {renderFlightDetails(selectedOption.returning_flight)}
            </div>
          </div>
          <div>
            <h3>Hotel</h3>
            <p>{selectedOption.hotel}</p>
            <p>Price: ${selectedOption.hotel_price}</p>
          </div>
          <div>
            <h3>Total Cost</h3>
            <p>${selectedOption.total_cost}</p>
          </div>
          <div>
            <h3>Trip Plan</h3>
            <pre>{JSON.stringify(selectedOption.trip_plan, null, 2)}</pre>
          </div>
          <div>
            <h3>Trip Images</h3>
            {selectedOption.trip_images.map((imgUrl, index) => (
              <img key={index} src={imgUrl} alt={`Trip Image ${index + 1}`} className={styles.tripImage} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
