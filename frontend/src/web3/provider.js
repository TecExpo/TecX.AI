import { ethers } from "ethers";

let provider;

if (typeof window !== "undefined" && window.ethereum) {
  provider = new ethers.BrowserProvider(window.ethereum);
} else {
  provider = new ethers.JsonRpcProvider(process.env.NEXT_PUBLIC_RPC_URL || "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID");
}

export default provider;
