from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from pytz import timezone


# Create your models here.
class Update(models.Model):
    update = models.IntegerField(null=True, blank=True, default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True) # datetime of object creation
    next_allowed_update = models.DateTimeField(
            default=datetime.now()+timedelta(minutes=1)-timedelta(hours=5)
        )
    location = models.CharField(max_length=30, default='defaultlocation')

    # in shell you can add an entry like this:
    # from main.models import Update
    # from datetime import datetime, timedelta
    #
    # > user=User.objects.create_user('user1', password='RaNdOm!@#')
    # > user.save()
    # > p = Update(update=12, user=user, date=datetime.now(), location='starbucks')
    # > p.save()

    # select user_id with the most updates
    #    mysql> select user_id, COUNT(user_id) as most from main_update group by user_id order by COUNT(user_id) DESC <limit 1>;

    # To get user information
    #    mysql> select id, first_name, email from auth_user;

    # To get number of users / number of updates
    #    mysql> select count(id) from main_update; 
    #    mysql> select count(id) from auth_user;