import { useState, useEffect } from "react";
import { connectWallet } from "../web3/connectWallet";

const useAuth = () => {
  const [account, setAccount] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const loadAccount = async () => {
      const wallet = await connectWallet();
      if (wallet) {
        setAccount(wallet.address);
        setIsAuthenticated(true);
      }
    };

    if (window.ethereum) {
      loadAccount();

      window.ethereum.on("accountsChanged", (accounts) => {
        if (accounts.length > 0) {
          setAccount(accounts[0]);
          setIsAuthenticated(true);
        } else {
          setAccount(null);
          setIsAuthenticated(false);
        }
      });
    }
  }, []);

  return { account, isAuthenticated };
};

export default useAuth;
