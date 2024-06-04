from django.db import models
from base_models import BaseModel

# Create your models here.


class CaseThemeModel(BaseModel):
    """ 案例主题模型 """
    name = models.CharField(max_length=20, verbose_name="名称")
    index = models.SmallIntegerField(verbose_name="顺序")
    remark = models.CharField(max_length=50, verbose_name="备注")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "db_case_theme"
        verbose_name = "案例主题"
        verbose_name_plural = verbose_name


class CaseContentModel(BaseModel):
    """ 案例内容模型 """
    theme = models.ForeignKey(CaseThemeModel, on_delete=models.CASCADE, verbose_name="主题")
    name = models.CharField(max_length=20, verbose_name="名称")
    content = models.TextField(verbose_name="内容")
    index = models.SmallIntegerField(verbose_name="顺序")
    remark = models.CharField(max_length=50, verbose_name="备注")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "db_case_content"
        verbose_name = "案例内容"
        verbose_name_plural = verbose_name
