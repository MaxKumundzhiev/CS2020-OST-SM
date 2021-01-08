from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement, dict_factory
import csv

class CassandraDb:

    def __init__( self, ip_addr, port):

        cluster = Cluster(ip_addr, port=port)

        self.session = cluster.connect()

        self.session.row_factory = dict_factory
        self.session.default_timeout=60

    # create a table inside a specific keyspace

    def create_keyspace(self, keyspace ):

        '''create a keyspace'''
        query = "CREATE KEYSPACE "+keyspace+" WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3};"

        self.session.execute( query )

    def create_table( self, keyspace, table, schema, order_by='' ):
        '''
            This function will create a table within a given keyspace
            fields: parameter represent the table schema
        '''

        self.session.execute('USE {};'.format( keyspace ) )

        fields = ','.join([k + " " + v for k,v in schema.items()])

        create_table_query = 'CREATE TABLE IF NOT EXISTS {} ({}) {};'.format( table, fields, order_by )

        self.session.execute( create_table_query )

        print('Table {} created successfully'.format(table))

    # insert a batch of data inside a table
    def insert_batch_data(self, data, keyspace, table, start_index=0):

        '''
            insert a batch of records
        '''

        self.session.execute('USE {};'.format( keyspace ) )

        for i, row in enumerate( data[start_index:] ):

            fields = ','.join( row.keys() )

            parameters = ','.join([ '%s' for _ in range( len(row.keys()) ) ])

            query = SimpleStatement(
                "INSERT INTO {}({}) VAlUES({})".format(table, fields, parameters),
                consistency_level=ConsistencyLevel.ANY
            )

            if ( i+1 ) % 10000 == 0 or i == len( data ) - 1 :
                print( 'inserting row # {}'.format(i+1) )

            self.session.execute( query, row.values())

            # save index to a file
            with open('insert_index.txt', 'w') as f:
                f.write(str(start_index + i + 1))

    def read_table( self, keyspace, table, fields=[]):

        ''' read data from an input table'''
        self.session.execute('USE {};'.format( keyspace ) )

        if len( fields ) == 0:

            select_query = 'SELECT * FROM {};'.format( table )

        else:
            select_query = 'SELECT {} FROM {};'.format( ','.join( fields ), table )

        future = self.session.execute_async( select_query )

        return list( future.result() )

    def alter_table( self, keyspace, tablename, keyword, col, coltype ):

        ''' add column to an exising table'''
        self.session.execute('USE {};'.format( keyspace ) )

        if keyword == 'ADD':
            alter_query = 'ALTER TABLE {} {} ADD {};'.format(tablename, col, coltype)
        elif keyword == 'ALTER':
            alter_query = 'ALTER TABLE {} {} ALTER TYPE {};'.format(tablename, col, coltype)
        self.session.execute( alter_query )

    def update_records( self, keyspace, table_name, ids, col, new_vals):

        ''' update a single value for a batch of records '''
        self.session.execute('USE {};'.format( keyspace ) )

        ids = [int(id) for id in ids]

        for id, new_val in zip( ids, new_vals ):

            update_query = 'UPDATE {} SET {}={} WHERE id={}'.format( table_name, col, "'"+new_val+"'", id)

            self.session.execute(update_query)
    def export_table_to_csv(self, keyspace, table_name, fields=[]):

        data = self.read_table(keyspace, table_name)

        with open('{}.csv'.format(table_name), 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            for row in data:
                writer.writerow(row)
    def build_schema(self, data):
        '''
            this function will build schema from an instance, assuming the attributes are either of
            class int, float, or list
        '''
        schema = dict()

        for instance in data:

            for k, v in instance.items():

                if k in schema:
                    continue

                if type(v) is int:
                    schema[k] = 'bigint'
                elif type(v) is float:
                    schema[k] = 'double'
                elif type(v) is str:
                    schema[k] = 'text'
                elif type(v) is list:
                    if type(v[0]) is int:
                        schema[k] = 'list<int>'
                    elif type(v[0]) is float:
                        schema[k] = 'list<double>'
                    elif type(v[0]) is str:
                        schema[k] = 'list<text>'
            schema['PRIMARY KEY'] = '(id)'
            schema['label'] = 'text'
        return schema
