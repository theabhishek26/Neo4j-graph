# Neo4j-graph

This project demonstrates how to use Python with Neo4j to create and query a simple graph database of people and their relationships within a company.

## Features

- Connects to a Neo4j database using the official Python driver.
- Creates sample data: people, a company, and their relationships.
- Queries and displays employees working at "Blackcoffer" and their roles.

## Requirements

- Python 3.x
- [neo4j Python driver](https://pypi.org/project/neo4j/)
- Running Neo4j instance (default URI: `neo4j://127.0.0.1:7687`)

## Installation

1. Install the Neo4j Python driver:
    ```sh
    pip install neo4j
    ```

2. Make sure Neo4j is running and accessible at the configured URI.

## Usage

1. Edit the connection details in [`neo4j_project.py`](neo4j_project.py) if needed (username, password, URI).
2. Run the script:
    ```sh
    python neo4j_project.py
    ```

3. The script will:
    - Create sample data in the database.
    - Print the list of employees at "Blackcoffer" and their roles.

## File Structure

- [`neo4j_project.py`](neo4j_project.py): Main script for database operations.

