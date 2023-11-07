// SPDX-License-Identifier: MIT
pragma solidity >=0.8.2 <0.9.0;

contract InputRecipe {
    
    // MEMBER VARIABLES
    uint256 public changeCount;
    address public owner;
    string public title;
    string public ingredients;
    string public steps;

    constructor(string memory newTitle, string memory newIngredients, string memory newSteps) {
        owner = msg.sender;
        title = newTitle;
        ingredients = newIngredients;
        steps = newSteps;
    }

    modifier ownerChangeCheck() {
        require(msg.sender == owner, "Only the person who deployed the contract can update the message.");
        _;
    }

}