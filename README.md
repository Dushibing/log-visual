简介：
---

日常的各种应用都有很多的日志文件，某些特殊的应用需要分析日志，对于较小的应用我门可以采用自己编写脚本工具来完成分析，那么对于大型应用的日志数据，我们就需要借用开源软件帮助我们完成。我将会分两部分来讲，第一部分是介绍如何使用Python+echart 完成日志可视化的任务，后部分讲给大家介绍如何使用Elasticsearch + logstash + Kibana 实现对日志的实时大批量的数据可视化。

##Python实现

背景：如果老板让你对一个web应用的访问日志进行分析，给力你一些基本的要求，比如说访问量最大的IP地址，防止爬虫影响网站运行。分析访问客户的一些特征。

1.简单版本
你写了一个脚本，去分析日志，出一个报表，基本满足了老板的要求，但是没有什么特点，不能让你的工作出色。
2. Django版本
你整懂得一些web开发知识，决定写一个一个web工具报表更好的展示，这样了老板就不用每次都查看邮件了，只要点点就能找到他想看到的数据。

![这里写图片描述](http://img.blog.csdn.net/20170507152904212?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYWZ4Y29udHJvbGJhcnM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
2.1 这样他只显示前10可能不够，偶尔会看到后面的，做好是能查看所有的，按照访问量排序。
![这里写图片描述](http://img.blog.csdn.net/20170507153119810?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYWZ4Y29udHJvbGJhcnM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这样的版本基本上对于绝大多数运维来说已经够了，老板说小伙子不错啊！但是如果你是一个开发，这样显然是不够的。然后我就有开发一个用图来展示的版本。
![这里写图片描述](http://img.blog.csdn.net/20170507153522316?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYWZ4Y29udHJvbGJhcnM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
![这里写图片描述](http://img.blog.csdn.net/20170507153543269?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYWZ4Y29udHJvbGJhcnM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

利用echart实现了可以调节时间的显示，并且可以下载图片，老板看到这个版本可能说小伙子不错啊，有发展前途，年底涨工资。

3.Django酷炫版本
这样已经满足了可视化的要求，既美观又直接，但是不够惊艳，你想做的更加惊艳一些，然后我就有做出来一个更牛逼的版本。
![这里写图片描述](http://img.blog.csdn.net/20170507154135136?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYWZ4Y29udHJvbGJhcnM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

老板看到这个版本直接和HR说这个月就加工资。哈哈都是自己幻想的。

最后一图幅可视化图数据是微博的数据，由于暂时只找到这一份数据。以上都是自己实现几个日志可视化例子，对于一般的网站日志分析应该是已经够了，我将会在下面把实现源码链接贴出来，日志数据来源于网络，所以不要做任何对应关系，日志数量比较少，所以图标出来并不是很漂亮，这样对于一些较小的应用已经够了，但是对于大型应用，巨量日志的实时分析就不能采用以让的方法，必须借用一些开源软件的结合。

源码: https://github.com/Dushibing/log-visual

ELK
---

待续
![这里写图片描述](http://img.blog.csdn.net/20170507215044955?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYWZ4Y29udHJvbGJhcnM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
