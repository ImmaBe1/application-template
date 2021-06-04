from cloudant import Cloudant
from cloudant.database import CloudantDatabase
from cloudant.design_document import DesignDocument
from cloudant.query import Query
#from cloudant.view import View

class AbstractModel:
    """
    Abstract Model for cloudant database inheritance. Base class operations used by subclasses.

    :param user: Username of cloudant database.
    :type user: str
    :param password: Password of cloudant database.
    :type password: str
    :param url: Url of cloudant database.
    :type url: str
    :param db_name: Specific table name for cloudant.
    :type db_name: str
    """

    def __init__(self, db_set):
        self.client = Cloudant(db_set['user'], db_set['password'], url=db_set['url'], connect=True)
        self.db = self.client.create_database(db_set['db_name'], throw_on_exists=False)
        self.setup_views()
    
    def getDB(self) -> CloudantDatabase:
        """
        Get cloudant database instance.

        :returns: Cloudant database instance with specific table.
        :rtype: CouchDatabase
        """    
        return self.db
    
    def get_client(self) -> Cloudant:
        """
        Get the connecting client to database.

        :returns: Cloudant client connection to specific table.
        :rtype: Cloudant
        """
        return self.client
    
    def get_supported_fields(self):
        pass

    def __del__(self) -> None:
        """
        Disconnects client connection to database.
        """ 
        if self.client:
            self.client.disconnect()
    
    def create_indexes(self, fields:dict):
        for key in fields:
            index = self.getDB().create_query_index(
                design_document_id='query',
                index_name = key+'-index',
                fields=[key],
                type='json'
            )
            index.create()

    def get_doc_id(self, document_id:str) -> dict:
        """
        Get all document based on document ID

        :param document_id: Document ID corresponding with one in Cloudant database
        :type document_id: str

        :returns: Data on search fields
        :rtype: dict
        """
        data = {}
        try:
            selector = {"_id" : document_id}
            query = Query(self.getDB(), selector=selector)
            data = query.result[0]
        except Exception as e:
            pass
        finally:
            return data
   
    def setup_views(self) -> None:
        """
        Setups views in table.
        """
        try:
            for key in self._views:
                ddoc = DesignDocument(self.getDB(), document_id=self._views[key]['design'], partitioned=False)
                if not ddoc.exists():
                    if 'search_index' in self._views[key]:
                        ddoc.add_search_index(index_name=self._views[key]['search_index']['name'], search_func=self._views[key]['search_index']['index'], analyzer=self._views[key]['search_index']['analyzer'])
                    ddoc.add_view(self._views[key]['view']['name'], self._views[key]['view']['map_reduce']['map'], reduce_func=self._views[key]['view']['map_reduce']['reduce'])
                    ddoc.save()
        except Exception as ex:
            print("An exception occurred adding the view to a design document: {}".format(ex))
    
    def insert(self, json_data):
        """
        Insert data into the database.

        :param json_data: Any kind of data
        :type json_data: dict

        :returns: If successful insertion, will return the new document id. If not it will return -1.
        :rtype: str/int
        """
        if self.db is not None:
            my_document = self.db.create_document(json_data)
            if my_document.exists():
                return my_document['_id']
        return -1
