pragma solidity ^0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract LegalDocumentsCollectible is ERC721 {
    uint256 public tokenCounter;
    uint256 realEstateId;

    constructor () public ERC721 ("LegalDocCollectible", "LDC"){
        tokenCounter = 0;

    }

    function createCollectible(string memory tokenURI, uint256 realEstateId) public returns (uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newItemId;
    }


}