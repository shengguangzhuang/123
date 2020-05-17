class MobileConverter:
    '''自定义路由转换器：匹配手机号'''
    # 匹配手机号的正则
    regex = '1[3-9]\d{9}'


    def to_python(self,value):

        return int(value)
    def to_url(self,value):

        return str(value)