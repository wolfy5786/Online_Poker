let socket;

export const connectSocket = (roomCode, onMessage) => {
  socket = new WebSocket(`ws://localhost:8000/ws/game/${roomCode}/`);
  socket.onmessage = (e) => onMessage(JSON.parse(e.data));
  return socket;
};

export const sendAction = (action) => {
  if (socket && socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({ action }));
  }
};
