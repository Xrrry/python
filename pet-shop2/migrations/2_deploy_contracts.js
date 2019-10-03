var MyContract = artifacts.require("Adoption");

module.exports = function(deployer) {
    deployer.deploy(MyContract);
}