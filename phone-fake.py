from utils import format_array_sql

mobile_prefixes = [str(i) for i in range(130, 200)]

sql = f"""-- fake手机号码(Python 自动生成)
CREATE OR REPLACE FUNCTION phone()
RETURNS TEXT AS $$
DECLARE
    mobile_prefixes TEXT[] := {format_array_sql(mobile_prefixes)};

    prefix_count INT := array_length(mobile_prefixes, 1);
    prefix TEXT;
    suffix TEXT;
BEGIN
    prefix := mobile_prefixes[1 + floor(random() * prefix_count)::int];

    suffix := lpad(floor(random() * 100000000)::text, 8, '0');

    RETURN prefix || suffix;
END;
$$ LANGUAGE plpgsql;
"""

with open("dist/phone-fake.sql", "w", encoding="utf-8") as f:
    f.write(sql)