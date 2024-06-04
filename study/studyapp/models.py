from django.db import models
from base_models import BaseModel

# Create your models here.

class outlineModel(BaseModel):
    """大纲模型"""
    name = models.CharField(max_length=20, verbose_name="名称")
    index = models.SmallIntegerField(verbose_name="顺序")
    remark = models.CharField(max_length=50, verbose_name="备注")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "db_app_outline"
        verbose_name = "大纲"
        verbose_name_plural = verbose_name



