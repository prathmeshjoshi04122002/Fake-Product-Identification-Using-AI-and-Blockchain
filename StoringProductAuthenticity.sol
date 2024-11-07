// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ProductAuthenticity {
    
    struct Product {
        uint id;
        string name;
        string manufacturer;
        bool isGenuine;
    }
    
    // Mapping to store product information
    mapping(uint => Product) public products;
    address public admin;

    // Event for new product registration
    event ProductRegistered(uint productId, string name, string manufacturer, bool isGenuine);

    // Constructor to set the admin
    constructor() {
        admin = msg.sender;
    }

    // Modifier to allow only admin
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    // Register a new product with authenticity status
    function registerProduct(uint _id, string memory _name, string memory _manufacturer, bool _isGenuine) public onlyAdmin {
        require(products[_id].id == 0, "Product already exists");
        
        products[_id] = Product({
            id: _id,
            name: _name,
            manufacturer: _manufacturer,
            isGenuine: _isGenuine
        });

        emit ProductRegistered(_id, _name, _manufacturer, _isGenuine);
    }

    // Verify if a product is genuine or fake
    function verifyProduct(uint _id) public view returns (string memory name, string memory manufacturer, bool isGenuine) {
        require(products[_id].id != 0, "Product not found");
        
        Product memory p = products[_id];
        return (p.name, p.manufacturer, p.isGenuine);
    }
}
