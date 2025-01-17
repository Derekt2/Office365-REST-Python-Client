from office365.mail.item import Item
from office365.runtime.queries.service_operation_query import ServiceOperationQuery


class Message(Item):
    """A message in a mailbox folder."""

    def reply(self):
        """Reply to the sender of a message by specifying a comment and using the Reply method. The message is then
        saved in the Sent Items folder. """
        qry = ServiceOperationQuery(self, "reply")
        self.context.add_query(qry)
        return self

    def move(self):
        """Move a message to a folder. This creates a new copy of the message in the destination folder. """
        qry = ServiceOperationQuery(self, "move")
        self.context.add_query(qry)
        return self
