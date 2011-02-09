from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save, pre_save
#import markdown
from thodol.wiki.controllers import CodeBlockPreprocessor
from markdown import Markdown

md = Markdown()
import ipdb; ipdb.set_trace()
md.preprocessors.insert(0, CodeBlockPreprocessor())
markdown = md.__str__

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

class Page(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    last_changed = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    def __unicode__(self):
        return unicode(self.slug)
    def render_content(self):
        return unicode(markdown(self.content))

class Record(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    last_changed = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    record_of = models.ForeignKey(Page)
    def __unicode__(self):
        return unicode(self.slug)

def slugify_name(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
        instance.save()

post_save.connect(slugify_name, sender=Page)

def save_record(sender, instance, **kwargs):
    if get_or_none(Page, name=instance.name):
        record = Record(name=instance.name, 
                        slug=instance.slug, 
                        content=instance.content, 
                        record_of=instance)
        record.save()

pre_save.connect(save_record, sender=Page)