# EXCITED

A Distributed Search Engine

##Features

1. 自动抓取互联网上的页面，并解析出文本。文本和网页HTML镜像都存储在服务器上。（支持解析动态网页）

2. 对文本进行中文分词

3. 对分词后的文本建立倒排索引和keywords词典

4. 对于用户的搜索请求，返回对应的URL

5. 上述系统将运行在一个分布式集群上（暂定1 Master + 4 Slave + 1 Cache），基于自行开发的类MapReduce计算框架和分布式数据库。

##Unsupported Features

1. 集群节点实时添加、脱机

2. 文件系统层次的容错机制

##Undetermined Features

1. 结果相关度排序
