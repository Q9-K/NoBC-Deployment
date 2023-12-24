# 说明文档

> author: q9k
>
> date: 12.23

这是**NoBC-Academic**的部署文档
部署方式:

- 创建一个.env 文件，填写`RABBITMQ_PASSWORD`, `RABBITMQ_USER`, `MYSQL_PASSWORD`
- 将前后端项目文件移至对应目录, 设置 Dockerfile 的对应目录
- 运行 docker-compose up -d
