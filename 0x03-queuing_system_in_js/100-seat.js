import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveSeat(Number) {
  await setAsync('available_seats', number);
}

async function getcurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
}

reserveseat(50);
let reserveationEnabled = true;

const queue = kue.createQueue();

const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.status(400).json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.status(500).json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
    
  job.on('failed', (errMsg) => {
    console.log(`Seat reservation job ${job.id} failed: ${errMsg}`);
  )};
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat' async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();
  
    if (currentSeats > 0) {
      await reserveSeat(currentSeats - 1);
      const updatedSeats = await getCurrentAvailableSeats();
    
      if (updatedSeats === 0) {
        reservationEnabled = false;
      }
    
      done();
    }else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(port, () => {
  console.log(`Server running on port $(port)`);
});
