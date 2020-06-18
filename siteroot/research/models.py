from django.db.models import *

class Researcher(Model):

    author = CharField(max_length=80)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return 'id:%s %s %s' % (self.id, self.author, self.created_at)

class Post(Model):
    post = ForeignKey(Researcher, on_delete=CASCADE)
    author_id = PositiveSmallIntegerField(default=1)
    subject = CharField(max_length=80)
    text = TextField(max_length=4096)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    updated_at = DateTimeField('update timestamp', auto_now=True)

    def __str__(self):
        return 'id:%s researcher_id:%s %s %s' % (self.post_id, self.author_id, self.subject, self.text, self.created_at)
