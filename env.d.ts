/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly SHOPIFY_STORE_URL: string;
  readonly SHOPIFY_STOREFRONT_ACCESS_TOKEN: string;
  readonly SESSION_SECRET: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
