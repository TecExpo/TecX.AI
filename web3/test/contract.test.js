const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("AIWeb3Contract", function () {
    let contract, owner, addr1;

    beforeEach(async function () {
        [owner, addr1] = await ethers.getSigners();
        const AIWeb3Contract = await ethers.getContractFactory("AIWeb3Contract");
        contract = await AIWeb3Contract.deploy();
        await contract.deployed();
    });

    it("Should allow deposits", async function () {
        await contract.connect(addr1).deposit({ value: ethers.parseEther("1") });
        expect(await contract.balances(addr1.address)).to.equal(ethers.parseEther("1"));
    });

    it("Should allow withdrawals", async function () {
        await contract.connect(addr1).deposit({ value: ethers.parseEther("1") });
        await contract.connect(addr1).withdraw(ethers.parseEther("1"));
        expect(await contract.balances(addr1.address)).to.equal(0);
    });
});
