from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement, dict_factory

class CassandraDb:

    def __init__(self, ip_addr, port, keyspace):

        cluster = Cluster([ip_addr])

        self.session = cluster.connect(keyspace)

        self.session.row_factory = dict_factory
    # create a table inside a specific keyspace
    def create_table( self, keyspace, table, fields ):

        self.session.execute('USE {};'.format( keyspace ) )

        create_table_query = 'CREATE TABLE ({});'.format( ','.join(fields) )

        self.session.execute( create_table_query )

    # insert a batch of data inside a table
    def insert_batch_data(self, data, table):

        for i, row in enumerate( data ):

            fields = ','.join( row.keys() )

            parameters = ','.join([ '%s' for _ in range( len(row.keys()) ) ])

            query = SimpleStatement(
                "INSERT INTO {}({}) VAlUES({})".format(table, fields, parameters),
                consistency_level=ConsistencyLevel.ANY
            )

            if ( i+1 ) % 10000 == 0 or i == len( data ) - 1 :
                print( 'inserting row # {}'.format(i+1) )

            self.session.execute( query, row.values())

    def read_table( self, table):

        select_query = 'SELECT * FROM {}'.format(table);

        future = self.session.execute_async( select_query )

        return list( future.result() )
