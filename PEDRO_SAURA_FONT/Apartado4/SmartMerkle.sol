// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SmartMerkle
 * @dev Contrato inteligente privado que permite registrar hashes
 *      que forman el inicio de una cadena basada en árboles de Merkle.
 *      Este contrato sirve como base para una estructura verificable
 *      donde cada nodo depende criptográficamente de sus hijos.
 *
 *      El objetivo es ilustrar cómo se construye un Merkle Root inicial
 *      y cómo se podrían añadir ramas posteriormente.
 */
contract SmartMerkle {

    // ---- MODIFICADOR DE PRIVACIDAD ----
    // Solo el creador del contrato puede modificar datos.
    address private owner;

    // Hash raíz del árbol de Merkle (Merkle Root)
    bytes32 public merkleRoot;

    // Evento para registrar la creación o actualización del árbol
    event MerkleRootUpdated(bytes32 newRoot);

    constructor(bytes32 _initialRoot) {
        owner = msg.sender;
        merkleRoot = _initialRoot;
        emit MerkleRootUpdated(_initialRoot);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Solo el propietario puede realizar esta accion.");
        _;
    }

    /**
     * @notice Actualiza el Merkle Root del arbol.
     * @dev Esta operación solo puede realizarla el creador del contrato.
     *
     * @param _newRoot El nuevo hash raíz del árbol.
     */
    function updateMerkleRoot(bytes32 _newRoot) external onlyOwner {
        merkleRoot = _newRoot;
        emit MerkleRootUpdated(_newRoot);
    }

    /**
     * @notice Calcula el hash de dos nodos hijos (left y right)
     * @dev Esto representa un paso típico de un Merkle Tree.
     *
     * @param left Hash del hijo izquierdo.
     * @param right Hash del hijo derecho.
     * @return El hash combinado.
     */
    function hashNodes(bytes32 left, bytes32 right) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(left, right));
    }
}
