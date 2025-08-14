**Neo4j Graph Database with Cypher Queries using Python**

---

## **1. Introduction**

This project demonstrates how to use **Neo4j** (a graph database) with **Python** to perform **Create, Read, Update, Delete (CRUD)** operations and visualize relationships between nodes.
It uses the **official Neo4j Python Driver** to connect to the database and execute **Cypher queries**.

The project models a small company structure where:

* **People (employees)** work at a **Company**.
* Employees can have **friendship relationships** with each other.

---

## **2. Requirements**

### **Software**

* **Neo4j Desktop** or **Neo4j Server** running locally on `bolt://127.0.0.1:7687`
* **Python 3.8+**
* **Neo4j Python Driver**
  Install with:

  ```bash
  pip install neo4j
  ```

### **Neo4j Setup**

1. Start your Neo4j database in Neo4j Desktop.
2. Set the **username** and **password** in the code:

   ```python
   username = "neo4j"
   password = "password123"
   ```
3. Ensure **Bolt protocol** is enabled.

---

## **3. Code Overview**

### **3.1 Database Connection**

```python
uri = "bolt://127.0.0.1:7687"
driver = GraphDatabase.driver(uri, auth=(username, password))
```

* **Bolt protocol** is used for local connection.
* `GraphDatabase.driver` establishes the connection to Neo4j.

---

### **3.2 Utility Functions**

#### **Clear Database**

```python
MATCH (n) DETACH DELETE n
```

* Deletes all nodes and relationships to ensure the database starts fresh.

#### **Create Constraints**

```cypher
CREATE CONSTRAINT person_name_unique IF NOT EXISTS
FOR (p:Person) REQUIRE p.name IS UNIQUE
```

* Prevents duplicate people with the same name.

```cypher
CREATE CONSTRAINT company_name_unique IF NOT EXISTS
FOR (c:Company) REQUIRE c.name IS UNIQUE
```

* Prevents duplicate company nodes.

---

### **3.3 Create Operations**

#### **Create Person and Company**

```cypher
MERGE (p:Person {name: $person_name})
SET p.role = $role
MERGE (c:Company {name: $company_name})
MERGE (p)-[:WORKS_AT]->(c)
```

* **MERGE** ensures the node is created only if it doesn’t already exist.
* **SET** updates the employee’s role.
* Creates a **WORKS\_AT** relationship.

#### **Create Friendship**

```cypher
MATCH (p1:Person {name: $name1})
MATCH (p2:Person {name: $name2})
MERGE (p1)-[:FRIENDS_WITH]->(p2)
```

* Creates a directed **FRIENDS\_WITH** relationship between two people.

---

### **3.4 Read Operations**

#### **Query Employees**

```cypher
MATCH (p:Person)-[:WORKS_AT]->(c:Company {name: $company_name})
RETURN DISTINCT p.name AS employee, p.role AS role
ORDER BY employee
```

* Retrieves **unique** employees and their roles for a specific company.

#### **Count Employees**

```cypher
MATCH (p:Person)-[:WORKS_AT]->(c:Company {name: $company_name})
RETURN count(DISTINCT p) AS total
```

* Counts the number of unique employees in a company.

---

### **3.5 Update Operation**

```cypher
MATCH (p:Person {name: $person_name})
SET p.role = $new_role
```

* Updates the `role` property of a given person.

---

### **3.6 Delete Operation**

```cypher
MATCH (p:Person {name: $person_name})
DETACH DELETE p
```

* Deletes a person and all relationships connected to them.

---

## **4. Program Execution Flow**

1. **Clear database** (`clear_database`)
2. **Create constraints** to avoid duplicates
3. **Insert sample data**: Alice, Bob, Charlie working at **Blackcoffer**
4. **Create friendship relationships**
5. **Query and print employees**
6. **Count total employees**
7. **Update Bob’s role**
8. **Delete Charlie**
9. **Show final data**

---

## **5. Sample Output**

```
=== Employees at Blackcoffer ===
Employee: Alice, Role: Data Scientist
Employee: Bob, Role: Engineer
Employee: Charlie, Role: Manager

=== Total Employees Count ===
Total employees in Blackcoffer: 3

=== Updating Bob's Role to 'Senior Engineer' ===
Employee: Alice, Role: Data Scientist
Employee: Bob, Role: Senior Engineer
Employee: Charlie, Role: Manager

=== Deleting Charlie ===
Employee: Alice, Role: Data Scientist
Employee: Bob, Role: Senior Engineer
```

---

## **6. Visualizing in Neo4j Browser**

After running the script, open **Neo4j Browser** and run:

```cypher
MATCH (n) RETURN n;
```

You’ll see:

* **Person nodes** with `name` and `role`
* **Company node** named "Blackcoffer"
* **WORKS\_AT** and **FRIENDS\_WITH** relationships

---

## **7. Key Learnings**

* Using `MERGE` instead of `CREATE` avoids duplicates.
* Constraints improve data integrity.
* Python driver `execute_write` and `execute_read` manage transactions efficiently.
* Cypher allows expressive querying of relationships.


