import requests

class SendComment():
    url = 'https://api.live.bilibili.com/msg/send'

    def __init__(self, cookie, roomId, csrf, rnd):
        self.roomid = roomId
        self.csrf = csrf
        self.csrf_token = csrf
        self.rnd = rnd
        self.cookie = cookie

    def send(self, messege):
        form_data = {
            # color 16777215 为普通白色弹幕，因为不保证特殊弹幕颜色每个人都有
            'color': '16777215',
            'fontsize': '25',
            'mode': '1',
            'msg': messege,
            #'rnd': '1583317514',时间戳
            'rnd': self.rnd,
            'roomid': self.roomid,
            'bubble': '0',
            'csrf_token': self.csrf,
            'csrf': self.csrf
        }
        # 设置cookie值帮助我们在发送弹幕的时候，服务器识别我们的身份
        cookie = {
            #'Cookie': 'DedeUserID=776474; DedeUserID__ckMd5=2c47b272bd8b70f7; SESSDATA=c4e3d2fb%2C1583946040%2C28d20021;'
            'Cookie': self.cookie
        }
        res = requests.post('https://api.live.bilibili.com/msg/send', cookies=cookie, data=form_data)

        if (res.status_code == '200') :
            print("发送成功")
        else:
            print("发送失败！")