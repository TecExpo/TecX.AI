import React from "react";
import Link from "next/link";

const Navbar = () => {
  return (
    <nav className="bg-gray-900 text-white p-4 flex justify-between items-center">
      <div className="text-xl font-bold">AI-Web3 Website</div>
      <ul className="flex space-x-4">
        <li>
          <Link href="/">
            <span className="hover:text-gray-400 cursor-pointer">Home</span>
          </Link>
        </li>
        <li>
          <Link href="/dashboard">
            <span className="hover:text-gray-400 cursor-pointer">Dashboard</span>
          </Link>
        </li>
        <li>
          <Link href="/login">
            <span className="hover:text-gray-400 cursor-pointer">Login</span>
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
