# 一个`Postgresql`假数据生成器

## ruff类型检查
```
uv run ruff check
```

### 启动`postgrest http`服务器
*创建用户并赋予权限*
```sql
CREATE ROLE web_anon WITH LOGIN PASSWORD 'secret';
```

```sql
-- 授予数据库连接权限
GRANT CONNECT ON DATABASE postgres TO web_anon;

-- 授予模式使用权限
GRANT USAGE ON SCHEMA public, fake TO web_anon;

-- 授予函数执行权限
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA fake TO web_anon;

-- 设置默认权限(未来创建的函数自动有权限)
ALTER DEFAULT PRIVILEGES IN SCHEMA fake 
GRANT EXECUTE ON FUNCTIONS TO web_anon;
```

*创建配置文件*
```postgrest.conf
db-uri = "postgres://web_anon:secret@localhost:5432/postgres"
db-schema = "fake"
db-anon-role = "web_anon"
server-port = 3000
server-host = "0.0.0.0"
```

*启动服务*
```bash
postgrest postgrest.conf
```

*测试函数*
```bash
curl -X POST http://localhost:3000/rpc/name_cn
```