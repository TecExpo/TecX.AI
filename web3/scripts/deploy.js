const { ethers } = require("hardhat");

async function main() {
    const AIWeb3Contract = await ethers.getContractFactory("AIWeb3Contract");
    const contract = await AIWeb3Contract.deploy();
    await contract.deployed();

    console.log("Contract deployed at:", contract.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
