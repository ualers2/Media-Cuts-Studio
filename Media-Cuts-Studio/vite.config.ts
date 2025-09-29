// vite.config.js
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { componentTagger } from "lovable-tagger";
import tsconfigPaths from "vite-tsconfig-paths";       // ← importa o plugin

export default defineConfig(({ mode }) => ({

  plugins: [
    tsconfigPaths(),
    react(),
    mode === "development" && componentTagger(),
  ].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },

  server: {
    host: "0.0.0.0",    // ou "::", para aceitar conexões externas
    port: 4343,
    allowedHosts: ["localhost", '904d7cc79a14.ngrok-free.app', "mediacutsstudio.com", "www.mediacutsstudio.com"],
    hmr: {
      protocol: 'wss',
      host: 'mediacutsstudio.com',  
    },
    // watch: {
    //   ignored: ['**/node_modules/**'],
    //   usePolling: true,
    //   interval: 100,
    // },
  },

}));
