# 长沙学院也要有自己的抢课工具 🕶

开发中,已完成基本功能

目前是 python 初学,可能之后会重构?(不会)

在 dist 内修改 'setting.json'后打开 CCSU_course.exe 即可使用 👍

---

##setting.json 说明:

"flag_AutoSelectOnline" 填入 true/false 打开自动选网课

"flag_TimeStart" 填入 true/false 打开定时启动

"StartTime" 填入 "x-x-x x:x:x" 即 "年-月-日 时:分:秒" 设置定时启动的时间

"flag_AutoSelectKeyWord" 填入 true/false 打开根据关键字的自动选课

"KeyWord" []中填入想要匹配的关键字

---

## 想要运行源代码？

所需包安装:

`pip install cryptography requests bs4 rsa six`

---

## 待办事项

1.异常处理

2.定时启动(已完成)

3.体育课直抢(添加关键字直抢,查找课程名中包含所设关键字的课程直接抢课-未测试)

4.课程捡漏

5.ABCD 类课程区分显示(已完成)

6.多线程的单课查询(已完成)

7.选择课程后的冲突课程排除/重查

8.多维度的关键字匹配(已添加教师,课程名)

9.子请求封装

---

[RSA 加密部分(jsFunction.py)来自,很难不磕一个](https://github.com/Kunz1Pro/CUMT-jwxt/tree/master)
