from django.db import models

class User(models.Model):
  email = models.EmailField(max_length=254)

  @classmethod
  def get_or_create_from_email(clazz, email):
    email = email.lower()
    try:
      return clazz.objects.get(email=email)
    except clazz.DoesNotExist:
      pass
    user = clazz(email=email)
    user.save()
    return user

  @classmethod
  def get_from_email(clazz, email):
    return clazz.objects.get(email=email)

  def unread_messages(self):
    return self.message_set.filter(is_read=False, direction=Message.OUT)

  def get_last_10_messages(self):
    return self.message_set.all().order_by('-time_stamp')[:10]

  def unread_count(self):
    return self.unread_messages().count()

  def __unicode__(self):
    return self.email


class Message(models.Model):
  user = models.ForeignKey(User)
  message = models.TextField()
  is_read = models.BooleanField(default=False)
  time_stamp = models.DateTimeField(auto_now_add=True, db_index=True)
  direction = models.CharField(max_length=1)

  # Direction Constants
  IN = 'I'
  OUT = 'O'

  @classmethod
  def for_user_and_id(clazz, user, message_id):
    return clazz.objects.get(user=user, id=message_id)

  def mark_read(self):
    self.is_read = True
    self.save()

  def __unicode__(self):
    return "To={} Read?={} Message={}".format(self.user, self.is_read, self.message)
