import React, { useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    alert(`Logging in with Email: ${email}`);
    // Call authentication API here
  };

  return (
    <div className="min-h-screen flex flex-col justify-between">
      <Navbar />
      <main className="flex flex-col items-center justify-center p-10">
        <h2 className="text-3xl font-bold mb-6">Login</h2>
        <form onSubmit={handleLogin} className="w-80 bg-white p-6 shadow-lg rounded-lg">
          <div className="mb-4">
            <label className="block text-gray-700">Email</label>
            <input
              type="email"
              className="w-full p-2 border border-gray-300 rounded"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700">Password</label>
            <input
              type="password"
              className="w-full p-2 border border-gray-300 rounded"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded">
            Login
          </button>
        </form>
      </main>
      <Footer />
    </div>
  );
}
