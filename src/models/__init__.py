from src.models.cloudant.abstract_model import AbstractModel
from src.models.cloudant.connections import db_maps

class ModelService:
    """
    Model services for directing data operation flow on different tables.
    """

    @staticmethod
    def get_instance(db_index):
        """
        Get a database Instance. 
        
        :return: Cloudant instance
        :rtype: database connection
        """
        return AbstractModel(db_maps[db_index])
    
    @staticmethod
    def testdboperation(id):
        """
        This is a sample
        """
        db = ModelService.get_instance("my_db_key")
        return db.get_doc_id(id)
