import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { ItemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { ItemId: 3, ItemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { ItemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.itemId === id);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return Stock ? parseInt(stock, 10) : null;
}

listProducts.forEach((product) => {
  reserveStockById(product.itemId, product.initialAvailableQuantity);
});

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  res.json({
    ...product,
    currentQuantity: currentQuantity ?? product.initialAvailableQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (!currentQuantity || currentQuantity <= 0) {
    return res.status(400).json({
      status: 'Not enough stock available',
      itemId,
    });
  }

  await reserveStockById(itemId, currentQuantity - 1);

  res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
