from neo4j import GraphDatabase

uri = "neo4j://127.0.0.1:7687"
username="neo4j"
password="password123"
driver = GraphDatabase.driver(uri, auth=(username, password))


# Create data
def create_sample_data(tx):
    tx.run("""
        CREATE (p1:Person {name: 'Alice', role: 'Data Scientist'}),
                (p2:Person {name: 'Bob', role: 'Engineer'}),
                (p3:Person {name: 'Charlie', role: 'Manager'}),
                (c1:Company {name: 'Blackcoffer'}),
                (p1)-[:WORKS_AT]->(c1),
                (p2)-[:WORKS_AT]->(c1),
                (p3)-[:WORKS_AT]->(c1),
                (p1)-[:FRIENDS_WITH]->(p2),
                (p2)-[:FRIENDS_WITH]->(p3)
    """)
    
# Query data

# ...existing code...

def query_data(tx):
    result=tx.run("""
            MATCH (p:Person)-[:WORKS_AT]->(c:Company {name: 'Blackcoffer'})
            RETURN p.name AS employee ,p.role AS role       
    """)
    for record in result:
        print(f"Employee: {record['employee']}, Role: {record['role']}")
    
#  Main execution

with driver.session() as session:
    session.execute_write(create_sample_data)
    print("Employee at Blackcoffer: ")
    session.execute_read(query_data)

driver.close()