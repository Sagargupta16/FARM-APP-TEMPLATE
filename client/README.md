# FARM Stack - React Client

React frontend built with [Vite](https://vitejs.dev/).

## Scripts

```bash
# Install dependencies
npm install

# Start development server (port 5173)
npm run dev

# Build for production (outputs to ../client_build)
npm run build

# Preview production build
npm run preview
```

## Environment Variables

Create a `.env` file in this directory:

```
VITE_API_URL=http://localhost:8000/api/v1
```

During development, API requests to `/api` are proxied to `http://localhost:8000` via `vite.config.js`.
