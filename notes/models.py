from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    owner_id_FK = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    ori_note_id = models.IntegerField()
    ref_note_id = models.IntegerField()

    def __str__(self):
        return str(self.ori_note_id) + ' to ' + str(self.ref_note_id)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id_FK = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name='img_', upload_to='')

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=20)
    note_id_FK = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tag_name
