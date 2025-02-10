import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { getUserData } from "../utils/api";

export default function Dashboard() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const data = await getUserData();
      setUser(data);
    }
    fetchData();
  }, []);

  return (
    <div className="min-h-screen flex flex-col justify-between">
      <Navbar />
      <main className="flex flex-col items-center justify-center p-10">
        <h2 className="text-3xl font-bold mb-6">Dashboard</h2>
        {user ? (
          <div className="bg-white p-6 shadow-lg rounded-lg">
            <h3 className="text-xl font-semibold">Welcome, {user.name}!</h3>
            <p>Email: {user.email}</p>
            <p>Role: {user.role}</p>
          </div>
        ) : (
          <p>Loading user data...</p>
        )}
      </main>
      <Footer />
    </div>
  );
}
