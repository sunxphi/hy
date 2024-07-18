import { defineConfig } from 'vite';
import hydrogen from '@shopify/hydrogen/plugin';
import tsconfigPaths from 'vite-tsconfig-paths';

export default defineConfig({
  plugins: [
    hydrogen(),
    tsconfigPaths(),
  ],
  ssr: {
    noExternal: ['dotenv'],
  },
  resolve: {
    alias: {
      '@': '/src',
    },
  },
});
