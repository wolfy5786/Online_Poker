import { useEffect, useState } from "react";
import { connectSocket, sendAction } from "./ws";

export default function Game({ roomCode }) {
  const [players, setPlayers] = useState([]);
  const [hand, setHand] = useState([]);
  const [community, setCommunity] = useState([]);
  const [turn, setTurn] = useState(0);
  const [gameOver, setGameOver] = useState(null);

  useEffect(() => {
    const socket = connectSocket(roomCode, (msg) => {
      if (msg.action === "update") {
        setPlayers(msg.players);
        setHand(msg.your_hand || []);
        setCommunity(msg.community_cards || []);
        setTurn(msg.turn);
      } else if (msg.action === "game_over") {
        setGameOver(msg.winner);
      }
    });

    return () => socket.close();
  }, [roomCode]);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">Poker Room: {roomCode}</h1>

      {gameOver && <div className="text-red-500">🏆 Winner: {gameOver}</div>}

      <div className="my-4">
        <button onClick={() => sendAction("start")} className="btn">
          Start Game
        </button>
        <button onClick={() => sendAction("next")} className="btn ml-2">
          Next Turn
        </button>
        <button onClick={() => sendAction("fold")} className="btn ml-2">
          Fold
        </button>
      </div>

      <div className="my-4">
        <h2 className="text-xl">Your Hand:</h2>
        <div className="flex gap-2">
          {hand.map((card, i) => (
            <div key={i} className="p-2 border">{card}</div>
          ))}
        </div>
      </div>

      <div className="my-4">
        <h2 className="text-xl">Community Cards:</h2>
        <div className="flex gap-2">
          {community.map((card, i) => (
            <div key={i} className="p-2 border">{card}</div>
          ))}
        </div>
      </div>

      <div>👥 Players: {players.length}</div>
      <div>🎯 Current Turn: Player #{turn + 1}</div>
    </div>
  );
}
