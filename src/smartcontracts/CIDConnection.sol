// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;

contract IPFSStorage {
    mapping(address => string) private ipfsCIDs;

    event IPFSCIDStored(address indexed user, string cid);

    function storeIPFSCID(string memory cid) public {
        ipfsCIDs[msg.sender] = cid;
        emit IPFSCIDStored(msg.sender, cid);
    }

    function getIPFSCID(address user) public view returns (string memory) {
        return ipfsCIDs[user];
    }
}