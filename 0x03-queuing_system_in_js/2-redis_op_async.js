//Import necessary modules
import redis from 'redis'
import { promisify } from 'util';

//Create a redis client
const client = redis.createClient();

//Set up event handlers for the Redis client
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.error('Redis client not connected to the server: ${error}');
});

//Promisify the get function of the Redis client
const getAsync = promisify(client.get).bind(client);

//Function to get a new scholl value
function setNewSchool (schoolName, value) {
    client.set(schoolName, value, redis.print);
}

//Async function to display the school value
async function displaySchoolValue (schoolName){
    try{
        const reply = await getAsync(schoolName);
        console.log('${reply}');
    } catch (error) {
        console.error('Error getting value for ${schoolNmae}: ${error}');
    }
}

//Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');