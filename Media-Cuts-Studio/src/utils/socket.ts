// src/utils/socket.ts
import { io, Socket } from 'socket.io-client';

let socket: Socket | null = null;

/**
 * Inicializa (ou reconecta) o socket, passando a API_KEY como auth.
 * Deve ser chamado logo após o login (no LoginForm).
 */
export const initSocket = (apiKey: string) => {
  if (socket && socket.connected) {
    return socket;
  }
  console.log(`VITE_WEBHOOK_URL? ${import.meta.env.VITE_WEBHOOK_URL}`)
  socket = io(`${import.meta.env.VITE_WEBHOOK_URL}`, {
    // auth: { api_key: apiKey },
    path: "/socket.io",
    autoConnect: true,
    // transports: ['websocket'],
    reconnection: true,
    timeout: 20000,
  });

  socket.on('connect_error', (err) => {
    console.error('Falha ao conectar no Socket.IO:', err);
  });

  return socket;
};

/**
 * Retorna a instância já inicializada de socket (ou null se não houver).
 */
export const getSocket = (): Socket | null => {
  return socket;
};
