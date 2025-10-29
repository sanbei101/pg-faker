import glob
import os
import subprocess
import sys

os.makedirs("dist", exist_ok=True)
py_scripts = glob.glob("*-fake.py")
py_scripts.sort()

print("正在运行以下脚本生成 SQL 文件：")
for script in py_scripts:
    print(f"  - {script}")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"❌脚本 {script} 执行失败,退出", file=sys.stderr)
        sys.exit(1)

print("\n✅所有脚本执行完毕,开始合并 SQL 文件...\n")

sql_files = glob.glob("*-fake.sql")
sql_files.sort()

fake_sql = ""
install_sql = """CREATE SCHEMA IF NOT EXISTS fake;
SET search_path TO fake;\n"""
for sql_file in sql_files:
    with open(sql_file, "r") as f:
        content = f.read()
        fake_sql += f"--- 开始文件: {sql_file} ---\n"
        install_sql += f"--- 开始文件: {sql_file} ---\n"
        
        fake_sql += content + "\n"
        install_sql += content + "\n"
        
        fake_sql += f"--- 结束文件: {sql_file} ---\n\n"
        install_sql += f"--- 结束文件: {sql_file} ---\n\n"

version = os.getenv("VERSION", "1.0")
# 生成 fake.control 文件
fake_control = f"""comment = 'A fake data generator for postgres'
default_version = '{version}'
relocatable = false
schema = fake"""

with open("extension/fake.control", "w") as f:
    f.write(fake_control)

# 生成 Makefile 文件
make_file = f"""EXTENSION = fake
DATA = fake--{version}.sql
PGXS := $(shell pg_config --pgxs)
include $(PGXS)"""

with open("Makefile", "w") as f:
    f.write(make_file)

# 生成合并后的 fake.sql 文件
with open(f"extension/fake--{version}.sql", "w") as f:
    f.write(fake_sql)

with open(f"dist/fake-{version}-install.sql", "w") as f:
    f.write(install_sql)