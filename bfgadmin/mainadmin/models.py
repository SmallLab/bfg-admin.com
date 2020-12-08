from django.db import models
from django.contrib.auth.models import User
from mainadmin.mainhelpers import MainImgTypeField as MI

"""-------------------------------- Categories Model -------------------------------------------"""

"""
Custom Manager for model Categories
"""


class ManagerCategories(models.Manager):
  # Get active Categories
  def get_active_categories(self):
    return self.get_queryset().filter(is_active__exact=True)

  # Get categories on 5 ps.
  def get_list_categories(self):
    activecategories = self.get_active_categories()
    return [activecategories[i:i + 5] for i in range(0, len(activecategories), 5)]


class Categories(models.Model):
  name = models.CharField(max_length=50)
  link_name = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  icon_style = models.CharField(max_length=50, default='')
  is_icon_img = models.BooleanField(default=False)
  max_num = models.SmallIntegerField(default=1)
  paid_num = models.SmallIntegerField(default=5)
  object = ManagerCategories()

  class Meta:
    db_table = 'mainbfg_categories'

  def get_absolute_url(self):
    return "/categories/%s/" % self.link_name

  def __str__(self):
    return self.name


"""-------------------------------- Regions Model -------------------------------------------"""
class ManagerRegions(models.Manager):
  def get_active_categories(self):
    return self.get_queryset()


class Regions(models.Model):
  name = models.CharField(max_length=100)
  link_name = models.CharField(max_length=100)
  is_active = models.BooleanField(default=True)
  object = ManagerRegions()

  def get_absolute_url(self):
    return "/%s/" % self.link_name

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'mainbfg_regions'


"""------------------------- TypeSentence Model -----------------------------------------------"""
"""
Custom Manadger for model TypeSentence
"""


class ManagerTypeSentence(models.Manager):
  # Get active Types
  def get_active_types(self):
    return self.get_queryset().filter(is_active__exact=True)


class TypeSentence(models.Model):
  name = models.CharField(max_length=50)
  link_name = models.CharField(max_length=50, default='')
  is_active = models.BooleanField(default=True)
  object = ManagerTypeSentence()

  def get_absolute_url(self):
    return "/%s/" % self.link_name

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'mainbfg_typesentence'


""""-------------------------------- Profile Model -------------------------------------------"""
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone = models.CharField(blank=True, max_length=100)
  email = models.EmailField(blank=True, max_length=255)
  favorite_num = models.SmallIntegerField(blank=True, default=0)
  is_subscrabtion = models.BooleanField(default=False)
  is_subscriber = models.BooleanField(default=False)
  facebook_id = models.BigIntegerField(blank=True, default=0)
  vk_id = models.IntegerField(blank=True, default=0)
  first_name = models.CharField(max_length=50, blank=True)
  last_name = models.CharField(max_length=50, blank=True)

  class Meta:
    db_table = 'mainbfg_profile'


"""-----------------------------------Sentence Model-----------------------------------------"""


def custom_directory_path(instance, filename):
  return 'images/{0}/{1}'.format(instance.dirname_img, filename)


class ManagerSentences(models.Manager):

  def get_single_sentence(self, pk):
    try:
      return Sentence.objects.get(pk=pk)
    except Sentence.DoesNotExist:
      return False

  def get_sent_for_mode(self):
    try:
      return Sentence.objects.using("mainbfg").order_by('-create_time').filter(on_moderation=0).filter(status=0)[0]
    except IndexError:
      return False

  def set_mode_result(self, kwargs):
    sentence = Sentence.objects.using("mainbfg").get(pk=kwargs['pk'])
    sentence.status = kwargs['status']
    sentence.on_moderation = False
    sentence.save()
    # Save record for sending messges on subscrabers
    if kwargs['status'] == 1:
      pass


class Sentence(models.Model):
  type_id = models.SmallIntegerField()
  category_id = models.SmallIntegerField()
  sub_id = models.SmallIntegerField(default=0)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentences')
  autor = models.CharField(max_length=30, error_messages={'max_length': 'Required error'})
  caption = models.CharField(max_length=50)
  region_id = models.SmallIntegerField()
  full_adress = models.CharField(max_length=100, blank=True)
  phone = models.CharField(max_length=100, blank=True)
  web_site = models.CharField(max_length=250, blank=True)
  is_webstore = models.BooleanField(default=False)
  description = models.TextField(max_length=1000)
  meta_info = models.CharField(max_length=500, blank=True)
  main_img = MI.MainImgTypeField(upload_to=custom_directory_path,
                                 # content_types=['image/jpeg', 'image/jpg', 'image/png', 'image/jpeg'],
                                 blank=True, default='nophoto.png')
  dirname_img = models.CharField(max_length=15, default='', blank=True)
  create_time = models.DateTimeField(auto_now_add=True)
  stop_time = models.DateTimeField(blank=True)
  status = models.SmallIntegerField(default=0)  # 0 - on moderations, 1 - published, 2 - on editing
  type_s = models.SmallIntegerField(default=0)  # 0 - usual, 1 - TOP, 2 - VIP
  type_img_s = models.CharField(max_length=300, blank=True)  # path to img (Stock, Discount, Sale)
  views = models.IntegerField(default=0)
  phone_views = models.IntegerField(default=0)
  text_message = models.CharField(max_length=1000, blank=True)
  is_paid = models.BooleanField(default=False)
  start_time_paid = models.DateTimeField(auto_now_add=True)
  end_time_paid = models.DateTimeField(auto_now_add=True)
  on_moderation = models.BooleanField(default=False)
  link_name = models.CharField(max_length=550)
  identifier = models.CharField(max_length=20)
  objects = ManagerSentences()

  def get_absolute_url(self):
    return "sentence/%s" % self.link_name

  def __str__(self):
    return self.link_name

  class Meta:
    db_table = 'mainbfg_sentence'


"""---------------------------------Images Model----------------------------------------------"""
class ImageManager(models.Manager):
  def get_queryset(self, *args, **kwargs):
    return super().get_queryset(*args, **kwargs)


class Image(models.Model):
  sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE, related_name='image')
  img_path = models.CharField(max_length=250, blank=True)
  object = ImageManager()

  def get_absolute_url(self):
    return self.img_path

  class Meta:
    db_table = 'mainbfg_image'


"""--------------------------------------Notification Model-----------------------------------"""


class ManageNotificationTask(models.Manager):
  pass


class NotificationTask(models.Model):
  sent_id = models.IntegerField()
  user_id = models.IntegerField()
  text_message = models.CharField(default='', max_length=100)
  data_send_sms = models.TextField()  # Phone numbers for send SMS
  data_send_email = models.TextField()  # EMAIL data for send email
  is_send = models.BooleanField(default=False)
  objects = ManageNotificationTask()
