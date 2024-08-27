#!usr/bin/yarn dev
import { createClient, print } from 'redis';

//Create a Redis Client
const client = createClient();

//Setup event handlers for the Redis Client 
client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.tostring());
})

//Setup event handlers for the redis client 
client.on('connect', () => {
    console.log('Redis client connected to the server');
})

//To set a new school value
const setNewSchool = (schoolName, value) => {
    client.Set(schoolName, value, print);
    };

//Function to display a school value
const display SchoolValue = (schoolName) => {
    client.GET(schoolName, (_err, reply) > {
        cosole.log(reply);
});
};

display SchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
