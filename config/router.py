"""
Database Router Configuration
"""

class DatabaseRouter:
    """
    A router to control all database operation on models
    """
    default_database = 'default'
    APP_ROUTE = {
        'silk': 'profilling',
    }

    def db_for_read(self, model, **hint):
        """
        control the database when reading model
        """
        return self.APP_ROUTE.get(model._meta.app_label, self.default_database)

    def db_for_write(self, model, **hint):
        """
        control the database when writing model
        """
        return self.APP_ROUTE.get(model._meta.app_label, self.default_database)

    def allow_relation(self, obj1, obj2, **hint):
        """
        Allow relations between models
        """
        return obj1._meta.app_label == obj2._meta.app_label

    def allow_migrate(self, db_alias, app_label, model_name=None, **hint):
        """
        Determine if the migration operation is allowed to run on the database with alias db.
        Return True if the operation should run, False if it shouldn’t run, or None if the router has no opinion.
        """
        return None
