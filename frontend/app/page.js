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
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStep(2);
    setLoading(true); // Set loading to true when request starts
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
    } finally {
      setLoading(false); // Set loading to false when request completes
    }
  };

  const handleOptionSelect = async (option) => {
    setSelectedOption(option);
    console.log('setting chosen option to selectedOption:', option);
    setStep(3);
    try {
      const res = await axios.get('http://localhost:8000/generate-itinerary-and-images', {
        params: {
          destination: option.destination,
          start_date: startDate,
          end_date: endDate,
          trip_type: tripType,
        },
      });
      console.log('res:', res.data[0]);
      setSelectedOption({ ...option, ...res.data[0] });
      console.log('Selected Option:', selectedOption);
    } catch (err) {
      console.log('inside catch!')
      console.error(err);
    }
  };

  const renderFlightDetails = (flight, type) => {
    console.log(flight);
    const city = Object.keys(flight)[0];
    console.log('city:', city);
    const flight_direction = type === 'going_flight' ? 'Going' : 'Returning';
    if (!flight || !flight[city].flights) {
      return <div>No flight details available.</div>;
    }

    const { flights, price } = flight[city];
    return (
      <div>
        {price && <h4>Flights Price: ${price}</h4>}
        <h4>{flight_direction} Flights</h4>
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

  const renderTripPlan = (tripPlan) => {
    if (!tripPlan) return null;

    const days = tripPlan.split('\n\n').filter(day => day.trim() !== '');

    return (
      <div>
        <h3>Trip Plan</h3>
        {days.map((day, index) => {
          const lines = day.split('\n').filter(line => line.trim() !== '');
          const [date, ...activities] = lines;
          return (
            <div key={index}>
              <h4>{date}</h4>
              <ul>
                {activities.map((activity, i) => (
                  <li key={i}>{activity}</li>
                ))}
              </ul>
            </div>
          );
        })}
      </div>
    );
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Trip Planner</h1>

      {step === 1 && (
        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.section}>
            <div className={styles.formInput}>
              <label>
                Start Date:
                <input
                  type="date"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                  required
                />
              </label>
            </div>
          </div>

          <div className={styles.section}>
            <div className={styles.formInput}>
              <label>
                End Date:
                <input
                  type="date"
                  value={endDate}
                  onChange={(e) => setEndDate(e.target.value)}
                  required
                />
              </label>
            </div>
          </div>

          <div className={styles.section}>
            <div className={styles.formInput}>
              <label>
                Budget (USD):
                <input
                  type="number"
                  value={budget}
                  onChange={(e) => setBudget(e.target.value)}
                  required
                />
              </label>
            </div>
          </div>

          <div className={styles.section}>
            <div className={styles.formInput}>
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
            </div>
          </div>

          <button type="submit">Get Options</button>
        </form>
      )}

      {step === 2 && (
        <div className={styles.optionsContainer}>
          <h2 className={styles.subheading}>Select a Trip Option</h2>
          {loading ? (
            <div className={styles.loadingMessage}>
              <p>Loading options...</p>
            </div>
          ) : (
            <>
              {tripOptions.length > 0 ? (
                tripOptions.map((option) => (
                  <div key={option.id} className={styles.optionCard}>
                    <p>Destination: {option.destination}</p>
                    {renderFlightDetails(option.going_flight, 'going_flight')}
                    {renderFlightDetails(option.returning_flight, 'returning_flight')}
                    <p>Hotel: {option.hotel}</p>
                    <p>Hotel Price: ${option.hotel_price}</p>
                    <p>Total Price: ${option.price}</p>
                    <button onClick={() => handleOptionSelect(option)}>Choose this option</button>
                  </div>
                ))
              ) : (
                <div className={styles.noDataMessage}>
                  <p>No trip options found. Please try adjusting your search criteria.</p>
                </div>
              )}
            </>
          )}
        </div>
      )}

      {step === 3 && selectedOption && (
        <div className={styles.summaryContainer}>
          <h2>Trip Summary</h2>
          <div>
            <h3>Destination</h3>
            <p>{selectedOption.destination}</p>
          </div>
          <div>
            <h3>Flights</h3>
            <div>
              {renderFlightDetails(selectedOption.going_flight, 'going_flight')}
              {renderFlightDetails(selectedOption.returning_flight, 'returning_flight')}
            </div>
          </div>
          <div>
            <h3>Hotel</h3>
            <p>{selectedOption.hotel}</p>
            <p>Price: ${selectedOption.hotel_price}</p>
          </div>
          <div>
            <h3>Total Cost</h3>
            <p>${selectedOption.price}</p>
          </div>
          <div>
            {renderTripPlan(selectedOption.trip_plan)}
          </div>
          <div>
            <h3>Trip Images</h3>
            {selectedOption.trip_images && selectedOption.trip_images.map((imgUrl, index) => (
              <img key={index} src={imgUrl} alt={`Trip Image ${index + 1}`} className={styles.tripImage} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
