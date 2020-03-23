import random
import string
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from blog.settings import PICTURE_PATH

class PictureVerify:
    def __init__(self,width=120,height=42,size=4):
        """
          width: 验证码图片宽度
          height: 验证码图片高度
          size: 验证码图片字符数
        """
        self.width = width
        self.height = height
        self.size = size
        self.__code = '' # 验证码字符串
        self.pen = None # 画笔
        """
            PICTURE_PATH:字体路径
            size=25:字体大小
        """
        self.font_tmp = ImageFont.truetype(PICTURE_PATH,size=25,encoding='utf-8')

    def  generate(self):
        # 1)、创建画布
        im = Image.new('RGB',(self.width,self.height),self.__rand_color(150))
        self.pen = ImageDraw.Draw(im)
        # 2)、生成验证码字符串
        self.rand_string()
        # 3)、画验证码
        self.__draw_code()
        # 4)、画干扰点
        self.__draw_point()
        # 5)、画干扰线
        self.__rand_line()
        # 6)、返回验证码图片
            # 缓冲区
        buf = BytesIO()
            # 把图片放到缓冲区
        im.save(buf,'png')
            # 获取图片的二进制
        res = buf.getvalue()
        buf.close()
        return res
    # 生成验证码字符串(随机字母+数字)
    def rand_string(self):
        self.__code = ''
        self.__code = "".join(random.sample(string.digits+string.ascii_letters, 4))
    # 生成随机图片底色
    def __rand_color(self,min=0,max=255):
        return random.randint(min,max),random.randint(min,max),random.randint(min,max)
    # 生成验证码
    def __draw_code(self):
        # 计算字符宽度
        width = (self.width - 17) // self.size
        # 逐个画字符
        for i in range(len(self.__code)):
            x = 15 + width * i # 计算每个字符的x坐标
            y = random.randint(3,12) # 随机生成每个字符的y坐标
            self.pen.text((x,y),self.__code[i],font=self.font_tmp,fill=self.__rand_color(0,80))
    # 生成干扰点
    def __draw_point(self):
        for i in range(100):
            self.pen.point((random.randint(1, self.width - 1), random.randint(1, self.height - 1)), self.__rand_color(30, 100))
    # 生成干扰线
    def __rand_line(self):
        for i in range(5):
            """
                width=2:线宽
            """
            self.pen.line([(random.randint(1, self.width - 1), random.randint(1, self.height - 1)), (random.randint(1, self.width - 1), random.randint(1, self.height - 1))], fill=self.__rand_color(50, 150), width=2)

    @property
    def code(self):
        return self.__code

# 单例属性
pv = PictureVerify()