#!/usr/bin/env python

from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4j1"))

def _create_and_return_user(tx, user):
	result = tx.run("CREATE (p:Person) "
		"SET p = $user"
		"RETURN a + ', from node ' + id(a)", user=user)
	print(result)
	return result.single()[0]

new_user='''{name: 'Alex', email:'alex.tfif.sf@gmail.com'}'''

cqlCreate=''' CREATE(Alex:Person {name: 'Alex', email:'alex.tfif.sf@gmail.com'} ) '''


### LOAD from CSV ###

#1. Create senders

cqlLoadSenders = ''' 
	LOAD CSV WITH HEADERS FROM "file:////tfif.csv" AS row
	CREATE (n:Person)
	SET n = row,
	n.email = row.sender_email_address,
  	n.name = row.sender_first_name,
  	n.company = row.sender_work
	''' 

#2. Create Admirers
cqlLoadAdmireres1 = '''
	LOAD CSV WITH HEADERS FROM "file:////tfif.csv" AS row
	CREATE (n:Person)
	SET 
  	n.email = row.admiree_1_email_address,
  	n.name = row.admiree_1_first_name
	'''

cqlLoadAdmireres2 = '''
	LOAD CSV WITH HEADERS FROM "file:////tfif.csv" AS row
	CREATE (n:Person)
	SET 
  	n.email = row.admiree_2_email_address,
  	n.name = row.admiree_2_first_name
	'''

cqlLoadAdmireres3 = '''
	LOAD CSV WITH HEADERS FROM "file:////tfif.csv" AS row
	CREATE (n:Person)
	SET 
  	n.email = row.admiree_3_email_address,
  	n.name = row.admiree_3_first_name
	'''

#3. Delete empty records:
deleteEmptyNodes = ''' match( n:Person) WHERE NOT (EXISTS (n.name)) DELETE n '''


#4. Create Relationships:
cqlCreateRel1='''
MATCH (p1:Person),(p2:Person)
WHERE p1.admiree_1_first_name = p2.name
and p1.admiree_1_email_address = p2.email
CREATE (p1)-[:ADMIRES]->(p2)
'''
cqlCreateRel2='''
MATCH (p1:Person),(p2:Person)
WHERE p1.admiree_2_first_name = p2.name
and p1.admiree_2_email_address = p2.email
CREATE (p1)-[:ADMIRES]->(p2)
'''
cqlCreateRel3='''
MATCH (p1:Person),(p2:Person)
WHERE p1.admiree_3_first_name = p2.name
and p1.admiree_3_email_address = p2.email
CREATE (p1)-[:ADMIRES]->(p2)
'''


# Execute the CQLs
with driver.session() as graphDB_Session:
	# _create_and_return_greeting(graphDB_Session,new_user)
    
    # Create nodes
    graphDB_Session.run(cqlLoadSenders)
    print('senders created..')
    graphDB_Session.run(cqlLoadAdmireres1)
    print('Admirers1 created..')
    graphDB_Session.run(cqlLoadAdmireres2)
    print('Admirers2 created..')
    graphDB_Session.run(cqlLoadAdmireres3)
    print('Admirers3 created..')
    graphDB_Session.run(deleteEmptyNodes)
    print('Empty Nodes deleted..')
    graphDB_Session.run(cqlCreateRel1)
    print('Rel1 created..')
    graphDB_Session.run(cqlCreateRel2)
    print('Rel2 created..')
    graphDB_Session.run(cqlCreateRel3)
    print('Rel created..')









