import React from "react";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Button from "../components/Button";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col justify-between">
      <Navbar />
      <main className="flex flex-col items-center justify-center text-center p-10">
        <h1 className="text-4xl font-bold mb-4">Welcome to AI-Web3-Website</h1>
        <p className="text-lg text-gray-700 mb-6">
          A cutting-edge platform combining AI and Web3 technologies.
        </p>
        <Button text="Get Started" onClick={() => alert("Getting Started!")} />
      </main>
      <Footer />
    </div>
  );
}
