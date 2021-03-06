from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
def savefile(self,filename):
    return 'files/resources/{0}/{1}_{2}'.format(self.author,self.id,filename)

class Resource(models.Model):
    title = models.CharField(max_length = 1000)
    content = models.TextField()
    classes = models.CharField(max_length=50)
    subject = models.CharField(max_length=50,default='Other')
    files = models.FileField(upload_to=savefile, max_length=100,null=True,blank=True,default=None)
    date = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    video_link = models.CharField(max_length=5000,null=True,blank=True,default='None')
    
    class Meta:
        verbose_name_plural = 'Resources'
        db_table = 'resources'

    def filetype(self):
        if(self.files == None):
            return 'None'
        ext = self.files.name.split('.')
        ext = '.'+ext[-1]
        img = {'.jpg':1,'.png':1,'.jpeg':1,}
        print(ext)
        filetype = 'other'
        if(ext in img):
            filetype = 'image'
        elif(ext == '.pdf'):
            filetype = 'pdf'
        print(filetype)
        return filetype
    
    def  __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('resources')