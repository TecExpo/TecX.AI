
import React from "react";

const Footer = () => {
  return (
    <footer className="bg-gray-900 text-white py-6 mt-10">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Logo & Description */}
          <div>
            <h2 className="text-xl font-bold">TecX AI Platform</h2>
            <p className="mt-2 text-sm text-gray-400">
              The next-gen AI-powered Web3 platform for secure and decentralized solutions.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold">Quick Links</h3>
            <ul className="mt-2 space-y-2">
              <li><a href="/about" className="text-gray-400 hover:text-white">About Us</a></li>
              <li><a href="/services" className="text-gray-400 hover:text-white">Services</a></li>
              <li><a href="/contact" className="text-gray-400 hover:text-white">Contact</a></li>
              <li><a href="/faq" className="text-gray-400 hover:text-white">FAQ</a></li>
            </ul>
          </div>

          {/* Social Media & Newsletter */}
          <div>
            <h3 className="text-lg font-semibold">Connect with Us</h3>
            <div className="flex space-x-4 mt-2">
              <a href="https://twitter.com" className="hover:text-blue-400">Twitter</a>
              <a href="https://linkedin.com" className="hover:text-blue-400">LinkedIn</a>
              <a href="https://github.com" className="hover:text-blue-400">GitHub</a>
            </div>

            <h3 className="text-lg font-semibold mt-4">Subscribe to our Newsletter</h3>
            <form className="mt-2">
              <input 
                type="email" 
                placeholder="Enter your email" 
                className="w-full p-2 rounded-md text-gray-900"
              />
              <button className="mt-2 w-full bg-blue-500 text-white py-2 rounded-md">
                Subscribe
              </button>
            </form>
          </div>
        </div>

        {/* Copyright */}
        <div className="text-center text-sm text-gray-500 mt-6">
          © {new Date().getFullYear()} AI Web3 Platform. All rights reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
