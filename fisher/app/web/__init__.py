from flask import Blueprint

web=Blueprint('web',__name__)

# 注意，如果一下两个导入放到web前边会报错，因为web还没初始化
from app.web import book
from app.web import user