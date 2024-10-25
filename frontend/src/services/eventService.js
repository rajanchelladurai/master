import React, { useEffect, useState } from 'react';
import axios from 'axios';

const EventList = () => {
    const [events, setEvents] = useState([]);

    useEffect(() => {
        // Fetch events from the static Django API
        axios.get('http://127.0.0.1:8000/api/events/')
            .then(response => {
                setEvents(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the events!', error);
            });
    }, []);

    return (
        <div>
            <h1>Upcoming Events</h1>
            <ul>
                {events.map(event => (
                    <li key={event.id}>
                        <h2>{event.title}</h2>
                        <p>{event.description}</p>
                        <p>Starts: {new Date(event.start_date).toLocaleString()}</p>
                        <p>Ends: {new Date(event.end_date).toLocaleString()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default EventList;
