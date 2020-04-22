# -*- coding: utf-8 -*-
# utils.py
# author: yangrui
# description: 
# created: 2020-04-10T11:05:29.209Z+08:00
# last-modified: 2020-04-10T11:05:29.209Z+08:00
# email: yangrui19@mails.tsinghua.edu.cn


def html_body(title='documentory', css='index.css', add_heart=True):
    heart = ''
    if add_heart:  # 点击爱心代码
        heart = '''<script type="text/javascript">
        !function (e, t, a) {function r() {for (var e = 0; e < s.length; e++) s[e].alpha <= 0 ? (t.body.removeChild(s[e].el), s.splice(e, 1)) : (s[e].y--, s[e].scale += .004, s[e].alpha -= .013, s[e].el.style.cssText = "left:" + s[e].x + "px;top:" + s[e].y + "px;opacity:" + s[e].alpha + ";transform:scale(" + s[e].scale + "," + s[e].scale + ") rotate(45deg);background:" + s[e].color + ";z-index:99999");requestAnimationFrame(r)}function n() {var t = "function" == typeof e.onclick && e.onclick;e.onclick = function (e) {t && t(), o(e)}}function o(e) {var a = t.createElement("div");a.className = "heart", s.push({el: a,x: e.clientX - 5,y: e.clientY - 5,scale: 1,alpha: 1,color: c()}), t.body.appendChild(a)}function i(e) {var a = t.createElement("style");a.type = "text/css";try {a.appendChild(t.createTextNode(e))} catch (t) {a.styleSheet.cssText = e}t.getElementsByTagName("head")[0].appendChild(a)}function c() {return "rgb(" + ~~(255 * Math.random()) + "," + ~~(255 * Math.random()) + "," + ~~(255 * Math.random()) + ")"}var s = [];e.requestAnimationFrame = e.requestAnimationFrame || e.webkitRequestAnimationFrame || e.mozRequestAnimationFrame || e.oRequestAnimationFrame || e.msRequestAnimationFrame || function (e) {setTimeout(e, 1e3 / 60)}, i(".heart{width: 10px;height: 10px;position: fixed;background: #f00;transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);}.heart:after,.heart:before{content: '';width: inherit;height: inherit;background: inherit;border-radius: 50%;-webkit-border-radius: 50%;-moz-border-radius: 50%;position: fixed;}.heart:after{top: -5px;}.heart:before{left: -5px;}"), n(), r()}(window, document);
        </script>'''
        
    head = '''<!DOCTYPE html>
            <html lang="en">
            <head>
            {}
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
             <title>{}</title>
            <link rel="stylesheet" href='{}'>
            </head>
            <body>
            <div class="wrapper">'''.format(heart, title, css)

    end = '''
            </div>
            </body> 
            </html>'''
    return head, end

def get_box(i, two_side=True):
    if two_side:
        if i % 2:
            box_head = '<div class="box-area box-right">'
        else:
            box_head = '<div class="box-area">'
    else:
        box_head = '<div class="box-area">'
    box_head += '<div class="custom"></div>'
    box_end = '''</div>''' 
    return box_head, box_end

def is_image(path):
    if path.split('.')[-1].lower() in ['jpg','png', 'jpeg']:
        return True
    else:
        return False

def read_txt(path):
    assert path.endswith('.txt'), 'read path type should be txt!'
    with open(path, 'r') as file:
        data = file.readlines()
    return data

def save_txt(path, data):
    # assert path.endswith('.txt'), 'save path type should be txt!'
    with open(path, 'w') as file:
        file.write(data)
    print('write finished')


