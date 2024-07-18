import { createServer } from '@shopify/hydrogen';
import dotenv from 'dotenv';

dotenv.config();  // Load environment variables from .env file

const shopifyConfig = {
  storeDomain: process.env.SHOPIFY_STORE_URL,
  storefrontToken: process.env.SHOPIFY_STOREFRONT_ACCESS_TOKEN,
  storefrontApiVersion: '2022-07',
};

createServer({
  shopify: shopifyConfig,
  // Other server configuration...
}).then(({ server }) => server.listen(3000));
