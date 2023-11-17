// SPDX-License-Identifier: MIT
pragma solidity ^0.8.6;

contract AssignHash{

    address public owner;
    string public ipfsHash;

    constructor() {
        ipfsHash = "NadaAhorita";
        owner = msg.sender;
    }

    function changeHash(string memory newHash) public {
        ipfsHash = newHash;
    }

    function getHash() public view returns (string memory) {
        return (ipfsHash);
    }

}