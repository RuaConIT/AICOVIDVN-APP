from django.db import models

gender_choise = (('nam', 'Nam'), ('nữ', 'Nữ'))


class Survey(models.Model):

    uuid = models.CharField(max_length=100, default="", blank=True, null=True)
    gender = models.CharField(max_length=5,
                              choices=gender_choise,
                              default='Nam')
    age = models.IntegerField("Nhập tuổi", default=18)
    result = models.BooleanField(default=False)
    audio_path = models.FileField(default="", blank=True, null=True)

    def __str__(self):
        return self.uuid

    class Meta:
        db_table = 'survey'