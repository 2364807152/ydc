#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xueshengxuehao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='xueshengxuehao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xueshengxuehao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='学生学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    mima=models.CharField ( max_length=255, null=True, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    zhuanye=models.CharField ( max_length=255, null=True, unique=False, verbose_name='专业' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    nianji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='年级' )
    '''
    xueshengxuehao=VARCHAR
    xueshengxingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    zhuanye=VARCHAR
    lianxidianhua=VARCHAR
    yuanxi=VARCHAR
    banji=VARCHAR
    nianji=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class jiaoshi(BaseModel):
    __doc__ = u'''jiaoshi'''
    __tablename__ = 'jiaoshi'

    __loginUser__='jiaoshigonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='jiaoshigonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaoshigonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='教师工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    jiaoshixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    zhicheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='职称' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    '''
    jiaoshigonghao=VARCHAR
    mima=VARCHAR
    jiaoshixingming=VARCHAR
    xingbie=VARCHAR
    zhicheng=VARCHAR
    lianxidianhua=VARCHAR
    '''
    class Meta:
        db_table = 'jiaoshi'
        verbose_name = verbose_name_plural = '教师'
class kechengxinxi(BaseModel):
    __doc__ = u'''kechengxinxi'''
    __tablename__ = 'kechengxinxi'



    __authTables__={'jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='课程编号' )
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    kechengleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程类型' )
    keshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课时' )
    shangkedidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='上课地点' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    kechengxiangqing=models.TextField   (  null=True, unique=False, verbose_name='课程详情' )
    kechengbiao=models.TextField   (  null=True, unique=False, verbose_name='课程表' )
    '''
    kechengbianhao=VARCHAR
    kechengmingcheng=VARCHAR
    kechengleixing=VARCHAR
    keshi=VARCHAR
    shangkedidian=VARCHAR
    tupian=VARCHAR
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    kechengxiangqing=Text
    kechengbiao=Text
    '''
    class Meta:
        db_table = 'kechengxinxi'
        verbose_name = verbose_name_plural = '课程信息'
class qiandaoxinxi(BaseModel):
    __doc__ = u'''qiandaoxinxi'''
    __tablename__ = 'qiandaoxinxi'



    __authTables__={'xueshengxuehao':'xuesheng','jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程编号' )
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    xueshengxuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    qiandaoshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='签到时间' )
    qiandaoleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='签到类型' )
    beizhu=models.TextField   (  null=True, unique=False, verbose_name='备注' )
    '''
    kechengbianhao=VARCHAR
    kechengmingcheng=VARCHAR
    xueshengxuehao=VARCHAR
    xueshengxingming=VARCHAR
    banji=VARCHAR
    jiaoshigonghao=VARCHAR
    qiandaoshijian=DateTime
    qiandaoleixing=VARCHAR
    beizhu=Text
    '''
    class Meta:
        db_table = 'qiandaoxinxi'
        verbose_name = verbose_name_plural = '签到信息'
class qingjiashenqing(BaseModel):
    __doc__ = u'''qingjiashenqing'''
    __tablename__ = 'qingjiashenqing'



    __authTables__={'xueshengxuehao':'xuesheng','jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xueshengxuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    kaishishijian=models.DateField   (  null=True, unique=False, verbose_name='开始时间' )
    jieshushijian=models.DateField   (  null=True, unique=False, verbose_name='结束时间' )
    liyou=models.TextField   (  null=True, unique=False, verbose_name='理由' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    xueshengxuehao=VARCHAR
    xueshengxingming=VARCHAR
    jiaoshigonghao=VARCHAR
    kaishishijian=Date
    jieshushijian=Date
    liyou=Text
    shenqingshijian=DateTime
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'qingjiashenqing'
        verbose_name = verbose_name_plural = '请假申请'
class kaoqinxinxi(BaseModel):
    __doc__ = u'''kaoqinxinxi'''
    __tablename__ = 'kaoqinxinxi'



    __authTables__={'jiaoshigonghao':'jiaoshi','xueshengxuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    kechengbianhao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程编号' )
    kechengmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='课程名称' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    xueshengxuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    qiandaocishu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='签到次数' )
    qingjiacishu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='请假次数' )
    chidaocishu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='迟到次数' )
    kuangkecishu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='旷课次数' )
    dengjishijian=models.DateField   (  null=True, unique=False, verbose_name='登记时间' )
    '''
    kechengbianhao=VARCHAR
    kechengmingcheng=VARCHAR
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    xueshengxuehao=VARCHAR
    xueshengxingming=VARCHAR
    qiandaocishu=VARCHAR
    qingjiacishu=VARCHAR
    chidaocishu=VARCHAR
    kuangkecishu=VARCHAR
    dengjishijian=Date
    '''
    class Meta:
        db_table = 'kaoqinxinxi'
        verbose_name = verbose_name_plural = '考勤信息'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'
