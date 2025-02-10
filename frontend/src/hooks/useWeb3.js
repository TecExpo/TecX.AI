import { useState, useEffect } from "react";
import provider from "../web3/provider";
import { ethers } from "ethers";

const useWeb3 = () => {
  const [signer, setSigner] = useState(null);
  const [balance, setBalance] = useState("0");

  useEffect(() => {
    const fetchSigner = async () => {
      if (provider) {
        const signer = await provider.getSigner();
        setSigner(signer);

        const address = await signer.getAddress();
        const balanceWei = await provider.getBalance(address);
        setBalance(ethers.formatEther(balanceWei));
      }
    };

    fetchSigner();
  }, []);

  return { signer, balance };
};

export default useWeb3;
