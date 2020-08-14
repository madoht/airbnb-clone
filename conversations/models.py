from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    """ Conversations Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return " ".join(usernames)


class Message(core_models.TimeStampedModel):

    """ Messages Model Definition """

    messages = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.messages}"
