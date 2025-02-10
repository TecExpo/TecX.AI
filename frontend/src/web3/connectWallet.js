import { ethers } from "ethers";

export const connectWallet = async () => {
  if (typeof window !== "undefined" && window.ethereum) {
    try {
      await window.ethereum.request({ method: "eth_requestAccounts" });
      const provider = new ethers.BrowserProvider(window.ethereum);
      const signer = await provider.getSigner();
      const address = await signer.getAddress();
      return { provider, signer, address };
    } catch (error) {
      console.error("Wallet connection failed:", error);
      return null;
    }
  } else {
    alert("MetaMask is not installed. Please install it to use Web3 features.");
    return null;
  }
};
