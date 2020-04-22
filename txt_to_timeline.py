# -*- coding: utf-8 -*-
# txt_to_html.py
# author: yangrui
# description: 
# created: 2020-04-10T10:40:32.186Z+08:00
# last-modified: 2020-04-10T10:40:32.186Z+08:00
# email: yangrui19@mails.tsinghua.edu.cn

from utils import *
import argparse


def add_html(html, ids, temp_str):
    box_head, box_end = get_box(ids)
    html += box_head + temp_str + '</div>' + box_end
    ids += 1
    return html, ids

def process(path='story.txt', css='index.css', add_heart=True):
    assert path.endswith('.txt'), 'path file should be txt'
    head, end = html_body(path.rstrip('.txt'), css=css, add_heart=add_heart)
    html = head
    lines = read_txt(path)
    temp_str = ''
    ids = 0
    for i, line in enumerate(lines):
        line = line.rstrip('\n').strip()

        if not len(line):  # 空行
            continue

        if line.startswith('-'):  # 开始
            if len(temp_str):
                html, ids = add_html(html, ids, temp_str)

            # 添加日期
            temp_str = '''<div class="box-date">
                            <span>{}</span>
                            </div>
                            <div class="box-text">'''.format(line[1:].strip())
            
        elif is_image(line):
            temp_str += '<img src="{}" />'.format(line)

        else:
            if line.startswith('#'):
                num = line[:3].count('#')
                temp_str += '<h{}>{}</h{}>'.format(num, line.lstrip('#'), num)
            else:
                temp_str += '<p>{}</p>'.format(line)

    html, ids = add_html(html, ids, temp_str)
    html += end
    save_path = path.replace('txt','html')
    save_txt(save_path, html)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        type=str,
        default='story.txt',
        help='Where the text file is.'
    )
    parser.add_argument(
        '--css',
        type=str,
        default='index.css',
        help='Where the css file is.'
    )
    parser.add_argument(
        '--add_heart',
        type=bool,
        default=True,
        help='If to use a heart effect.'
    )
    args = parser.parse_args()
    process(args.path, args.css, args.add_heart)