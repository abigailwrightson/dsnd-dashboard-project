# Import any dependencies needed to execute sql queries
from .sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):
    """
    Base class for querying the employee_events database
    """
    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    @classmethod
    def names(cls):
        """
        Returns an empty list; to be overridden by subclasses if needed
        """
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    @classmethod
    def event_counts(cls, id):
        """
        Returns a pandas dataframe of event counts
        """
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        query = f"""
        SELECT event_date,
               SUM(positive_events) AS total_positive_events,
               SUM(negative_events) AS total_negative_events
        FROM employee_events
        WHERE {cls.name}_id = {id}
        GROUP BY event_date
        ORDER BY event_date
        """
        instance = cls()
        return instance.pandas_query(query)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    @classmethod
    def notes(cls, id):
        """
        Returns a pandas dataframe of notes
        """
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        query = f"""
        SELECT note_date, note
        FROM notes
        WHERE {cls.name}_id = {id}
        """
        instance = cls()
        return instance.pandas_query(query)

